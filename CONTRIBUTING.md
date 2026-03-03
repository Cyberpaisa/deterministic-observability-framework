# Contributing

## Requirements

- Python 3.11+
- Dependencies: `pip install -r requirements.txt`
- Provider API keys in `.env` (see `.env.example`)

## Running Experiments Locally

```bash
# Baseline (no failures, deterministic)
python -c "
from core.experiment import run_experiment
result = run_experiment(n_runs=10, deterministic=True)
print(result['aggregate'])
"

# Parametric sweep
python -c "
from core.experiment import run_parametric_sweep
run_parametric_sweep(rates=[0.0, 0.1, 0.2, 0.3, 0.5, 0.7], n_runs=20)
"
```

## Code Style

- Python 3.11+ features (type hints with `list[dict]`, dataclasses)
- Data persistence: JSONL (one JSON object per line)
- No external observability dependencies — all tracing is internal
- Singletons (`ProviderManager`) must be reset between experiments

## Adding a New Metric

1. Define the metric mathematically in `core/observability.py` → `compute_derived_metrics()`
2. Add the field to `RunTrace` dataclass
3. Update `run_experiment()` aggregation in `core/experiment.py`
4. Document the metric in the paper (`paper/PAPER_OBSERVABILITY_LAB.md`, Section 5)

## Adding a Governance Rule

1. Open `core/governance.py`
2. Add rule to `HARD_RULES` (blocks output) or `SOFT_RULES` (warning only)
3. Each rule is a function `(text: str) -> bool` returning `True` if violation detected
4. Run baseline experiment to verify GCR impact

## Singleton Reset Requirement

All singletons (`ProviderManager`) accumulate state across runs. When adding new singletons:

1. Implement a `reset_all()` or `reset()` method
2. Call it at the start of `run_experiment()` (see the existing `ProviderManager().reset_all()` call)
3. Verify that parametric sweeps produce identical results with and without the reset

## Submitting Changes

1. Fork the repository
2. Create a feature branch from `main`
3. Run the baseline experiment to verify no regression
4. Submit a pull request with experiment results included
