"""
Run-Level Observability — FASE 1.

Full run traces with UUID v4, session tracking, ordered steps,
token counting, derived metrics, and deterministic mode.

Every execution generates a complete RunTrace exported as JSON.
Derived metrics saved to logs/experiments/runs.jsonl.
"""

import os
import json
import time
import uuid
import hashlib
import logging
import math
from dataclasses import dataclass, field, asdict
from typing import Any

logger = logging.getLogger("core.observability")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXPERIMENTS_DIR = os.path.join(BASE_DIR, "logs", "experiments")
TRACES_DIR = os.path.join(BASE_DIR, "logs", "traces")

# ── Deterministic Mode ──
DETERMINISTIC_MODE = bool(os.getenv("DETERMINISTIC_MODE", ""))
_DETERMINISTIC_SEED = 42
_DETERMINISTIC_PROVIDER_ORDER = ["cerebras", "groq", "nvidia", "zhipu"]


def set_deterministic(enabled: bool):
    """Toggle deterministic mode at runtime."""
    global DETERMINISTIC_MODE
    DETERMINISTIC_MODE = enabled
    if enabled:
        import random
        random.seed(_DETERMINISTIC_SEED)
        logger.info(f"Deterministic mode ON (seed={_DETERMINISTIC_SEED})")
    else:
        logger.info("Deterministic mode OFF")


def get_deterministic_providers() -> list[str] | None:
    """Return fixed provider order if deterministic mode is on."""
    if DETERMINISTIC_MODE:
        return list(_DETERMINISTIC_PROVIDER_ORDER)
    return None


# ── Session Management ──

_SESSION_ID: str = ""


def get_session_id() -> str:
    global _SESSION_ID
    if not _SESSION_ID:
        _SESSION_ID = str(uuid.uuid4())
    return _SESSION_ID


def reset_session():
    global _SESSION_ID
    _SESSION_ID = str(uuid.uuid4())
    return _SESSION_ID


# ── Step Trace ──

@dataclass
class StepTrace:
    """One step in a run trace."""
    step_index: int
    agent: str
    provider: str
    latency_ms: float = 0.0
    retries: int = 0
    status: str = "pending"
    supervisor_score: float = 0.0
    governance_passed: bool = True
    token_input: int = 0
    token_output: int = 0
    error: str = ""
    provider_switched: bool = False


# ── Run Trace ──

@dataclass
class RunTrace:
    """Complete trace for one execution run."""
    run_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    session_id: str = field(default_factory=get_session_id)
    crew_name: str = ""
    mode: str = "production"  # research | production
    timestamp_start: str = ""
    timestamp_end: str = ""
    start_epoch: float = 0.0
    end_epoch: float = 0.0
    total_latency_ms: float = 0.0
    status: str = "pending"  # ok | error | escalated
    deterministic: bool = False
    input_text: str = ""
    input_hash: str = ""
    output_len: int = 0
    steps: list[StepTrace] = field(default_factory=list)
    # Derived metrics
    stability_score: float = 0.0
    provider_fragility_index: float = 0.0
    retry_pressure: float = 0.0
    governance_compliance_rate: float = 0.0
    supervisor_score_final: float = 0.0
    supervisor_decision: str = ""
    total_retries: int = 0
    total_token_input: int = 0
    total_token_output: int = 0

    def to_dict(self) -> dict:
        d = asdict(self)
        d["steps"] = [asdict(s) for s in self.steps]
        return d


# ── Token Estimation ──

def estimate_tokens(text: str) -> int:
    """Estimate token count (~4 chars per token for multilingual)."""
    if not text:
        return 0
    return max(1, len(text) // 4)


# ── Derived Metrics Calculator ──

def compute_derived_metrics(trace: RunTrace) -> RunTrace:
    """Compute all derived metrics from a completed RunTrace."""
    steps = trace.steps
    n = len(steps) if steps else 1

    # Stability Score = 1 - (step_failures / total_steps)
    failures = sum(1 for s in steps if s.status == "failed")
    trace.stability_score = round(1.0 - (failures / n), 4)

    # Provider Fragility Index = provider_switches / total_steps
    switches = sum(1 for s in steps if s.provider_switched)
    trace.provider_fragility_index = round(switches / n, 4)

    # Retry Pressure = retries / total_steps
    total_retries = sum(s.retries for s in steps)
    trace.retry_pressure = round(total_retries / n, 4)
    trace.total_retries = total_retries

    # Governance Compliance Rate = governance_passed_steps / total_steps
    gov_passed = sum(1 for s in steps if s.governance_passed)
    trace.governance_compliance_rate = round(gov_passed / n, 4)

    # Token totals
    trace.total_token_input = sum(s.token_input for s in steps)
    trace.total_token_output = sum(s.token_output for s in steps)

    # Total latency
    trace.total_latency_ms = round(sum(s.latency_ms for s in steps), 1)

    return trace


# ── Persistence ──

class RunTraceStore:
    """Persists RunTraces as JSON files and aggregates to runs.jsonl."""

    def __init__(self):
        os.makedirs(EXPERIMENTS_DIR, exist_ok=True)
        os.makedirs(TRACES_DIR, exist_ok=True)
        self._runs_file = os.path.join(EXPERIMENTS_DIR, "runs.jsonl")

    def save(self, trace: RunTrace) -> str:
        """Save trace as individual JSON + append to runs.jsonl. Returns trace path."""
        trace = compute_derived_metrics(trace)

        # Individual JSON trace
        trace_path = os.path.join(TRACES_DIR, f"{trace.run_id}.json")
        with open(trace_path, "w") as f:
            json.dump(trace.to_dict(), f, indent=2, default=str)

        # Append summary to runs.jsonl
        summary = {
            "run_id": trace.run_id,
            "session_id": trace.session_id,
            "crew_name": trace.crew_name,
            "mode": trace.mode,
            "timestamp_start": trace.timestamp_start,
            "timestamp_end": trace.timestamp_end,
            "total_latency_ms": trace.total_latency_ms,
            "status": trace.status,
            "deterministic": trace.deterministic,
            "steps_count": len(trace.steps),
            "stability_score": trace.stability_score,
            "provider_fragility_index": trace.provider_fragility_index,
            "retry_pressure": trace.retry_pressure,
            "governance_compliance_rate": trace.governance_compliance_rate,
            "supervisor_score_final": trace.supervisor_score_final,
            "supervisor_decision": trace.supervisor_decision,
            "total_retries": trace.total_retries,
            "total_token_input": trace.total_token_input,
            "total_token_output": trace.total_token_output,
            "output_len": trace.output_len,
            "raw_trace_path": trace_path,
        }
        with open(self._runs_file, "a") as f:
            f.write(json.dumps(summary, default=str) + "\n")

        logger.info(f"Trace saved: {trace_path}")
        return trace_path

    def load_runs(self, n: int = 0) -> list[dict]:
        """Load run summaries from runs.jsonl."""
        if not os.path.exists(self._runs_file):
            return []
        runs = []
        with open(self._runs_file) as f:
            for line in f:
                line = line.strip()
                if line:
                    runs.append(json.loads(line))
        if n > 0:
            return runs[-n:]
        return runs

    def load_trace(self, run_id: str) -> dict | None:
        """Load full trace JSON by run_id."""
        path = os.path.join(TRACES_DIR, f"{run_id}.json")
        if not os.path.exists(path):
            return None
        with open(path) as f:
            return json.load(f)

    def aggregate(self, runs: list[dict] | None = None) -> dict:
        """Compute aggregated statistics across runs."""
        if runs is None:
            runs = self.load_runs()
        if not runs:
            return {"total_runs": 0}

        n = len(runs)

        def _mean(values: list[float]) -> float:
            return sum(values) / len(values) if values else 0.0

        def _stddev(values: list[float]) -> float:
            if len(values) < 2:
                return 0.0
            m = _mean(values)
            variance = sum((x - m) ** 2 for x in values) / (len(values) - 1)
            return math.sqrt(variance)

        stability = [r["stability_score"] for r in runs]
        fragility = [r["provider_fragility_index"] for r in runs]
        retry_p = [r["retry_pressure"] for r in runs]
        gov_rate = [r["governance_compliance_rate"] for r in runs]
        latency = [r["total_latency_ms"] for r in runs]
        sup_scores = [r["supervisor_score_final"] for r in runs if r.get("supervisor_score_final", 0) > 0]
        tok_in = [r.get("total_token_input", 0) for r in runs]
        tok_out = [r.get("total_token_output", 0) for r in runs]

        statuses = {}
        for r in runs:
            s = r.get("status", "unknown")
            statuses[s] = statuses.get(s, 0) + 1

        # Supervisor Strictness Ratio = escalations / total_runs
        escalations = statuses.get("escalated", 0)
        strictness = escalations / n if n > 0 else 0.0

        return {
            "total_runs": n,
            "statuses": statuses,
            "stability_score": {"mean": round(_mean(stability), 4), "stddev": round(_stddev(stability), 4)},
            "provider_fragility_index": {"mean": round(_mean(fragility), 4), "stddev": round(_stddev(fragility), 4)},
            "retry_pressure": {"mean": round(_mean(retry_p), 4), "stddev": round(_stddev(retry_p), 4)},
            "governance_compliance_rate": {"mean": round(_mean(gov_rate), 4), "stddev": round(_stddev(gov_rate), 4)},
            "supervisor_strictness_ratio": round(strictness, 4),
            "supervisor_score": {"mean": round(_mean(sup_scores), 2), "stddev": round(_stddev(sup_scores), 2)} if sup_scores else {"mean": 0, "stddev": 0},
            "latency_ms": {"mean": round(_mean(latency), 1), "stddev": round(_stddev(latency), 1)},
            "tokens": {"input_total": sum(tok_in), "output_total": sum(tok_out)},
        }
