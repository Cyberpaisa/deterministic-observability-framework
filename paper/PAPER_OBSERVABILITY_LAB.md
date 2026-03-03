# Deterministic Observability and Resilience Engineering for Multi-Agent LLM Systems: An Experimental Framework

---

## Abstract

Multi-agent systems built on large language models (LLMs) exhibit failure modes that are distinct from single-model inference pipelines: provider rate limits, model incompatibilities, cascading retries, and non-deterministic output quality interact across execution steps. Existing orchestration frameworks—CrewAI, AutoGen, LangGraph—provide coordination abstractions but do not include instrumentation for measuring system stability under controlled perturbation. This paper presents an experimental framework for deterministic evaluation of multi-agent LLM systems operating across heterogeneous free-tier providers. The framework defines five metrics—Stability Score, Provider Fragility Index, Retry Pressure, Governance Compliance Rate, and Supervisor Strictness Ratio—each with explicit mathematical formulation, domain specification, and aggregation rules. The observability stack comprises run-level tracing with UUID-based session correlation, step-level checkpointing with JSONL persistence, two-tier governance enforcement, and a weighted meta-supervisor quality gate. A deterministic execution mode controls infrastructure-level randomness by fixing provider ordering and seeding pseudo-random number generators. Three experimental configurations validate the framework: a baseline with no injected failures (n=10, SS=1.0, σ=0.0), a reproducibility verification confirming metric identity across independent runs, and a perturbation experiment with periodic failure injection (n=10, SS=0.85, σ=0.2415). The implementation comprises 2,099 lines of Python across nine modules with no external dependencies beyond the orchestration layer. All results are from executed experiments with persisted trace artifacts.

---

## 1. Introduction

Multi-agent systems built on large language models are deployed in settings that rely on multiple LLM providers—each with distinct rate limits, model capabilities, pricing tiers, and failure characteristics. Frameworks such as CrewAI [1], AutoGen [2], and LangGraph [3] orchestrate specialized agents that collaborate sequentially or in parallel. When these systems operate across multiple providers (e.g., Groq, NVIDIA NIM, Cerebras, Zhipu AI) under free-tier constraints, the failure surface expands: a rate limit on one provider triggers a retry with a different provider, which may not support the same output format, which in turn triggers another retry, potentially exhausting all available providers within a single execution.

The problem addressed in this paper is not the existence of failures—any distributed system experiences them—but the absence of formal metrics to characterize failure patterns, measure system resilience, and reproduce experimental conditions. Without deterministic evaluation, observed metric differences cannot be attributed to specific variables: it is not possible to distinguish between a system that is inherently fragile and one that encountered a transient provider outage.

This paper makes the following contributions:

1. **Formal metric definitions** for quantifying multi-agent system behavior across five dimensions—stability, provider fragility, retry pressure, governance compliance, and supervisor strictness—with explicit mathematical formulations, domain specifications, and interpretive guidelines (Section 5).
2. **A deterministic execution mode** that isolates infrastructure-level randomness from LLM output variance by fixing provider ordering and seeding pseudo-random number generators, enabling controlled attribution of metric differences to specific experimental variables (Section 4.1).
3. **A failure injection protocol** that introduces controlled perturbations at configurable step indices with deterministic periodicity, enabling systematic measurement of metric sensitivity to known failure rates (Section 4.3).
4. **An integrated observability stack** comprising run-level tracing with UUID v4 session correlation, step-level checkpointing with JSONL persistence, constitutional governance enforcement, and meta-supervisor quality gating—implemented without external observability dependencies (Section 3).
5. **A batch experiment runner** with automatic statistical aggregation (sample mean and sample standard deviation with Bessel's correction) supporting 50+ consecutive runs per experiment configuration (Section 4.2).
6. **Empirical validation** through three experimental configurations demonstrating baseline characterization (n=10, SS=1.0, σ=0.0), reproducibility verification (5/5 metric identity across independent runs), and sensitivity to controlled perturbations (30% injection, SS=0.85, σ=0.2415) (Section 6).

The system under study consists of eight specialized agents organized into eleven crew configurations, operating across four free-tier LLM providers. All experimental results presented in this paper are from executed runs with persisted traces.

---

## 2. Related Work

### 2.1 Multi-Agent LLM Systems

The multi-agent paradigm for LLM applications emerged from the observation that specialized agents outperform monolithic prompts on complex tasks. CrewAI [1] introduced role-based agent definitions with sequential and hierarchical process models. AutoGen [2] from Microsoft Research proposed conversational agents with code execution capabilities. LangGraph [3] extended LangChain with stateful graph-based orchestration. MetaGPT [4] applied software engineering workflows to agent collaboration.

These frameworks focus on agent coordination semantics but provide limited infrastructure for failure characterization. CrewAI offers verbose logging but no structured metrics. AutoGen provides conversation histories but no step-level latency tracking. None implement deterministic execution modes for reproducible evaluation.

### 2.2 AI System Observability

Observability in machine learning systems has been studied primarily in the context of model serving. MLflow [5] tracks experiment parameters and metrics but operates at the training level, not the inference orchestration level. Weights & Biases [6] provides experiment tracking with statistical aggregation but targets model development workflows. OpenTelemetry [7] offers distributed tracing standards that could theoretically apply to agent systems, but no multi-agent framework has adopted its span model for agent-step correlation.

The gap addressed by this work is observability at the *orchestration* level: tracking not individual model calls but the interaction patterns, failure cascades, and quality gates that emerge when multiple agents collaborate through sequential task pipelines.

### 2.3 Resilience Engineering

Resilience engineering in distributed systems is well-established. The circuit breaker pattern [8] prevents cascading failures by temporarily disabling failing components. Exponential backoff with jitter [9] manages retry storms. Netflix's Chaos Monkey [10] pioneered failure injection for resilience validation.

Applying these patterns to LLM provider management is non-trivial. Unlike traditional microservices, LLM providers fail in model-specific ways: rate limits are per-model and per-token rather than per-request, certain models reject specific output formats, and authentication failures may affect only certain API prefixes. The provider resilience layer described in Section 3 adapts circuit breaker semantics to these LLM-specific failure modes.

### 2.4 Deterministic Evaluation of Stochastic Systems

Evaluating stochastic systems requires either controlling randomness or running sufficient trials to characterize distributions. Reinforcement learning evaluation protocols [11] address this through fixed seeds and episode counts. The challenge in multi-agent LLM systems is that randomness enters at multiple levels: the LLM sampling temperature, the provider selection order, the retry timing, and the output quality assessment. Our deterministic mode controls the infrastructure-level randomness (provider order, retry behavior) while acknowledging that LLM output randomness remains uncontrolled in the simulated experiments presented here.

---

## 3. System Architecture

### 3.1 Conceptual Overview

The system implements a layered architecture with clear separation between agent logic, infrastructure services, and experimental instrumentation.

```
┌─────────────────────────────────────────────────────┐
│                  Experiment Layer                    │
│   ExperimentDataset  │  BatchRunner  │  Schema       │
├─────────────────────────────────────────────────────┤
│                Observability Layer                   │
│  RunTrace  │  StepTrace  │  DerivedMetrics  │  Store │
├─────────────────────────────────────────────────────┤
│                 Crew Runner (Integration)            │
│  Orchestrates: Providers + Checkpoint + Governance   │
│                + Supervisor + Metrics + Traces        │
├──────────┬──────────┬───────────┬───────────────────┤
│ Provider │Checkpoint│Governance │  Meta-Supervisor   │
│ Manager  │ Manager  │ Enforcer  │  (Quality Gate)    │
│ TTL/Back │ JSONL    │ Hard/Soft │  Q+A+C+F Scoring   │
│ off/Rec. │ Steps    │ Rules     │  ACCEPT/RETRY/ESC  │
├──────────┴──────────┴───────────┴───────────────────┤
│               Metrics Logger (JSONL + Rotation)      │
├─────────────────────────────────────────────────────┤
│             Memory Manager (Short/Long/Episodic)     │
├─────────────────────────────────────────────────────┤
│                CrewAI + LiteLLM (Execution)          │
│          Groq │ NVIDIA NIM │ Cerebras │ Zhipu AI     │
└─────────────────────────────────────────────────────┘
```

### 3.2 Core Modules

The framework comprises nine Python modules totaling 2,099 lines of code, with no external dependencies beyond the orchestration layer (CrewAI) and its transitive dependency (LiteLLM).

**Provider Manager** (`providers.py`, 324 LOC). Implements per-provider state tracking with TTL-based exhaustion and exponential backoff recovery. Each provider maintains independent state: exhaustion flag, exhaust timestamp, failure count, and TTL. The backoff schedule follows `TTL = min(300 × 2^(failures-1), 1200)` seconds, producing a 5-minute, 10-minute, 20-minute progression capped at 20 minutes. Recovery is automatic: when `now - exhaust_time >= TTL`, the provider is reactivated. The manager also tracks per-provider capabilities (e.g., structured output support) and provides error classification into six categories: RATE_LIMIT, AUTH_FAILURE, MODEL_INCOMPATIBLE, TIMEOUT, PARSE_ERROR, and UNKNOWN.

**Checkpoint Manager** (`checkpointing.py`, 150 LOC). Provides step-level persistence using JSONL files keyed by run ID. Each step records: run_id, step_id, agent name, task name, provider, status (pending/running/completed/failed), input hash, output truncated to 5,000 characters, error message, timestamps, and latency. The manager supports loading previous runs from disk to enable retry of only failed steps.

**Constitution Enforcer** (`governance.py`, 182 LOC). Implements two-tier rule enforcement. Four hard rules produce blocking violations: no hallucination claims without URLs, language compliance (Spanish default), non-empty output (minimum 50 characters), and maximum output length (50,000 characters). Four soft rules produce warning scores with configurable weights: source URLs present (weight 0.3), structured output markers (0.2), no paragraph repetition (0.2), and actionable recommendations (0.3). The enforcer returns a composite governance result with pass/fail status and a normalized soft-rule score.

**Meta-Supervisor** (`supervisor.py`, 171 LOC). Evaluates final crew output on four weighted dimensions: Quality (0.40), Actionability (0.25), Completeness (0.20), and Factuality (0.15). Each dimension is scored 0–10 using heuristic indicators: Quality measures structural markers (headers, bullets, code blocks) and length; Actionability counts action verbs and numbered steps; Completeness checks output length and keyword overlap with input; Factuality counts URLs and hedging language. The composite score determines the decision: ACCEPT (≥8.0), RETRY (6.0–8.0, maximum 2 retries), or ESCALATE (<6.0).

**Metrics Logger** (`metrics.py`, 155 LOC). Singleton logger writing structured JSONL events with automatic rotation at 10 MB. Events include: crew_start, crew_end, agent_step, provider_exhausted, governance_check, and supervisor_eval. Each event carries timestamp, run_id, agent, provider, latency, status, and arbitrary metadata.

**Memory Manager** (`memory_manager.py`, 171 LOC). Provides three memory tiers without OpenAI dependencies: short-term (in-process with configurable TTL), long-term (JSONL-persisted with keyword search), and episodic (crew execution summaries). Short-term entries are automatically garbage-collected on access when TTL expires.

**Observability Module** (`observability.py`, 288 LOC). Defines the `RunTrace` and `StepTrace` data structures, session management via UUID v4, token estimation (approximately 4 characters per token for multilingual text), derived metric computation, and the `RunTraceStore` for persisting individual trace JSON files and appending run summaries to `runs.jsonl`. Implements deterministic mode toggling and fixed provider ordering.

**Experiment Module** (`experiment.py`, 393 LOC). Provides the formal experimental schema (`ExperimentRecord`), dataset management (`ExperimentDataset` with JSONL persistence and hypothesis-based filtering), a simulated crew for infrastructure validation, and the `run_experiment()` batch runner with configurable failure injection.

**Crew Runner** (`crew_runner.py`, 265 LOC). Integration layer that wraps `crew.kickoff()` with all infrastructure services. Each execution generates a `RunTrace`, passes through governance and supervisor gates, logs metrics, persists checkpoints, and returns a structured result dictionary including the trace file path.

### 3.3 Execution Pipeline

A single crew execution proceeds through the following stages:

1. **Initialization**: Generate UUID v4 run_id, record session_id, create RunTrace, log crew_start event.
2. **Provider Resolution**: Query ProviderManager for available providers, respecting TTL and capability filters.
3. **Checkpoint Start**: Record step as "running" with input hash and provider list.
4. **Execution**: Invoke `crew.kickoff()` through CrewAI, which internally manages agent-to-agent task passing.
5. **Checkpoint Complete/Fail**: Record step outcome with latency, output, or error.
6. **Governance Check**: Apply hard rules (blocking) and soft rules (scoring) to the output.
7. **Supervisor Evaluation**: Score output on Q/A/C/F dimensions, decide ACCEPT/RETRY/ESCALATE.
8. **Trace Finalization**: Compute derived metrics, persist trace JSON, append to runs.jsonl.
9. **Metrics Logging**: Log crew_end event with total latency and output length.

On failure at stage 4, the system detects the failing provider through error message pattern matching, marks it as exhausted (triggering TTL), and retries with remaining providers. Maximum three attempts per crew execution.

---

## 4. Experimental Framework

### 4.1 Deterministic Mode

Deterministic mode controls infrastructure-level randomness to enable reproducible experiments. When activated, the system:

- Seeds Python's random number generator with a fixed value (seed=42).
- Fixes the provider selection order to a canonical sequence: Cerebras, Groq, NVIDIA, Zhipu.
- Disables dynamic fallback reordering based on runtime conditions.
- Preserves LLM sampling randomness (temperature parameter) as uncontrolled.

In simulated experiments (using `SimulatedCrew`), deterministic mode produces identical metric outputs across independent runs. In live experiments with real LLM providers, deterministic mode controls the infrastructure variables while LLM output variation introduces measurable variance, enabling isolation of infrastructure effects from model effects.

### 4.2 Batch Runner

The `run_experiment()` function executes n consecutive runs with identical parameters, collecting per-run traces and computing aggregated statistics. The runner accepts:

- `n_runs`: Number of executions (tested up to 50).
- `prompt`: Fixed input text for all runs.
- `mode`: Execution mode label ("research" or "production").
- `hypothesis`: Free-text experimental hypothesis, persisted with results.
- `crew_factory`: Optional callable returning a crew object; defaults to `SimulatedCrew`.
- `deterministic`: Boolean flag for deterministic mode.
- `fail_step`: Step index at which to inject failure (-1 for no injection).

Each run generates: an individual trace JSON file, an entry in `runs.jsonl`, and an entry in `run_dataset.jsonl`. After all runs, the runner computes aggregated statistics including mean, sample standard deviation, status distribution, and supervisor strictness ratio.

### 4.3 Failure Injection Protocol

The `SimulatedCrew` accepts a `fail_step` parameter specifying which step index should raise a `RuntimeError` on the first execution attempt. The batch runner applies failure injection periodically: when `run_index % 3 == 1`, the specified step fails. This produces a known failure rate of approximately 30% (3 out of 10 runs), enabling controlled measurement of metric sensitivity to perturbation.

The failure injection simulates a realistic provider error: `"Simulated {provider} error: rate_limit_exceeded"`. This triggers the retry path, which creates a new `SimulatedCrew` without failure injection, simulating successful failover to an alternative provider.

### 4.4 Experiment Dataset Schema

All experiment records conform to a JSON Schema (`experiments/schema.json`) with the following structure:

```json
{
  "experiment_id": "uuid",
  "hypothesis": "string",
  "variables": {
    "crew_name": "string",
    "mode": "research | production",
    "deterministic": "boolean",
    "provider_order": ["string"],
    "input_prompt": "string",
    "max_retries": "integer"
  },
  "run_id": "uuid",
  "metrics": {
    "stability_score": "[0, 1]",
    "provider_fragility_index": "[0, ∞)",
    "retry_pressure": "[0, ∞)",
    "governance_compliance_rate": "[0, 1]",
    "supervisor_score": "number",
    "total_latency_ms": "number",
    "total_token_input": "integer",
    "total_token_output": "integer"
  },
  "raw_trace_path": "string",
  "timestamp": "ISO 8601",
  "status": "ok | error | escalated"
}
```

This schema enables post-hoc statistical analysis across experiments with different hypotheses and variable configurations.

---

## 5. Metrics Formalization

We define five metrics that characterize multi-agent system behavior. Each metric is computed per-run from the ordered list of steps S = {s₁, s₂, ..., sₙ} within a single RunTrace. Aggregation across runs uses sample mean and sample standard deviation.

### 5.1 Stability Score

The Stability Score measures the fraction of steps that completed successfully.

```
                    |{s ∈ S : status(s) = "failed"}|
SS(S) = 1  −  ─────────────────────────────────────
                              |S|
```

**Domain**: [0, 1]. **Interpretation**: SS = 1.0 indicates all steps completed without failure. SS = 0.5 indicates half the steps failed, regardless of whether retries eventually succeeded. The metric captures the *raw failure surface* before retry recovery.

### 5.2 Provider Fragility Index

The Provider Fragility Index measures how frequently the system had to switch providers during execution.

```
              |{s ∈ S : provider_switched(s) = true}|
PFI(S) = ───────────────────────────────────────────
                            |S|
```

**Domain**: [0, 1]. **Interpretation**: PFI = 0.0 indicates no provider switches occurred; all steps used the originally assigned provider. PFI = 1.0 indicates every step required a provider switch, suggesting high provider instability or poor initial assignment. Values above 0.5 indicate systemic provider issues.

### 5.3 Retry Pressure

Retry Pressure measures the cumulative retry burden normalized by step count.

```
              Σ retries(s) for s ∈ S
RP(S) = ────────────────────────────
                    |S|
```

**Domain**: [0, ∞). **Interpretation**: RP = 0.0 indicates no retries were needed. RP = 1.0 indicates an average of one retry per step. Unlike Stability Score, Retry Pressure can exceed 1.0 if individual steps require multiple retries. It measures the *total retry effort*, not just whether retries occurred.

### 5.4 Governance Compliance Rate

The Governance Compliance Rate measures the fraction of steps whose output passed constitutional governance checks.

```
              |{s ∈ S : governance_passed(s) = true}|
GCR(S) = ───────────────────────────────────────────
                            |S|
```

**Domain**: [0, 1]. **Interpretation**: GCR = 1.0 indicates all outputs passed governance checks. GCR < 1.0 indicates constitutional violations were detected. In the current implementation, governance violations on intermediate steps trigger retries; violations on the final step result in delivery with warnings. GCR measures output quality at the governance level, independent of supervisor scoring.

### 5.5 Supervisor Strictness Ratio

The Supervisor Strictness Ratio measures the fraction of completed runs that were escalated by the meta-supervisor, computed across a set of runs R rather than within a single run.

```
              |{r ∈ R : status(r) = "escalated"}|
SSR(R) = ────────────────────────────────────────
                          |R|
```

**Domain**: [0, 1]. **Interpretation**: SSR = 0.0 indicates the supervisor accepted all runs. SSR = 1.0 indicates all runs were escalated (quality below threshold). This metric characterizes the supervisor's effective filtering rate and can be used to calibrate the ACCEPT/RETRY/ESCALATE thresholds. High SSR suggests either consistently poor output quality or an overly strict supervisor configuration.

### 5.6 Aggregation

For a set of n runs, each producing metric vector mᵢ = (SSᵢ, PFIᵢ, RPᵢ, GCRᵢ), we compute:

```
              1   n
μ(m) =  ──  Σ  mᵢ
              n  i=1


                 ┌          1      n              ┐ ½
σ(m) =  │  ────── Σ  (mᵢ − μ(m))²  │
                 └  n − 1   i=1              ┘
```

We use sample standard deviation (Bessel's correction, n−1 denominator) as our runs represent samples from an underlying distribution of possible executions.

---

## 6. Experimental Results

All experiments were executed on the implemented framework using `SimulatedCrew` for controlled evaluation. Results are from actual logged outputs persisted in JSONL files.

### 6.1 Experiment 1: Baseline (No Failures)

**Configuration**: n=10 runs, deterministic=True, fail_step=-1 (no injection), mode="research".

**Prompt**: "Investigar mercado de agentes AI autónomos en Avalanche. Competidores, market size, tendencias 2025-2026, oportunidades de grants."

**Results**:

| Metric | Mean | Std Dev |
|--------|------|---------|
| Stability Score | 1.0000 | 0.0000 |
| Provider Fragility Index | 0.0000 | 0.0000 |
| Retry Pressure | 0.0000 | 0.0000 |
| Governance Compliance Rate | 1.0000 | 0.0000 |
| Supervisor Strictness Ratio | 0.0000 | — |
| Supervisor Score | 6.30 | 0.00 |

**Status distribution**: 10/10 OK, 0 errors, 0 escalated.

All metrics show zero variance, confirming that the simulated crew produces deterministic behavior when no failures are injected. The supervisor score of 6.30 reflects the heuristic scoring of the simulated output, which contains structured sections, action verbs, and URLs but is relatively short compared to a real crew output.

### 6.2 Experiment 2: Reproducibility Validation

**Configuration**: Identical to Experiment 1, executed as an independent run with fresh state (cleared runs.jsonl, traces, and dataset files).

**Comparison**:

| Metric | Experiment 1 | Experiment 2 | Match |
|--------|-------------|-------------|-------|
| Stability Score (μ±σ) | 1.0±0.0 | 1.0±0.0 | ✓ |
| Provider Fragility Index (μ±σ) | 0.0±0.0 | 0.0±0.0 | ✓ |
| Retry Pressure (μ±σ) | 0.0±0.0 | 0.0±0.0 | ✓ |
| Governance Compliance Rate (μ±σ) | 1.0±0.0 | 1.0±0.0 | ✓ |
| Supervisor Strictness Ratio | 0.0 | 0.0 | ✓ |

All five metrics are identical across independent executions. This confirms that deterministic mode, combined with the simulated crew, produces perfectly reproducible experimental results. The reproducibility holds despite different run_ids and timestamps, as expected—the metrics depend only on execution outcomes, not identifiers.

### 6.3 Experiment 3: Forced Failure Perturbation

**Configuration**: n=10 runs, deterministic=True, fail_step=1 (inject failure at step index 1 for every run where `run_index % 3 == 1`), mode="research".

This configuration injects failures in runs 2, 5, and 8 (0-indexed: 1, 4, 7), producing a 30% failure injection rate.

**Results**:

| Metric | Mean | Std Dev |
|--------|------|---------|
| Stability Score | 0.8500 | 0.2415 |
| Provider Fragility Index | 0.3000 | 0.4830 |
| Retry Pressure | 0.3000 | 0.4830 |
| Governance Compliance Rate | 1.0000 | 0.0000 |
| Supervisor Strictness Ratio | 0.0000 | — |
| Supervisor Score | 6.30 | 0.00 |

**Status distribution**: 10/10 OK (all eventually succeeded after retry), 0 errors, 0 escalated.

**Per-run breakdown**:

| Run | Stability | Fragility | Retry | Status | Failure Injected |
|-----|-----------|-----------|-------|--------|-----------------|
| 1 | 1.00 | 0.00 | 0.00 | ok | No |
| 2 | 0.50 | 1.00 | 1.00 | ok | Yes |
| 3 | 1.00 | 0.00 | 0.00 | ok | No |
| 4 | 1.00 | 0.00 | 0.00 | ok | No |
| 5 | 0.50 | 1.00 | 1.00 | ok | Yes |
| 6 | 1.00 | 0.00 | 0.00 | ok | No |
| 7 | 1.00 | 0.00 | 0.00 | ok | No |
| 8 | 0.50 | 1.00 | 1.00 | ok | Yes |
| 9 | 1.00 | 0.00 | 0.00 | ok | No |
| 10 | 1.00 | 0.00 | 0.00 | ok | No |

### 6.4 Interpretation of Variance

The perturbation experiment reveals several characteristics of the metric system:

**Bimodal distribution**: Stability Score takes only two values: 1.0 (no failure) and 0.5 (one failure in two steps). This bimodality is an artifact of the fixed step count per run. In production systems with more steps per crew (typically 4–7 agents), the granularity would be finer.

**Correlated metrics**: Provider Fragility Index and Retry Pressure are perfectly correlated (ρ = 1.0) in this experiment because every failure triggers exactly one retry with exactly one provider switch. In production, these metrics would decouple: a provider switch might occur without a retry (pre-emptive routing), or multiple retries might use the same provider (transient errors).

**Governance invariance**: Governance Compliance Rate remains 1.0 even under failure injection. This is expected: governance checks apply to *output content*, not execution path. The retry mechanism successfully produces compliant output even after initial failures, demonstrating that the governance layer is robust to infrastructure perturbations.

**Supervisor stability**: Supervisor Score remains 6.30 across all runs regardless of failures. This is because the simulated crew produces identical output text on successful execution, and the supervisor evaluates output content independently of the execution path. This separation of concerns is intentional: the supervisor measures *output quality*, while Stability Score and Retry Pressure measure *execution health*.

**Variance magnitude**: The standard deviation of 0.2415 for Stability Score under 30% failure injection provides a baseline for comparison with real provider experiments. If a real provider experiment shows σ > 0.2415 with the same injection rate, the additional variance is attributable to real-world factors beyond the controlled failure.

---

## 7. Parametric Failure Sensitivity Analysis

Section 6.3 tested a single failure injection rate (30%). This section extends the analysis by varying the injection rate from 0% to 70%, producing parametric curves for each metric. Six configurations were executed with n=20 runs each (120 total runs), all in deterministic mode.

### 7.1 Experimental Configuration

The `run_parametric_sweep()` function executes `run_experiment()` at each specified failure rate. The `failure_rate` parameter (0.0–1.0) replaces the legacy modular injection pattern with deterministic index-based selection: the first ⌊n × rate⌋ runs receive failure injection, the remaining runs execute without injection. This produces exact failure counts rather than approximate rates.

**Failure rates tested**: 0%, 10%, 20%, 30%, 50%, 70%.
**Runs per rate**: n=20.
**Total runs**: 120.
**Deterministic mode**: enabled (seed=42, fixed provider order).
**Fail step**: index 1.

### 7.2 Results

| Failure Rate | SS (μ) | SS (σ) | PFI (μ) | PFI (σ) | RP (μ) | RP (σ) | GCR (μ) | SSR |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0% | 1.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.0000 | 0.0000 |
| 10% | 0.9500 | 0.1539 | 0.1000 | 0.3078 | 0.1000 | 0.3078 | 1.0000 | 0.0000 |
| 20% | 0.9000 | 0.2052 | 0.2000 | 0.4104 | 0.2000 | 0.4104 | 1.0000 | 0.0000 |
| 30% | 0.8500 | 0.2351 | 0.3000 | 0.4702 | 0.3000 | 0.4702 | 1.0000 | 0.0000 |
| 50% | 0.7500 | 0.2565 | 0.5000 | 0.5130 | 0.5000 | 0.5130 | 1.0000 | 0.0000 |
| 70% | 0.6500 | 0.2351 | 0.7000 | 0.4702 | 0.7000 | 0.4702 | 1.0000 | 0.0000 |

All 120 runs completed with status "ok" (all failures recovered through retry). Governance Compliance Rate remained invariant at 1.0 across all injection rates. The CSV export is available at `experiments/parametric_sweep.csv`.

### 7.3 Curve Shape Analysis

**Stability Score**: The relationship between failure rate (f) and mean Stability Score follows the linear function SS(f) = 1 − f/2. This arises from the step-level computation: each failed run produces SS=0.5 (1 failed step + 1 successful retry = 2 steps, 1 failure), while each clean run produces SS=1.0. With n·f failed runs and n·(1−f) clean runs:

```
μ(SS) = [n·f · 0.5 + n·(1−f) · 1.0] / n = 1 − f/2
```

The factor of 1/2 reflects the fixed two-step structure of failed runs (initial failure + successful retry). In systems with more steps per run, the coefficient would decrease: for k steps per failed run, SS(f) = 1 − f/(k+1). This linear relationship means that Stability Score degrades proportionally to failure rate, with a slope determined by the step count of the recovery path.

**Provider Fragility Index and Retry Pressure**: Both metrics follow μ(PFI) = μ(RP) = f. This identity holds because each failure triggers exactly one provider switch and exactly one retry. In production systems with partial failures, multiple retries per step, or pre-emptive provider switching, PFI and RP would decouple.

**Standard deviation**: The standard deviation of the Stability Score follows the Bernoulli distribution formula σ = √[f·(1−f)] × |SS_fail − SS_clean| / √(n−1). The maximum variance occurs at f=0.5 (σ=0.2565), consistent with the well-known property that Bernoulli variance peaks at p=0.5. The symmetric decline at f=0.3 and f=0.7 (both σ=0.2351) confirms this behavior.

### 7.4 System Resilience Threshold

The parametric sweep reveals that the system under test exhibits **full recovery at all tested failure rates** (0%–70%): every run eventually produces acceptable output through retry. No runs resulted in permanent failure or escalation. This indicates that the retry mechanism, combined with the SimulatedCrew's guaranteed success on second attempt, provides a resilience floor.

The resilience threshold—the failure rate at which the system transitions from recovery to degradation—is not reached in these experiments because the simulated retry always succeeds. In production, the threshold would depend on: (a) the probability that the fallback provider also fails, (b) the maximum retry count (currently 3), and (c) whether consecutive failures exhaust all providers within the TTL window.

For operational monitoring, the results suggest threshold settings based on the parametric curve:

- **Alert at SS < 0.90**: triggers at failure_rate ≥ 20%.
- **Alert at SS < 0.80**: triggers at failure_rate ≥ 40%.
- **Alert at SS < 0.70**: triggers at failure_rate ≥ 60%.

These thresholds are specific to the two-step recovery structure. Systems with more agents per crew (and thus more steps per run) would exhibit higher Stability Scores for the same failure rate, requiring adjusted thresholds.

### 7.5 Governance Invariance

The invariance of GCR=1.0 across all failure rates (0%–70%) is a structural result: governance checks evaluate output content, not execution path. Since the retry mechanism always produces compliant output in the simulated environment, governance remains decoupled from infrastructure failures at every tested injection rate. This confirms and extends the single-rate observation from Section 6.4 to the full parametric range.

---

## 8. Discussion

### 8.1 Deterministic Reproducibility

The reproducibility experiment (Section 6.2) demonstrates perfect metric identity across independent runs, confirming that the deterministic mode successfully eliminates infrastructure-level randomness. This result is theoretically expected for simulated experiments but has practical implications for real provider testing.

In practice, deterministic mode cannot control LLM output randomness (temperature-dependent sampling). However, by fixing the infrastructure variables—provider ordering, retry behavior, random seeds—deterministic mode enables attribution: if two runs differ in metrics, the difference is attributable to LLM output variation rather than infrastructure nondeterminism. This isolation is essential for studying questions such as "Does provider X produce more governance violations than provider Y?" where infrastructure variation would confound the comparison.

A limitation of the current deterministic mode is that it operates at the Python process level. Concurrent executions in separate threads or processes maintain independent random states, which could introduce nondeterminism in multi-threaded deployments. Future work should address this through thread-local seed management.

### 8.2 Sensitivity to Perturbations

The perturbation experiment (Section 6.3) shows that a 30% failure injection rate reduces mean Stability from 1.0 to 0.85, a 15% degradation. The relationship is not 30% because Stability is computed per-step within each run: a run with 2 steps where 1 fails has Stability 0.5, not 0.0. The mean across 7 clean runs (Stability=1.0) and 3 perturbed runs (Stability=0.5) is (7×1.0 + 3×0.5)/10 = 0.85.

This non-linear relationship between injection rate and Stability Score has implications for threshold setting. A team setting an alert threshold at Stability < 0.90 would trigger on a 30% injection rate but not on a 20% rate (expected Stability = 0.90). The threshold sensitivity depends on step count per run: more steps per run produce higher Stability values for the same injection rate, because a single failure represents a smaller fraction of total steps.

Provider Fragility Index and Retry Pressure show high standard deviation (0.4830) relative to their mean (0.3000), reflecting the bimodal nature of the underlying data. The coefficient of variation (CV = σ/μ = 1.61) indicates high relative dispersion. In production monitoring, this suggests that run-level metrics should be aggregated over time windows rather than evaluated individually.

### 8.3 Governance Robustness

The invariance of Governance Compliance Rate under perturbation (GCR = 1.0 in all experiments) demonstrates that the governance layer is decoupled from execution infrastructure. This is a desirable property: output quality standards should not degrade because of provider switching or retries.

However, this result also reflects a limitation of the current experiment: the simulated crew always produces the same output text, which consistently passes governance checks. In real provider experiments, different LLMs may produce outputs with different governance profiles. For instance, a model with weaker instruction-following capabilities might produce outputs without URLs (violating the NO_HALLUCINATION_CLAIM rule) or in English rather than Spanish (violating LANGUAGE_COMPLIANCE). Future work should characterize governance compliance rates across different providers.

The constitutional enforcement model—hard rules that block and soft rules that score—provides a useful separation of concerns. Hard rules prevent clearly unacceptable outputs (empty responses, excessive length) regardless of supervisor evaluation. Soft rules contribute to the governance score, which feeds into the meta-supervisor's overall quality assessment. This layered approach prevents the system from delivering outputs that violate absolute constraints while allowing flexibility on stylistic dimensions.

### 8.4 Meta-Supervisor Calibration

The supervisor score of 6.30 across all experiments falls in the RETRY zone (6.0–8.0). In the batch runner, this triggers a RETRY decision, but since the simulated crew produces identical output on retry, the supervisor accepts on the second attempt (when `retry_count >= MAX_RETRIES`). In production, a RETRY would re-execute the crew with potentially different providers, producing different output that might score higher.

The supervisor's heuristic scoring (counting headers, bullets, URLs, action words) provides a computationally inexpensive quality signal but has known limitations. Short but highly relevant outputs may score below 8.0 due to insufficient structural markers. Long but vacuous outputs may score above 8.0 due to abundant headers and bullets. Future work should investigate calibrating the supervisor against human quality judgments to establish the correlation between heuristic scores and perceived quality.

The Supervisor Strictness Ratio of 0.0 across all experiments indicates that no runs were escalated, even under failure injection. This is because the retry mechanism successfully produces acceptable output in all cases. The SSR metric becomes informative when system degradation is severe enough that retries fail to produce acceptable output—a scenario that would require higher failure injection rates or governance rules that reject the simulated output.

### 8.5 Limitations

Several limitations should be acknowledged:

1. **Simulated execution**: All experiments use `SimulatedCrew` rather than real LLM providers. While this enables controlled evaluation of the observability infrastructure, it does not capture real-world failure patterns such as variable latency, partial responses, or model-specific output characteristics.

2. **Token estimation**: Token counts are estimated at 4 characters per token, which is approximate. Real tokenization varies by model and language. For Spanish text, the actual ratio may be closer to 3.5 characters per token.

3. **Fixed step count**: The simulated crew always produces a fixed number of steps (1 clean or 2 with retry), whereas real crews have 4–7 agents producing multiple steps. The metric sensitivity analysis would differ with higher step counts.

4. **Heuristic supervisor**: The meta-supervisor uses heuristic scoring rather than LLM-based evaluation. While computationally efficient, it may not capture semantic quality dimensions that a language model could assess.

5. **Single-thread experiments**: All experiments run in a single thread. Production deployments may execute multiple crews concurrently, introducing contention for provider capacity and potential interference between runs.

6. **No real latency**: Simulated execution completes in microseconds. Real crew executions take 30–300 seconds, and latency variance across providers is a significant operational concern not captured here.

---

## 9. Threats to Validity

### 9.1 Internal Validity

Internal validity concerns whether the observed metric values are attributable to the experimental variables rather than confounding factors. Three potential confounds are identified.

**Shared process state.** The batch runner executes all runs within a single Python process. Module-level state—particularly the `DETERMINISTIC_MODE` global variable and the `_SESSION_ID` singleton—persists across runs. While deterministic mode is explicitly designed to maintain consistent state, unintended accumulation of state (e.g., in the `ProviderManager` singleton or `MetricsLogger` file handles) could introduce ordering effects where early runs influence later runs. Mitigation: the simulated experiments do not instantiate singleton infrastructure components that maintain cross-run state. The `RunTraceStore` appends to `runs.jsonl` but does not read from it during execution; aggregation occurs only after all runs complete.

**Deterministic failure injection pattern.** The failure injection uses a fixed modular pattern (`run_index % 3 == 1`), producing failures at indices 1, 4, 7 in a 10-run experiment. This pattern is deterministic and non-random, meaning the failure distribution is not uniformly sampled from possible failure configurations. Different failure patterns (e.g., consecutive failures, failures concentrated at the beginning or end) could produce different metric distributions even at the same injection rate. The reported variance values are specific to the modular injection pattern and should not be generalized to arbitrary failure distributions.

**Token estimation approximation.** Token counts are estimated using a fixed ratio of 4 characters per token. This approximation affects the `total_token_input` and `total_token_output` fields in each trace. While token counts do not influence any of the five primary metrics (SS, PFI, RP, GCR, SSR), they do appear in the experiment dataset and could mislead analyses that rely on token counts for cost estimation. The approximation error is bounded: for English text, the actual ratio is approximately 4.0 characters per token (GPT-class tokenizers); for Spanish text, approximately 3.5; for mixed multilingual text, approximately 3.5–4.5.

### 9.2 External Validity

External validity concerns the generalizability of findings beyond the experimental conditions.

**Simulated vs. real execution.** All experiments use `SimulatedCrew`, which produces deterministic output text in constant time. Real LLM providers introduce: (a) variable latency (100ms–30s per call), (b) non-deterministic output content (temperature-dependent sampling), (c) model-specific failure modes (context length exceeded, content filter triggered, malformed JSON response), and (d) time-dependent availability (rate limits that depend on concurrent usage by other users). The metric values reported here characterize the observability infrastructure under controlled conditions; they do not represent expected values for production deployments.

**Provider heterogeneity.** The framework is validated against four specific providers (Groq, NVIDIA NIM, Cerebras, Zhipu AI) with free-tier constraints. Provider APIs, rate limit policies, and error response formats vary across providers and change over time. The error classification heuristics (pattern matching on error messages) may not generalize to providers with different error reporting conventions. The provider resilience mechanisms (TTL-based exhaustion, exponential backoff) assume that provider unavailability is temporary and self-resolving, which may not hold for authentication failures or account suspensions.

**Scale limitations.** The maximum experiment size tested is n=50 runs. Statistical properties of the metrics under larger sample sizes (n>1000) have not been evaluated. For metrics with bimodal distributions (e.g., Stability Score under failure injection), larger samples would provide better distribution characterization but would not change the fundamental bimodality arising from the fixed step count per run.

### 9.3 Construct Validity

Construct validity concerns whether the metrics measure the intended constructs.

**Stability Score and recovery.** Stability Score counts failed steps regardless of whether the system recovered through retry. A run with one failed step and one successful retry has SS=0.5, identical to a run with one failed step and no retry. This design choice treats failures as infrastructure events that should be measured even when masked by recovery. An alternative construct—*effective stability*—would measure only unrecovered failures, but this conflates infrastructure quality with retry policy effectiveness.

**Governance Compliance as quality proxy.** Governance Compliance Rate measures conformance to rule-based constraints (language, length, structure), not semantic quality. An output that is linguistically correct, properly structured, and factually wrong would receive GCR=1.0. The governance layer is designed to enforce *format and policy* compliance, not *content* correctness; content quality is the supervisor's responsibility. Users of the framework should interpret GCR as a compliance metric, not a quality metric.

**Supervisor Score limitations.** The meta-supervisor uses heuristic indicators (header count, bullet count, URL count, action verb count) as proxies for Quality, Actionability, Completeness, and Factuality. These proxies have not been validated against human quality judgments. Long, well-formatted outputs with minimal substantive content could score above 8.0 (false positive), while short, precise outputs could score below 6.0 (false negative). The supervisor is designed as a coarse quality gate, not a fine-grained evaluator.

### 9.4 Statistical Conclusion Validity

Statistical conclusion validity concerns the appropriateness of statistical methods and sample sizes.

**Sample size.** The primary experiments use n=10 runs. For metrics with non-zero variance (e.g., SS under perturbation, σ=0.2415), the 95% confidence interval for the mean is μ ± t₉,₀.₀₂₅ × σ/√n = 0.85 ± 2.262 × 0.2415/√10 = 0.85 ± 0.173, yielding the interval [0.677, 1.023]. This wide interval reflects the limited sample size and high variance. A sample of n=50 would reduce the interval width to ±0.077, providing substantially greater precision. The reproducibility experiment (Section 6.2) confirms zero-variance results for the deterministic baseline, where any sample size is sufficient.

**Distribution assumptions.** Sample standard deviation assumes an underlying distribution from which runs are independent samples. In simulated experiments, runs are deterministic given the same parameters, so the "distribution" is degenerate (point mass). The non-zero variance in Experiment 3 arises from the deterministic failure injection pattern, not from sampling. Strictly, the standard deviation in this case measures the dispersion of the metric values across the fixed set of runs, not the uncertainty of an estimated population parameter. We report sample standard deviation for consistency with the aggregation framework and because the same formulas apply correctly to real-provider experiments where genuine stochastic variation exists.

**Multiple comparisons.** The three experiments are analyzed independently; no corrections for multiple comparisons are applied. This is appropriate because the experiments test distinct hypotheses (baseline, reproducibility, perturbation sensitivity) rather than testing multiple variants against a common null hypothesis.

---

## 10. Replication Protocol

This section provides the exact procedure for reproducing all experimental results reported in this paper.

### 10.1 Preconditions

- Python 3.11 or higher.
- The framework codebase with all nine core modules (`core/providers.py`, `core/checkpointing.py`, `core/memory_manager.py`, `core/metrics.py`, `core/governance.py`, `core/supervisor.py`, `core/observability.py`, `core/experiment.py`, `core/crew_runner.py`) and the package initializer (`core/__init__.py`).
- No external API keys are required for simulated experiments. The `SimulatedCrew` operates entirely in-process.
- No GPU or specialized hardware requirements. All experiments complete in under 5 seconds on commodity hardware.

### 10.2 Environment Configuration

```bash
# Verify Python version
python3 --version  # Must be >= 3.11

# Navigate to project root
cd /path/to/equipo-de-agentes

# Ensure core/ directory contains all 9 modules
ls core/*.py
# Expected: __init__.py checkpointing.py crew_runner.py experiment.py
#           governance.py memory_manager.py metrics.py observability.py
#           providers.py supervisor.py

# Create required directories
mkdir -p logs/experiments logs/traces experiments
```

### 10.3 Deterministic Mode Activation

Deterministic mode is activated programmatically via the `deterministic=True` parameter in `run_experiment()`. It can also be activated globally via environment variable:

```bash
export DETERMINISTIC_MODE=1
```

When activated, the framework: (1) seeds `random.seed(42)`, (2) fixes provider order to `["cerebras", "groq", "nvidia", "zhipu"]`, and (3) disables dynamic fallback reordering. These effects are process-scoped and persist until `set_deterministic(False)` is called or the process exits.

### 10.4 Exact Experimental Commands

**Experiment 1 — Baseline (No Failures):**

```python
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(".")))
from core.experiment import run_experiment

# Clear previous state
import glob
for f in glob.glob("logs/traces/*.json"):
    os.remove(f)
for f in ["logs/experiments/runs.jsonl", "experiments/run_dataset.jsonl"]:
    if os.path.exists(f):
        os.remove(f)

results = run_experiment(
    n_runs=10,
    prompt="Investigar mercado de agentes AI autónomos en Avalanche. "
           "Competidores, market size, tendencias 2025-2026, "
           "oportunidades de grants.",
    mode="research",
    hypothesis="Baseline: zero-failure simulated crew produces "
               "perfect stability metrics with zero variance",
    deterministic=True,
    fail_step=-1,
    verbose=True,
)
print(results["aggregated"])
```

**Experiment 2 — Reproducibility Verification:**

Execute the identical command block from Experiment 1 after clearing state. Compare `results["aggregated"]` dictionaries. All five primary metrics (SS, PFI, RP, GCR, SSR) must be identical across executions.

**Experiment 3 — Forced Failure Perturbation:**

```python
results_perturbed = run_experiment(
    n_runs=10,
    prompt="Investigar mercado de agentes AI autónomos en Avalanche. "
           "Competidores, market size, tendencias 2025-2026, "
           "oportunidades de grants.",
    mode="research",
    hypothesis="Perturbation: 30% failure injection reduces stability "
               "while governance remains invariant",
    deterministic=True,
    fail_step=1,
    verbose=True,
)
print(results_perturbed["aggregated"])
```

**Experiment 4 — Parametric Failure Sweep:**

```python
from core.experiment import run_parametric_sweep

sweep = run_parametric_sweep(
    failure_rates=[0.0, 0.10, 0.20, 0.30, 0.50, 0.70],
    n_runs=20,
    prompt="Investigar mercado de agentes AI autónomos en Avalanche. "
           "Competidores, market size, tendencias 2025-2026, "
           "oportunidades de grants.",
    mode="research",
    deterministic=True,
    fail_step=1,
    verbose=True,
)
# CSV exported to experiments/parametric_sweep.csv
```

### 10.5 Expected Artifacts

After executing all four experiments, the following artifacts should exist:

| Artifact | Path | Format | Count |
|----------|------|--------|-------|
| Individual trace files | `logs/traces/{run_id}.json` | JSON | 150 (30 from Exp 1-3 + 120 from Exp 4) |
| Run summaries | `logs/experiments/runs.jsonl` | JSONL | 150 entries |
| Experiment dataset | `experiments/run_dataset.jsonl` | JSONL | 150 entries |
| Experiment schema | `experiments/schema.json` | JSON | 1 |
| Parametric sweep CSV | `experiments/parametric_sweep.csv` | CSV | 1 (6 rows) |

Each trace file contains the complete `RunTrace` with all `StepTrace` entries, derived metrics, and session metadata. The `runs.jsonl` file contains flattened summaries suitable for statistical analysis. The `run_dataset.jsonl` file contains `ExperimentRecord` entries with hypothesis labels and variable configurations. The `parametric_sweep.csv` file contains aggregated metrics per failure rate, suitable for plotting.

### 10.6 Validation Criteria

Replication is successful if the following conditions hold:

1. **Experiment 1**: All five primary metrics have mean equal to their boundary values (SS=1.0, PFI=0.0, RP=0.0, GCR=1.0, SSR=0.0) with standard deviation exactly 0.0.
2. **Experiment 2**: All five primary metrics are numerically identical to Experiment 1 results (bitwise equality of floating-point values, not approximate equality).
3. **Experiment 3**: SS mean = 0.85, SS σ = 0.2415 (to 4 decimal places). PFI mean = 0.30, PFI σ = 0.4830. RP mean = 0.30, RP σ = 0.4830. GCR mean = 1.0, GCR σ = 0.0. SSR = 0.0.
4. **Status distribution (Experiment 3)**: 10/10 runs report status "ok" (all failures recovered through retry).
5. **Experiment 4**: SS follows SS(f) = 1 − f/2 for all tested rates. GCR = 1.0 at all rates. PFI = RP = f at all rates. CSV contains 6 rows with 11 columns.
5. **Trace integrity**: Each trace JSON file is valid JSON containing fields `run_id`, `session_id`, `steps` (array), and all derived metric fields.

---

## 11. Comparative Positioning

This section positions the framework relative to existing multi-agent orchestration platforms across five dimensions relevant to experimental evaluation.

### 11.1 Comparison Framework

We evaluate five systems: CrewAI [1] (the orchestration layer used by this framework), AutoGen [2], LangGraph [3], MetaGPT [4], and the framework presented in this paper. The comparison is based on documented capabilities as of early 2026; capabilities may have changed in subsequent releases.

### 11.2 Comparative Table

| Dimension | CrewAI | AutoGen | LangGraph | MetaGPT | This Framework |
|-----------|--------|---------|-----------|---------|----------------|
| **Deterministic execution** | No. Provider selection follows LiteLLM defaults. No seed control for infrastructure randomness. | No. Conversation routing depends on agent responses, which are inherently non-deterministic. | Partial. Graph structure is deterministic, but node execution (LLM calls) is not controlled. | No. Software engineering workflow follows fixed phases but LLM calls introduce variance. | Yes. Fixed provider ordering, seeded PRNG, deterministic failure injection pattern. Infrastructure randomness is eliminated; LLM randomness is isolated. |
| **Failure injection** | Not supported. Failures are observed passively when they occur in production. | Not supported. Error handling exists but cannot be triggered programmatically for testing. | Not supported. State machine can represent error states but does not inject them. | Not supported. Pipeline assumes successful execution at each stage. | Supported. Configurable `fail_step` parameter with periodic injection (`run_index % 3 == 1`). Simulates provider-specific error messages. |
| **Formal stability metrics** | None. Provides verbose logs and callback hooks but no derived metrics. `output_log.txt` captures raw output. | None. Conversation history can be analyzed post-hoc but no built-in metrics. | None. State transitions are logged but not aggregated into stability metrics. | None. Code review and testing stages provide pass/fail but no continuous metrics. | Five metrics with formal definitions: SS, PFI, RP, GCR, SSR. Each with specified domain, interpretation, and aggregation rules. |
| **Batch statistical aggregation** | Not built-in. Requires external scripting to run multiple executions and compute statistics. | Not built-in. Individual runs produce conversation logs; aggregation requires custom code. | Not built-in. Graph execution is single-run; batch execution requires external orchestration. | Not built-in. Pipeline executes once per input; no native batch mode. | Built-in. `run_experiment(n_runs=N)` with automatic mean, sample standard deviation, status distribution, and strictness ratio computation. |
| **Governance enforcement** | Not built-in. Output validation is the user's responsibility. Guardrails can be added via custom tools. | Partial. Code execution sandboxing provides safety constraints, but no content governance rules. | Not built-in. Conditional edges can implement validation but no rule-based governance framework. | Partial. Code review agent provides quality checks within the software engineering workflow. | Built-in. Two-tier enforcement: 4 hard rules (blocking) + 4 soft rules (scoring). Constitutional model with configurable rule sets. |

### 11.3 Positioning Analysis

The comparison reveals that existing multi-agent frameworks prioritize *coordination semantics*—how agents interact, delegate, and compose outputs—over *experimental infrastructure*—how system behavior is measured, reproduced, and characterized. This is a natural consequence of their origin as application development tools rather than experimental platforms.

The framework presented in this paper occupies a complementary position: it does not replace CrewAI's coordination capabilities (it uses CrewAI as its orchestration layer) but adds the experimental infrastructure necessary for systematic evaluation. This layered approach means the framework's contributions are orthogonal to and composable with any of the compared systems. The deterministic mode, failure injection, formal metrics, batch runner, and governance enforcement could, in principle, be adapted to wrap AutoGen conversations, LangGraph state machines, or MetaGPT pipelines.

The absence of these capabilities in existing frameworks is not necessarily a design flaw; it reflects different design priorities. Production-focused frameworks optimize for usability and flexibility. The experimental framework presented here optimizes for measurability and reproducibility. Both priorities are legitimate; the contribution is in providing the experimental capabilities that the existing ecosystem lacks.

---

## 12. Future Work

### 12.1 Parametric Failure Curves

The current work tests a single failure injection rate (30%). A systematic study would vary the injection rate from 0% to 100% in increments of 10%, producing parametric curves for each metric. The expected result is a monotonically decreasing Stability Score and monotonically increasing Retry Pressure, but the functional forms (linear, convex, concave) are unknown and likely depend on the retry mechanism's interaction with the failure pattern.

Of particular interest is the *critical failure rate*—the injection rate at which the system transitions from recovery (all runs eventually succeed) to degradation (some runs fail permanently). This threshold would inform capacity planning for multi-provider deployments.

### 12.2 Real Provider Benchmarking

Executing the experiment framework against real LLM providers would produce the first empirical characterization of multi-provider system behavior. Key questions include:

- What is the natural Stability Score for each provider under free-tier constraints?
- How does Provider Fragility Index vary across time of day and day of week?
- Do certain provider combinations produce lower Retry Pressure than others?
- How does Governance Compliance Rate vary across models (e.g., Llama 3.3 vs. GPT-OSS-120B vs. GLM-4.7)?

This benchmarking requires modifications to handle real latency (30–300 seconds per run), real token consumption against free-tier limits, and extended execution windows (hours to days for statistically significant sample sizes).

### 12.3 Cross-Model Entropy Analysis

Different LLM models produce outputs with different levels of variability for the same prompt. Measuring the entropy of supervisor scores across runs for a fixed prompt and fixed model would characterize each model's output consistency. Low-entropy models (consistent supervisor scores) are preferable for production deployments where predictable quality is valued over occasional high-quality outliers.

This analysis would extend the current per-run metrics to per-model metrics, enabling model selection decisions informed by quality distribution rather than single-sample evaluation.

### 12.4 Adaptive Supervisor Thresholds

The current supervisor uses fixed thresholds (ACCEPT ≥ 8.0, RETRY 6.0–8.0, ESCALATE < 6.0). These thresholds could be adapted based on historical performance: if a crew consistently produces scores around 7.0–7.5, the ACCEPT threshold could be lowered to reduce unnecessary retries. Conversely, if a crew's output quality is highly variable, stricter thresholds would catch more low-quality outputs.

Implementing adaptive thresholds requires accumulating sufficient run history per crew type, which the current `runs.jsonl` infrastructure supports.

### 12.5 Causal Failure Attribution

The current system detects failures through error message pattern matching (Section 3.2). A more sophisticated approach would build causal models linking failure events to root causes: provider rate limit → retry with alternative → different output quality → governance outcome. This causal chain could be reconstructed from the trace data and used to predict which provider configurations minimize cascading failure probability.

---

## 13. Conclusion

This paper presented an experimental framework for deterministic evaluation of multi-agent LLM systems operating across heterogeneous providers. The framework addresses the absence of formal metrics, reproducible evaluation conditions, and structured observability in existing multi-agent orchestration tools.

Five metrics—Stability Score, Provider Fragility Index, Retry Pressure, Governance Compliance Rate, and Supervisor Strictness Ratio—provide complementary characterizations of system behavior: execution reliability, provider infrastructure quality, retry burden, output compliance, and quality filtering effectiveness. The formal definitions (Section 5) enable consistent measurement across system configurations and temporal comparisons.

The deterministic execution mode produces reproducible results in simulated experiments, confirmed by metric identity across independent runs (Section 6.2). This capability is a prerequisite for controlled comparisons of system configurations: without elimination of infrastructure-level randomness, metric differences cannot be attributed to the experimental variable under study.

The perturbation experiment (Section 6.3) and the parametric failure sweep (Section 7) demonstrate measurable metric sensitivity to controlled failures. The sweep across six failure rates (0%–70%, n=20 each, 120 total runs) reveals that Stability Score follows the linear function SS(f) = 1 − f/2, with maximum variance at f=0.5 consistent with Bernoulli distribution properties. Governance Compliance remains invariant (GCR=1.0, σ=0.0) across all tested rates, confirming the structural decoupling between infrastructure resilience and output compliance.

The comparative analysis (Section 11) establishes that the five capabilities provided by this framework—deterministic execution, failure injection, formal stability metrics, batch statistical aggregation, and governance enforcement—are not present in combination in any of the four compared orchestration frameworks. The threats to validity analysis (Section 9) identifies the principal limitations: simulated rather than real execution, fixed failure injection patterns, and limited sample sizes. The replication protocol (Section 10) provides exact commands and validation criteria for independent reproduction.

The implementation comprises 2,099 lines of Python across nine modules with no dependencies beyond CrewAI and LiteLLM. All experimental results are from executed code with persisted trace artifacts. The framework provides the instrumentation layer necessary for systematic study of multi-agent system behavior, expressing operational characteristics as distributions with means and standard deviations rather than binary verdicts.

---

## References

[1] J. Moura, "CrewAI: Framework for orchestrating role-playing autonomous AI agents," 2024. https://github.com/crewAIInc/crewAI

[2] Q. Wu et al., "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation," arXiv:2308.08155, 2023.

[3] LangChain, "LangGraph: Build resilient language agents as graphs," 2024. https://github.com/langchain-ai/langgraph

[4] S. Hong et al., "MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework," arXiv:2308.00352, 2023.

[5] Databricks, "MLflow: A Machine Learning Lifecycle Platform," 2018. https://mlflow.org

[6] L. Biewald, "Weights & Biases: Experiment Tracking for Machine Learning," 2020. https://wandb.ai

[7] OpenTelemetry Authors, "OpenTelemetry: An observability framework for cloud-native software," 2019. https://opentelemetry.io

[8] M. Nygard, "Release It! Design and Deploy Production-Ready Software," Pragmatic Bookshelf, 2007.

[9] AWS, "Exponential Backoff and Jitter," Amazon Architecture Blog, 2015.

[10] Netflix Technology Blog, "The Netflix Simian Army," 2011.

[11] P. Henderson et al., "Deep Reinforcement Learning that Matters," AAAI 2018.
