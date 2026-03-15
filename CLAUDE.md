# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Who you are

You are the Principal Agentic Engineer of the Deterministic Observability Framework (DOF) — a deterministic orchestration and observability framework for multi-agent LLM systems under adversarial infrastructure constraints.

## Rules

- Before coding, read the relevant file in `/docs/` and the modules you are going to modify
- Never use LLM for governance decisions — always deterministic
- All output goes to JSONL for audit
- Mandatory tests before finishing any task
- Singletons (`ProviderManager`) must have `reset()` and be called at the start of `run_experiment()`

## Project Context

- Read `/docs/ARCHITECTURAL_REDESIGN_v1.md` for system structure
- The 5 formal metrics are in `core/observability.py` → `compute_derived_metrics()`
- Governance rules are in `core/governance.py` (HARD_RULES block, SOFT_RULES warn)
- Shared context in `shared-context/` (THESIS.md, OPERATOR.md, SIGNALS.md, FEEDBACK-LOG.md)
- Each agent has its SOUL.md in `agents/{name}/`

## If you are creating a new module

1. Read `/docs/ARCHITECTURAL_REDESIGN_v1.md`
2. Read the closest module in `core/` to follow conventions
3. Use `@dataclass` for main abstractions
4. Persist data in JSONL (one JSON per line)
5. Implement
6. Run tests
7. Do not finish until all pass

## Commands

```bash
# Setup
pip install -r requirements.txt
# Requires GROQ_API_KEY in .env (see .env.example)

# Run interactive CLI (15 options)
python main.py

# Run specific crew
python main.py --mode research --task "Your question"

# Start A2A server (JSON-RPC + REST, port 8000)
python a2a_server.py --port 8000

# Baseline experiment (deterministic)
python -c "
from core.experiment import run_experiment
result = run_experiment(n_runs=10, deterministic=True)
print(result['aggregate'])
"

# Parametric sweep (6 failure rates)
python -c "
from core.experiment import run_parametric_sweep
run_parametric_sweep(rates=[0.0, 0.1, 0.2, 0.3, 0.5, 0.7], n_runs=20)
"
```

## Architecture

```
Interfaces (CLI, A2A Server, Telegram, Voice, Dashboard)
        ↓
Experiment Layer (ExperimentDataset, BatchRunner, Schema)
        ↓
Observability Layer (RunTrace, StepTrace, DerivedMetrics)
        ↓
Crew Runner + Infrastructure (core/ — 11 modules)
  ├── crew_runner.py    → Orchestration with crew_factory, retry ×3
  ├── providers.py      → TTL backoff (5→10→20 min), provider chains
  ├── observability.py  → RunTrace/StepTrace, 5 formal metrics
  ├── governance.py     → CONSTITUTION: hard rules (block) + soft rules (warn)
  ├── supervisor.py     → Meta-supervisor: Q(0.4)+A(0.25)+C(0.2)+F(0.15), ACCEPT/RETRY/ESCALATE
  ├── checkpointing.py  → JSONL persistence per step
  ├── metrics.py        → JSONL Logger with rotation
  ├── memory_manager.py → ChromaDB + HuggingFace embeddings (all-MiniLM-L6-v2)
  ├── experiment.py     → Batch runner, statistical aggregation (Bessel)
  └── runtime_observer.py → Production metrics (SS, PFI, RP, GCR, SSR)
        ↓
8 Specialized Agents (config/agents.yaml + agents/*/SOUL.md)
        ↓
16 Tools (code, research, data, files, execution, blockchain)
4 MCP Servers (Filesystem, Web Search, Fetch, Knowledge Graph)
```

## Key Patterns

- **crew_factory**: Reconstructs the crew on each retry to bypass exhausted providers
- **Deterministic mode**: Fixed provider ordering + PRNGs with seed for reproducibility
- **Provider chains**: 5+ models per agent role with automatic fallback (see `llm_config.py`)
- **CONSTITUTION**: ~50 tokens, injected into each agent to save context
- **Internal observability**: No external dependencies (no OpenTelemetry) — everything custom JSONL

## Logs and outputs

- `logs/traces/` — RunTrace JSON (one per execution)
- `logs/experiments/` — runs.jsonl with aggregated metrics
- `logs/metrics/` — Agent steps, governance, supervisor
- `logs/checkpoints/` — JSONL per step for recovery
- `output/` — Crew results

## Adding a new metric

1. Define mathematically in `core/observability.py` → `compute_derived_metrics()`
2. Add field to the `RunTrace` dataclass
3. Update aggregation in `core/experiment.py` → `run_experiment()`
4. Document in `paper/PAPER_OBSERVABILITY_LAB.md` Section 5

## Adding a governance rule

1. Open `core/governance.py`
2. Add to `HARD_RULES` (blocks output) or `SOFT_RULES` (warning only)
3. Each rule is `(text: str) -> bool`, returns `True` if there is a violation
4. Run baseline experiment to verify impact on GCR

## LLM Providers — known restrictions

- Groq: 12K TPM, Llama 3.3 may fail with search_memory tool
- NVIDIA: 1000 credits, use `nvidia_nim/` prefix (not `openai/`), Qwen3-Coder-480B returns DEGRADED
- Cerebras: 1M tokens/day, Qwen3-235B and Qwen3-Coder-480B not available (404 free tier)
- Zhipu: GLM-4.7-Flash requires `extra_body={"enable_thinking": False}`
- SambaNova: limit 24K context tokens — backup only
o disponibles (404 free tier)
- Zhipu: GLM-4.7-Flash requiere `extra_body={"enable_thinking": False}`
- SambaNova: límite 24K tokens contexto — solo backup
