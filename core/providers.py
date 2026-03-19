"""
Provider management for LLM services
"""
import os
import random
import time
from dataclasses import dataclass
from typing import Dict, Any, Optional, List


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
            last = p.last_decay if p.last_decay is not None else now
            if now - last > self.decay_interval:
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
        # Fix for type-checking on max key
        selected = candidates[0]
        max_score = -1.0
        for p, s in scores.items():
            if s > max_score:
                max_score = s
                selected = p
        return selected


class ProviderManager:
    """Manager to coordinate LLM providers, health checks and exhaustion status."""
    
    def __init__(self):
        self.providers = {
            "openrouter": os.getenv("OPENROUTER_API_KEY"),
            "groq": os.getenv("GROQ_API_KEY"),
            "mistral": os.getenv("MISTRAL_API_KEY"),
            "cerebras": os.getenv("CEREBRAS_API_KEY"),
            "glm5": os.getenv("GLM5_API_KEY"),
            "huggingface": os.getenv("HF_TOKEN"),
        }
        self.available = {k: v for k, v in self.providers.items() if v}
        self.exhausted = {}
    
    def get_active(self) -> List[str]:
        """Returns list of non-exhausted provider names."""
        return [p for p in self.available.keys() if p not in self.exhausted]
    
    def get_status(self) -> dict:
        """Returns the health status of all keys."""
        return {
            p: {
                "healthy": True,
                "exhausted": p in self.exhausted,
                "recovery_in": self.exhausted.get(p, 0)
            }
            for p in self.providers.keys()
        }
    
    def mark_exhausted(self, provider: str, error: str = ""):
        """Marks a provider as exhausted."""
        self.exhausted[provider] = int(time.time() + 60)  # 1 min recovery
    
    def detect_provider(self, error_str: str) -> str | None:
        """Detects which provider failed from error string."""
        err_lower = error_str.lower()
        for p in self.providers.keys():
            if p in err_lower:
                return p
        return None
    
    def classify_error(self, error_str: str) -> str:
        """Classifies error type."""
        err_lower = error_str.lower()
        if "limit" in err_lower or "429" in err_lower:
            return "rate_limit"
        if "timeout" in err_lower:
            return "timeout"
        return "api_error"
    
    def get_best_provider(self) -> Dict[str, Any]:
        """Get the best available provider (prioritized)"""
        priorities = ["glm5", "huggingface", "openrouter", "groq", "mistral", "cerebras"]
        for provider in priorities:
            if provider in self.available and provider not in self.exhausted:
                return {
                    "provider": provider,
                    "api_key": self.available[provider],
                    "model": self._get_model_for_provider(provider)
                }
        # If all exhausted, return first available
        for provider in self.available:
            return {
                "provider": provider,
                "api_key": self.available[provider],
                "model": self._get_model_for_provider(provider)
            }
        return {"provider": "none", "error": "No LLM providers configured"}
    
    def _get_model_for_provider(self, provider: str) -> str:
        """Get default model for provider"""
        models = {
            "openrouter": "deepseek/deepseek-r1:free",
            "groq": "mixtral-8x7b-32768",
            "mistral": "mistral-small-latest",
            "cerebras": "cerebras-1.0",
            "glm5": "glm-5-turbo",
            "huggingface": "meta-llama/Llama-3.1-8B-Instruct"
        }
        return models.get(provider, "unknown")


# FUNCIÓN CRÍTICA QUE FALTABA
def get_llm_for_role(role: str = "default") -> Dict[str, Any]:
    """
    Get LLM configuration for a specific role
    Used by crew.py and other modules
    """
    manager = ProviderManager()
    best = manager.get_best_provider()
    
    if best["provider"] == "none":
        return {
            "error": True,
            "message": "No LLM providers configured",
            "available": manager.available
        }
    
    return {
        "provider": best["provider"],
        "model": best["model"],
        "api_key": best["api_key"],
        "temperature": 0.7,
        "max_tokens": 4000,
        "role": role
    }


# Alias for backward compatibility
def get_llm(role: str = "default") -> Dict[str, Any]:
    """Alias for get_llm_for_role"""
    return get_llm_for_role(role)
