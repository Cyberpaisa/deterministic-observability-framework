import random
import time
from dataclasses import dataclass


@dataclass
class BetaParams:
    alpha: float = 1.0
    beta: float = 1.0
    last_decay: float | None = None

    def __post_init__(self):
        if self.last_decay is None:
            self.last_decay = time.time()

    def mean(self):
        return self.alpha / (self.alpha + self.beta)

    def variance(self):
        a = self.alpha
        b = self.beta
        return (a * b) / (((a + b) ** 2) * (a + b + 1))

    def sample(self):
        return random.betavariate(self.alpha, self.beta)


class BayesianProviderSelector:

    def __init__(self, providers=None, decay_interval=3600, decay_factor=0.9):
        self.providers = providers or []
        self.decay_interval = decay_interval
        self.decay_factor = decay_factor
        self._providers = {}
        self.reset()

    def reset(self):
        self._providers = {p: BetaParams() for p in self.providers}

    def _ensure(self, provider):
        if provider not in self._providers:
            self._providers[provider] = BetaParams()

    def record_success(self, provider):
        self._ensure(provider)
        self._providers[provider].alpha += 1

    def record_failure(self, provider):
        self._ensure(provider)
        self._providers[provider].beta += 1

    def _apply_decay(self):
        now = time.time()
        for p in self._providers.values():
            if now - p.last_decay > self.decay_interval:
                p.alpha = max(1.0, p.alpha * self.decay_factor)
                p.beta = max(1.0, p.beta * self.decay_factor)
                p.last_decay = now

    def get_confidence(self, provider):
        if provider not in self._providers:
            return 0.5
        self._apply_decay()
        return self._providers[provider].mean()

    def get_all_confidences(self):
        self._apply_decay()
        return {p: self._providers[p].mean() for p in self._providers}

    def get_status(self):
        self._apply_decay()
        status = {}

        for name, p in self._providers.items():
            status[name] = {
                "alpha": p.alpha,
                "beta": p.beta,
                "confidence": p.mean(),
                "variance": p.variance(),
                "total_observations": p.alpha + p.beta - 2,
            }

        return status

    def select_provider(self, providers=None):

        if providers is None:
            candidates = self.providers
        else:
            candidates = providers

        if not candidates:
            raise ValueError("No providers available")

        self._apply_decay()

        scores = {}

        for p in candidates:
            self._ensure(p)
            scores[p] = self._providers[p].sample()

        return max(scores, key=scores.get)


class ProviderManager:
    """Manager to coordinate LLM providers, health checks and exhaustion status."""
    def __init__(self):
        # Lazy imports to avoid circular dependencies
        import llm_config
        self.config = llm_config

    def get_active(self) -> list[str]:
        """Returns list of non-exhausted provider names."""
        return self.config._get_active_providers()

    def get_status(self) -> dict:
        """Returns the health status of all keys."""
        try:
            keys_status = self.config.validate_keys()
            # Map simple boolean to a more detailed status expected by some callers
            status = {}
            for k, v in keys_status.items():
                status[k] = {
                    "healthy": v,
                    "exhausted": not self.config._is_available(k),
                    "recovery_in": 0 # Simplified
                }
            return status
        except Exception:
            return {}

    def mark_exhausted(self, provider: str, error: str = ""):
        """Marks a provider as exhausted."""
        self.config.mark_provider_exhausted(provider)

    def detect_provider(self, error_str: str) -> str | None:
        """Detects which provider failed from error string."""
        # Simple heuristic
        providers = ["groq", "nvidia", "cerebras", "minimax", "zhipu", "gemini", "sambanova", "openrouter"]
        for p in providers:
            if p in error_str.lower():
                return p
        return None

    def classify_error(self, error_str: str) -> str:
        """Classifies error type."""
        err_lower = error_str.lower()
        if "limit" in err_lower or "429" in err_lower:
            return "rate_limit"
        return "api_error"
