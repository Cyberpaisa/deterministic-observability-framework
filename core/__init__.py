"""
Core infrastructure — FASE 0 Hardening + FASE 1 Observability.
Providers, checkpointing, memory, governance, metrics, supervisor, crew_runner.
Observability, experiment framework, deterministic mode.
"""

# FASE 0
from core.checkpointing import CheckpointManager
from core.memory_manager import MemoryManager
from core.metrics import MetricsLogger
from core.governance import ConstitutionEnforcer
from core.supervisor import MetaSupervisor
from core.crew_runner import run_crew

# FASE 1
from core.observability import (
    RunTrace, StepTrace, RunTraceStore,
    compute_derived_metrics, estimate_tokens,
    set_deterministic, get_session_id, reset_session,
    DETERMINISTIC_MODE,
)
from core.experiment import run_experiment, run_parametric_sweep, ExperimentDataset
