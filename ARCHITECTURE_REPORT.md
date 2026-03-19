# DOF Architecture Report — Post-Hardening v4.1
**Date:** 2026-03-19 | **Engineer:** Claude Code (Opus 4.6) | **Status:** ALL TESTS PASSED

---

## System Overview

| Metric | Value |
|--------|-------|
| Core Modules | 63 (.py files in core/) |
| API Endpoints | 13 (+ OpenAPI docs) |
| Autonomous Cycles | 216+ completed |
| Trace Files | 216 verified deterministic |
| Legion Agents | 14 specialized |
| Security Level System | 8 levels |
| Tests Passed | 12/12 security + full integration |
| Disk Usage | 1.6 GB |
| Memory DB | SQLite (287+ messages, 14 agent statuses) |

---

## Architecture Diagram

```
                    ┌─────────────────────────────┐
                    │   MISSION CONTROL DASHBOARD  │
                    │   (Next.js / Vercel)         │
                    │   6 Tabs: COMMS | SWARM |    │
                    │   TRACKS | TRACES | NEURAL | │
                    │   SHIELD                     │
                    └──────────┬──────────────────┘
                               │ HTTP (port 3000→8000)
                    ┌──────────▼──────────────────┐
                    │  ENIGMA SOVEREIGN API        │
                    │  (FastAPI / port 8000)        │
                    │  ┌─────────────────────────┐ │
                    │  │ SecurityHeadersMiddleware│ │
                    │  │ • Rate Limit 60/min/IP  │ │
                    │  │ • Security Headers (7)   │ │
                    │  │ • CORS Restricted        │ │
                    │  └─────────────────────────┘ │
                    │  ┌─────────────────────────┐ │
                    │  │ Input Sanitization       │ │
                    │  │ • XSS Detection          │ │
                    │  │ • SQL Injection          │ │
                    │  │ • Prompt Injection (EN+ES)│ │
                    │  │ • Length Limits (4KB)     │ │
                    │  └─────────────────────────┘ │
                    │  13 API Endpoints             │
                    └──────────┬──────────────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
    ┌─────────▼──────┐  ┌─────▼──────┐  ┌─────▼──────────┐
    │ OLLAMA LOCAL    │  │ SQLite     │  │ AUTONOMOUS     │
    │ enigma:latest   │  │ Memory DB  │  │ LOOP v2        │
    │ llama3:latest   │  │ 287+ msgs  │  │ 216+ cycles    │
    │ Port 11434      │  │ 14 agents  │  │ 30-min cadence │
    └────────────────┘  └────────────┘  └────────────────┘
```

---

## API Endpoints (13)

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/chat` | POST | Chat with Enigma (sanitized + PI detection) |
| `/api/chat/history` | GET | Last 20 messages from SQLite |
| `/api/chat/upload` | POST | File upload (13 extensions, 10MB max) |
| `/api/exec` | POST | Execute whitelisted commands only (7 safe) |
| `/api/swarm` | GET | 14 agents with real telemetry + security levels |
| `/api/issues` | GET | 4 hackathon track missions |
| `/api/graph` | GET | Neural topology (nodes + edges) |
| `/api/skills` | GET | Sovereign Skill Vault registry |
| `/api/social` | GET | Karma engine status |
| `/api/stats` | GET | Real hardware telemetry (psutil) |
| `/api/traces` | GET | Last 20 autonomous cycle traces |
| `/api/security` | GET | Full security posture dashboard |
| `/health` | GET | Health check |

---

## Security Hardening (NEW)

### Module: `core/security_middleware.py`

**1. Rate Limiting** — Sliding window, 60 req/min per IP
- In-memory, zero external dependencies
- Returns 429 with Retry-After header

**2. Input Sanitization** — 3-layer defense
- XSS: 9 patterns (script, iframe, eval, document.cookie, etc.)
- SQL Injection: 4 patterns (UNION SELECT, DROP, OR 1=1, etc.)
- Prompt Injection: 13 patterns (EN + ES)
  - "ignore previous instructions", "DAN mode", "jailbreak"
  - "ignora todas las instrucciones", "modo sin restricciones"

**3. Per-Agent Tool Allowlists** — 8-Level Security System
| Level | Agents | Allowed Tools |
|-------|--------|---------------|
| 8 | organizer-os | ALL (*) |
| 7 | architect-enigma, sentinel-shield | read, write, crypto, exec_safe |
| 5 | blockchain-wizard, defi-orbital, rwa-tokenizator | read, write, blockchain_tx |
| 4 | moltbook | read, write, network, social |
| 3 | ralph-code, qa-vigilante, qa-specialist | read, write, exec_safe, test |
| 2 | charlie-ux, product-overlord | read, write |
| 1 | scrum-master-zen, biz-dominator | read, analyze |

**4. Security Headers** (7 headers on every response)
- X-Content-Type-Options: nosniff
- X-Frame-Options: DENY
- X-XSS-Protection: 1; mode=block
- Referrer-Policy: strict-origin-when-cross-origin
- Permissions-Policy: camera=(), microphone=(), geolocation=()
- Content-Security-Policy: default-src 'self'
- X-DOF-Shield: ACTIVE

**5. CORS** — Restricted to `localhost:3000` + `dof-agent-web.vercel.app` only

**6. File Upload Security**
- 13 allowed extensions (.txt, .md, .json, .csv, .py, .js, .ts, .pdf, .png, .jpg, .jpeg, .gif, .webp)
- 10MB max size
- UUID-based filenames (no path traversal)

**7. Command Execution** — Strict whitelist (7 commands)
- `ollama list`, `python3 --version`, `cat .dof_cycle_state`
- `ls logs/traces/`, `wc -l logs/traces/*`, `uptime`, `df -h`
- No shell=True, no user input in commands

**8. Heartbeat Self-Healing**
- Checks Ollama (port 11434) and SQLite DB before expensive operations
- Returns alive/dead + latency_ms

**9. Audit Logging** — JSONL append-only
- Logs: THREAT_DETECTED, RATE_LIMIT_EXCEEDED, EXEC_BLOCKED, FILE_UPLOADED
- Each entry has SHA256 integrity hash

---

## Dashboard (6 Tabs)

| Tab | Description |
|-----|-------------|
| COMMS | Chat with Enigma #1686 (file upload, drag & drop) |
| SWARM | 14 agents with real telemetry, security levels, missions |
| TRACKS | 4 hackathon missions (Celo, ERC-8004, x402, Karma) |
| TRACES | Real autonomous cycle traces (216+ cycles, deterministic verification) |
| NEURAL | 3D topology graph of agent orchestration |
| SHIELD | Full security posture (heartbeats, headers, allowlists, audit log) |

Right sidebar: Real-time telemetry (CPU, RAM, Neural Sync), Ollama stats, hardware info, system status.

---

## Core Modules (63 files in core/)

### Governance & Verification
- `governance.py` — Constitution enforcer (4 hard rules, 5 soft rules, hierarchy enforcement)
- `ast_verifier.py` — Python AST verification on agent output
- `z3_verifier.py` / `z3_gate.py` / `z3_proof.py` — Formal verification (Z3 solver)
- `hierarchy_z3.py` — Instruction hierarchy proofs
- `state_model.py` / `transitions.py` — State machine verification

### Observability
- `observability.py` — RunTrace, StepTrace, 5 derived metrics
- `runtime_observer.py` — Production metrics (SS, PFI, RP, GCR, SSR)
- `metrics.py` — JSONL logger with rotation
- `event_stream.py` — Event streaming
- `otel_bridge.py` — OpenTelemetry bridge

### Security
- `security_middleware.py` — Rate limiting, sanitization, tool allowlists (NEW)
- `sovereign_security_module.py` — Crypto lab (secp256k1, fault injection, wallet audit)
- `system_sentinel.py` — System monitoring
- `entropy_detector.py` — Entropy analysis
- `loop_guard.py` — Loop protection

### Infrastructure
- `providers.py` — LLM provider management (TTL backoff, chains)
- `crew_runner.py` — Crew orchestration with retry
- `checkpointing.py` — JSONL persistence per step
- `local_memory.py` — Sovereign SQLite memory
- `memory_manager.py` — ChromaDB + HuggingFace embeddings
- `memory_governance.py` — Memory access governance
- `backup_manager.py` — Backup management
- `cloud_sync.py` — Cloud synchronization
- `hardware_optimizer.py` — M4 Max optimization

### Blockchain
- `avalanche_bridge.py` — Avalanche C-Chain integration
- `chain_adapter.py` — Multi-chain adapter
- `enigma_bridge.py` — Enigma bridge
- `merkle_tree.py` — Merkle tree proofs
- `proof_hash.py` / `proof_storage.py` — Proof hashing and storage
- `oracle_bridge.py` / `data_oracle.py` — Oracle integrations

### Agent Intelligence
- `agent_factory.py` — Agent creation
- `skill_engine.py` — Sovereign Skill Vault
- `identity.py` — Enigma #1686 system prompt
- `supervisor.py` — Meta-supervisor (Q+A+C+F scoring)
- `knowledge_aggregator.py` — Knowledge aggregation
- `llm_bridge.py` — LLM API bridge
- `bayesian_provider.py` — Bayesian provider selection
- `execution_dag.py` — Execution DAG
- `task_contract.py` — Task contracts

### Testing & Benchmarking
- `test_generator.py` — Benchmark runner
- `agentleak_benchmark.py` — Privacy leak testing
- `adversarial.py` — Adversarial testing
- `regression_tracker.py` — Regression tracking
- `trust_patterns.py` / `agentic_trust_patterns.py` — Trust pattern testing

---

## Provider Configuration

18 API keys in `.env`:
- **LLM**: Groq, Anthropic, OpenAI, Mistral, Cerebras, SambaNova, NVIDIA, OpenRouter
- **Local**: Ollama (enigma:latest, llama3:latest)
- **Blockchain**: (keys in .env for Avalanche wallets)
- **Social**: Moltbook, Telegram
- **ML**: HuggingFace
- **DevOps**: GitHub
- **Search**: Inforce

---

## Links

| Resource | URL |
|----------|-----|
| GitHub (DOF) | github.com/Cyberpaisa/deterministic-observability-framework |
| Hackathon | github.com/sodofi/synthesis-hackathon |
| ERC-8004 | eips.ethereum.org/EIPS/eip-8004 |
| Dashboard (Vercel) | dof-agent-web.vercel.app |
| Dashboard (Local) | localhost:3000 |
| API (Local) | localhost:8000 |
| Ollama | localhost:11434 |
| ERC-8004 Registry | 0x8004A169FB4a3325136EB29fA0ceB6D2e539a432 |
| Participant ID | df62a8883f25455b9a0edca1c99d3fb3 |

---

## Bugs Fixed (8)

1. Double except block in enigma_api.py → removed
2. Duplicate imports (psutil, subprocess, random) → cleaned
3. Fake metrics with random.randint → replaced with real psutil telemetry
4. Command injection (shell=True + inverted logic) → strict whitelist
5. Port inconsistency (8005 vs 8000) → unified to 8000
6. local_memory.db path confusion → verified at memory/chat_history.db
7. Zep external dependency (7 references) → all replaced with local_memory
8. Hardcoded fake TX → replaced with real SHA256 trace hash

## New Features Added

1. **Security Middleware** — Rate limiting, input sanitization, prompt injection detection
2. **8-Level Tool Allowlists** — Per-agent security clearance
3. **Security Headers** — 7 headers on every response
4. **Heartbeat Self-Healing** — Ollama + SQLite health checks
5. **Audit Logging** — JSONL with integrity hashes
6. **CORS Restriction** — No more wildcard origins
7. **File Upload Hardening** — Extension whitelist + size limits
8. **Dashboard: TRACES Tab** — Real autonomous cycle visualization
9. **Dashboard: SHIELD Tab** — Full security posture view
10. **Dashboard: Enhanced Stats** — CPU cores, available RAM, boot time

---

## Hardware (Apple M4 Max)

| Component | Spec |
|-----------|------|
| CPU | 14 cores (10 Performance + 4 Efficiency) |
| RAM | 36 GB Unified Memory |
| GPU | 32 cores |
| Storage | 386 GB free |
| Ollama Models | enigma:latest, llama3:latest |

---

*Generated by Claude Code (Opus 4.6) for DOF Agent #1686 persistent memory.*
