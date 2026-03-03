"""
Provider Resilience Layer — TTL, backoff exponencial, reactivacion automatica.

Estado por modelo, no global permanente. Ningun bloqueo irreversible.
"""

import os
import time
import logging
import threading
from dataclasses import dataclass, field
from crewai import LLM
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger("core.providers")

# LiteLLM env vars
if os.getenv("NVIDIA_API_KEY") and not os.getenv("NVIDIA_NIM_API_KEY"):
    os.environ["NVIDIA_NIM_API_KEY"] = os.getenv("NVIDIA_API_KEY")


@dataclass
class ProviderState:
    """Estado de un provider con TTL y backoff."""
    name: str
    exhausted: bool = False
    exhaust_time: float = 0.0
    ttl_seconds: float = 300.0  # 5 minutos por defecto
    failure_count: int = 0
    last_error: str = ""
    supports_structured_output: bool = True

    @property
    def is_available(self) -> bool:
        if not self.exhausted:
            return True
        elapsed = time.time() - self.exhaust_time
        if elapsed >= self.ttl_seconds:
            self._recover()
            return True
        return False

    @property
    def recovery_in(self) -> float:
        if not self.exhausted:
            return 0.0
        remaining = self.ttl_seconds - (time.time() - self.exhaust_time)
        return max(0.0, remaining)

    def mark_exhausted(self, error: str = "", ttl_override: float = 0.0):
        self.exhausted = True
        self.exhaust_time = time.time()
        self.failure_count += 1
        self.last_error = error[:200]
        # Backoff exponencial: 5min, 10min, 20min (max 20min)
        if ttl_override > 0:
            self.ttl_seconds = ttl_override
        else:
            self.ttl_seconds = min(300 * (2 ** (self.failure_count - 1)), 1200)
        logger.warning(
            f"Provider '{self.name}' exhausted (TTL={self.ttl_seconds}s, "
            f"failures={self.failure_count}): {error[:100]}"
        )

    def _recover(self):
        self.exhausted = False
        logger.info(f"Provider '{self.name}' recovered after {self.ttl_seconds}s TTL")

    def reset(self):
        self.exhausted = False
        self.exhaust_time = 0.0
        self.failure_count = 0
        self.last_error = ""
        self.ttl_seconds = 300.0


class ProviderManager:
    """Gestor central de providers con TTL, backoff y estado por modelo."""

    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._initialized = False
            return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        self._providers: dict[str, ProviderState] = {
            "groq": ProviderState("groq"),
            "nvidia": ProviderState("nvidia", supports_structured_output=False),
            "cerebras": ProviderState("cerebras"),
            "zhipu": ProviderState("zhipu"),
        }

    # ── LLM Factories ──

    @staticmethod
    def _make_groq(model="llama-3.3-70b-versatile", temperature=0.3) -> LLM | None:
        key = os.getenv("GROQ_API_KEY")
        if not key:
            return None
        return LLM(model=f"groq/{model}", api_key=key, temperature=temperature, max_tokens=4096)

    @staticmethod
    def _make_nvidia(model="deepseek-ai/deepseek-v3.2", temperature=0.3) -> LLM | None:
        key = os.getenv("NVIDIA_API_KEY")
        if not key:
            return None
        return LLM(model=f"nvidia_nim/{model}", api_key=key, temperature=temperature, max_tokens=4096)

    @staticmethod
    def _make_cerebras(model="gpt-oss-120b", temperature=0.3) -> LLM | None:
        key = os.getenv("CEREBRAS_API_KEY")
        if not key:
            return None
        return LLM(model=f"cerebras/{model}", api_key=key, temperature=temperature, max_tokens=4096)

    @staticmethod
    def _make_zhipu(model="glm-4.7-flash", temperature=0.3) -> LLM | None:
        key = os.getenv("ZHIPU_API_KEY")
        if not key:
            return None
        return LLM(
            model=f"openai/{model}", api_key=key,
            base_url="https://api.z.ai/api/paas/v4/",
            temperature=temperature, max_tokens=4096,
            extra_body={"enable_thinking": False},
        )

    @staticmethod
    def _make_gemini(temperature=0.7) -> LLM | None:
        key = os.getenv("GEMINI_API_KEY")
        if not key:
            return None
        return LLM(model="gemini/gemini-2.5-flash", api_key=key, temperature=temperature)

    # ── Fallback chains per role ──

    ROLE_CHAINS: dict[str, list[tuple[str, dict]]] = {
        "code_architect": [
            ("nvidia", {"model": "moonshotai/kimi-k2.5", "temperature": 0.2}),
            ("groq", {"model": "moonshotai/kimi-k2-instruct", "temperature": 0.2}),
            ("cerebras", {"model": "gpt-oss-120b", "temperature": 0.2}),
            ("zhipu", {"temperature": 0.2}),
        ],
        "research_analyst": [
            ("groq", {"model": "llama-3.3-70b-versatile", "temperature": 0.5}),
            ("nvidia", {"model": "deepseek-ai/deepseek-v3.2", "temperature": 0.5}),
            ("cerebras", {"model": "gpt-oss-120b", "temperature": 0.5}),
            ("zhipu", {"temperature": 0.5}),
        ],
        "mvp_strategist": [
            ("nvidia", {"model": "qwen/qwen3.5-397b-a17b", "temperature": 0.6}),
            ("cerebras", {"model": "gpt-oss-120b", "temperature": 0.6}),
            ("zhipu", {"temperature": 0.6}),
            ("groq", {"model": "llama-3.3-70b-versatile", "temperature": 0.6}),
        ],
        "data_engineer": [
            ("cerebras", {"model": "gpt-oss-120b", "temperature": 0.1}),
            ("nvidia", {"model": "deepseek-ai/deepseek-v3.2", "temperature": 0.1}),
            ("groq", {"model": "llama-3.3-70b-versatile", "temperature": 0.1}),
            ("zhipu", {"temperature": 0.1}),
        ],
        "project_organizer": [
            ("groq", {"model": "qwen/qwen3-32b", "temperature": 0.3}),
            ("cerebras", {"model": "gpt-oss-120b", "temperature": 0.3}),
            ("zhipu", {"temperature": 0.3}),
            ("nvidia", {"model": "deepseek-ai/deepseek-v3.2", "temperature": 0.3}),
        ],
        "qa_reviewer": [
            ("cerebras", {"model": "gpt-oss-120b", "temperature": 0.2}),
            ("groq", {"model": "llama-3.3-70b-versatile", "temperature": 0.2}),
            ("nvidia", {"model": "deepseek-ai/deepseek-v3.2", "temperature": 0.2}),
            ("zhipu", {"temperature": 0.2}),
        ],
        "verifier": [
            ("cerebras", {"model": "gpt-oss-120b", "temperature": 0.2}),
            ("groq", {"model": "llama-3.3-70b-versatile", "temperature": 0.2}),
            ("nvidia", {"model": "deepseek-ai/deepseek-v3.2", "temperature": 0.2}),
            ("zhipu", {"temperature": 0.2}),
        ],
        "narrative_content": [
            ("cerebras", {"model": "gpt-oss-120b", "temperature": 0.7}),
            ("zhipu", {"temperature": 0.7}),
            ("nvidia", {"model": "deepseek-ai/deepseek-v3.2", "temperature": 0.7}),
            ("groq", {"temperature": 0.7}),
        ],
    }

    FACTORIES = {
        "groq": "_make_groq",
        "nvidia": "_make_nvidia",
        "cerebras": "_make_cerebras",
        "zhipu": "_make_zhipu",
    }

    def get_llm(self, role: str, needs_structured_output: bool = False) -> tuple[LLM, str]:
        """Returns (llm, provider_name) following fallback chain.

        Skips exhausted providers (with TTL auto-recovery).
        Skips NVIDIA if structured output is needed.
        """
        role = role.lower()
        chain = self.ROLE_CHAINS.get(role, self.ROLE_CHAINS["qa_reviewer"])

        for provider_name, kwargs in chain:
            state = self._providers.get(provider_name)
            if not state or not state.is_available:
                continue
            if needs_structured_output and not state.supports_structured_output:
                continue

            factory = getattr(self, self.FACTORIES[provider_name])
            llm = factory(**kwargs)
            if llm:
                return llm, provider_name

        # Absolute fallback: cerebras with defaults
        fallback = self._make_cerebras()
        if fallback:
            return fallback, "cerebras"

        raise ValueError(f"No providers available for role '{role}'")

    def mark_exhausted(self, provider: str, error: str = ""):
        provider = provider.lower()
        state = self._providers.get(provider)
        if state:
            state.mark_exhausted(error)

    def get_active(self) -> list[str]:
        return [name for name, state in self._providers.items() if state.is_available]

    def get_status(self) -> dict:
        return {
            name: {
                "available": state.is_available,
                "exhausted": state.exhausted,
                "recovery_in": round(state.recovery_in, 1),
                "failure_count": state.failure_count,
                "ttl": state.ttl_seconds,
                "supports_structured": state.supports_structured_output,
            }
            for name, state in self._providers.items()
        }

    def reset_all(self):
        for state in self._providers.values():
            state.reset()

    def detect_provider(self, error_str: str) -> str | None:
        """Detect which provider failed from error message."""
        error_lower = error_str.lower()
        patterns = {
            "groq": ["groq", "llama-3.3", "qwen3-32b", "kimi-k2-instruct"],
            "nvidia": ["nvidia", "nim", "kimi-k2.5", "qwen3.5"],
            "cerebras": ["cerebras", "gpt-oss"],
            "zhipu": ["zhipu", "z.ai", "glm"],
        }
        for provider, keywords in patterns.items():
            if any(kw in error_lower for kw in keywords):
                return provider
        return None

    def classify_error(self, error_str: str) -> dict:
        """Classify error type and recommended action."""
        e = error_str.lower()
        if any(k in e for k in ["rate_limit", "rate limit", "429", "resource_exhausted"]):
            return {"type": "RATE_LIMIT", "transient": True, "retry": True, "switch": True}
        if any(k in e for k in ["authentication", "api key", "unauthorized"]):
            return {"type": "AUTH_FAILURE", "transient": False, "retry": False, "switch": True}
        if any(k in e for k in ["invalid grammar", "not supported", "bad request"]):
            return {"type": "MODEL_INCOMPATIBLE", "transient": False, "retry": False, "switch": True}
        if any(k in e for k in ["timeout", "timed out"]):
            return {"type": "TIMEOUT", "transient": True, "retry": True, "switch": False}
        if any(k in e for k in ["validation error", "pydantic"]):
            return {"type": "PARSE_ERROR", "transient": False, "retry": True, "switch": True}
        return {"type": "UNKNOWN", "transient": False, "retry": False, "switch": False}


# ── Backward compatibility with llm_config.py ──

_pm = ProviderManager()


def get_llm_for_role(role: str) -> LLM:
    llm, _ = _pm.get_llm(role)
    return llm


def mark_provider_exhausted(provider: str):
    _pm.mark_exhausted(provider)


def reset_exhausted_providers():
    _pm.reset_all()


def _get_active_providers() -> list[str]:
    return _pm.get_active()


def validate_keys() -> dict:
    status = {
        "groq": bool(os.getenv("GROQ_API_KEY")),
        "gemini": bool(os.getenv("GEMINI_API_KEY")),
        "nvidia": bool(os.getenv("NVIDIA_API_KEY")),
        "cerebras": bool(os.getenv("CEREBRAS_API_KEY")),
        "sambanova": bool(os.getenv("SAMBANOVA_API_KEY")),
        "openrouter": bool(os.getenv("OPENROUTER_API_KEY")),
        "zhipu": bool(os.getenv("ZHIPU_API_KEY")),
        "serper": bool(os.getenv("SERPER_API_KEY")),
        "tavily": bool(os.getenv("TAVILY_API_KEY")),
    }
    if not status["groq"]:
        raise ValueError("GROQ_API_KEY no configurada. https://console.groq.com")
    return status
