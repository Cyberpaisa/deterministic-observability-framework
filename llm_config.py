"""
Configuración de LLMs — 7 proveedores gratuitos + Smart Router + Retry.

Distribución de carga (Research Crew):
  Researcher:  Groq Llama 3.3         (tool-calling)
  Strategist:  NVIDIA Qwen3.5-397B    (razonamiento)
  QA Reviewer: Cerebras GPT-OSS 120B  (tool-calling)
  Verifier:    Cerebras GPT-OSS 120B  (libera Groq TPM)

Proveedores activos (7):
  GROQ:       Llama 3.3 70B, Qwen3-32B, GPT-OSS 120B, Kimi K2  (131K, 12K TPM free)
  NVIDIA:     Qwen3.5-397B, Kimi K2.5, DeepSeek V3.2           (128K, 1000 credits)
  CEREBRAS:   GPT-OSS 120B                                      (128K, 1M tok/día free)
  GEMINI:     2.5 Flash                                (1M context, 20 req/día free)
  SAMBANOVA:  DeepSeek V3.2                            (BACKUP — 24K limit)
  OPENROUTER: Hermes 405B free                         (variable)
  ZHIPU:      GLM-4.7-Flash                             (128K, gratis, 745B MoE)

Búsqueda web: Serper (Google) → Tavily → DuckDuckGo
"""

import os
import time
import logging
from dotenv import load_dotenv
from crewai import LLM

load_dotenv()

# LiteLLM busca NVIDIA_NIM_API_KEY para el prefijo nvidia_nim/
# Copiamos NVIDIA_API_KEY si existe
if os.getenv("NVIDIA_API_KEY") and not os.getenv("NVIDIA_NIM_API_KEY"):
    os.environ["NVIDIA_NIM_API_KEY"] = os.getenv("NVIDIA_API_KEY")

# Zhipu: NO copiar la key a OPENAI_API_KEY — LiteLLM la envia a api.openai.com
# En su lugar, usamos api_key directo en la instancia LLM con base_url.

logger = logging.getLogger(__name__)


# ═══════════════════════════════════════════════════════
# PROVEEDORES
# ═══════════════════════════════════════════════════════

def get_groq_llm(model="llama-3.3-70b-versatile", temperature=0.3):
    """Groq — 131K context, ultrarrápido. 12K TPM free tier."""
    return LLM(
        model=f"groq/{model}",
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=temperature,
        max_tokens=4096,
    )


def get_nvidia_llm(model="deepseek-ai/deepseek-v3.2", temperature=0.3):
    """NVIDIA NIM — 128K context. Qwen3.5-397B, Kimi K2.5, DeepSeek V3.2."""
    api_key = os.getenv("NVIDIA_API_KEY")
    if not api_key:
        return None
    return LLM(
        model=f"nvidia_nim/{model}",
        api_key=api_key,
        temperature=temperature,
        max_tokens=4096,
    )


def get_cerebras_llm(model="gpt-oss-120b", temperature=0.3):
    """Cerebras — 128K context, ultrarrápido (0.3s)."""
    api_key = os.getenv("CEREBRAS_API_KEY")
    if not api_key:
        return None
    return LLM(
        model=f"cerebras/{model}",
        api_key=api_key,
        temperature=temperature,
        max_tokens=4096,
    )


def get_sambanova_llm(model="DeepSeek-V3.2", temperature=0.3):
    """SambaNova — BACKUP ONLY (24K context limit)."""
    api_key = os.getenv("SAMBANOVA_API_KEY")
    if not api_key:
        return None
    return LLM(
        model=f"sambanova/{model}",
        api_key=api_key,
        temperature=temperature,
        max_tokens=4096,
    )


def get_openrouter_llm(model="nousresearch/hermes-3-llama-3.1-405b:free", temperature=0.3):
    """OpenRouter — modelos gratuitos (rate limited)."""
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        return None
    return LLM(
        model=f"openrouter/{model}",
        api_key=api_key,
        temperature=temperature,
        max_tokens=4096,
    )


def get_gemini_llm(temperature=0.7):
    """Gemini 2.5 Flash — 1M context window. 20 req/día free."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return None
    return LLM(
        model="gemini/gemini-2.5-flash",
        api_key=api_key,
        temperature=temperature,
    )


def get_zhipu_llm(model="glm-4.7-flash", temperature=0.3):
    """Zhipu AI — GLM-4.7-Flash gratis, 128K context, 745B MoE."""
    api_key = os.getenv("ZHIPU_API_KEY")
    if not api_key:
        return None
    return LLM(
        model=f"openai/{model}",
        api_key=api_key,
        base_url="https://api.z.ai/api/paas/v4/",
        temperature=temperature,
        max_tokens=4096,
        extra_body={"enable_thinking": False},
    )



# ═══════════════════════════════════════════════════════
# PROVIDER RESILIENCE — Auto-fallback cuando un provider cae
# ═══════════════════════════════════════════════════════

_exhausted_providers: set[str] = set()


def mark_provider_exhausted(provider: str):
    """Marca un provider como agotado (rate limit). Se salta en todas las asignaciones."""
    provider = provider.lower()
    _exhausted_providers.add(provider)
    logger.warning(f"Provider '{provider}' marcado como agotado. Activos sin él: {_get_active_providers()}")


def reset_exhausted_providers():
    """Resetea todos los providers a disponibles."""
    _exhausted_providers.clear()
    logger.info("Todos los providers reseteados a disponibles.")


def _get_active_providers() -> list[str]:
    """Lista providers activos (no agotados)."""
    all_providers = ["groq", "nvidia", "cerebras", "zhipu"]
    return [p for p in all_providers if p not in _exhausted_providers]


def _is_available(provider: str) -> bool:
    """Verifica si un provider está disponible (no agotado + tiene API key)."""
    return provider.lower() not in _exhausted_providers


def _try_get(provider: str, getter, **kwargs):
    """Intenta obtener un LLM de un provider si está disponible."""
    if not _is_available(provider):
        return None
    return getter(**kwargs)


# ═══════════════════════════════════════════════════════
# ASIGNACIÓN POR ROL — Con auto-fallback resiliente
# ═══════════════════════════════════════════════════════
# Cada rol tiene cadena completa: Primario → Fallback 1 → Fallback 2 → Fallback 3
# Si un provider está agotado, se salta automáticamente al siguiente.

def get_llm_for_role(role: str) -> LLM:
    """
    Distribución resiliente — Si un provider cae, salta al siguiente automáticamente.

    | Agente            | Primario              | Fallback 1            | Fallback 2          | Fallback 3      |
    |-------------------|-----------------------|-----------------------|---------------------|-----------------|
    | Code Architect    | Kimi K2.5 (NVIDIA)    | Kimi K2 (Groq)        | GPT-OSS (Cerebras)  | GLM-4.7 (Zhipu) |
    | Research Analyst  | Llama 3.3 (Groq)      | DeepSeek V3.2 (NV)    | GPT-OSS (Cerebras)  | GLM-4.7 (Zhipu) |
    | MVP Strategist    | Qwen3.5-397B (NVIDIA) | GLM-4.7 (Zhipu)       | GPT-OSS (Cerebras)  | Llama 3.3 (Groq)|
    | Data Engineer     | GPT-OSS (Cerebras)    | DeepSeek V3.2 (NV)    | Llama 3.3 (Groq)    | GLM-4.7 (Zhipu) |
    | Project Organizer | Qwen3-32B (Groq)      | GLM-4.7 (Zhipu)       | GPT-OSS (Cerebras)  | DeepSeek (NV)   |
    | QA Reviewer       | GPT-OSS (Cerebras)    | Llama 3.3 (Groq)      | DeepSeek V3.2 (NV)  | GLM-4.7 (Zhipu) |
    | Verifier          | GPT-OSS (Cerebras)    | Llama 3.3 (Groq)      | DeepSeek V3.2 (NV)  | GLM-4.7 (Zhipu) |
    | Narrative         | GLM-4.7 (Zhipu)       | DeepSeek V3.2 (NV)    | GPT-OSS (Cerebras)  | Llama 3.3 (Groq)|
    """
    role = role.lower()

    # Code Architect: NVIDIA → Groq → Cerebras → Zhipu
    if role == "code_architect":
        for llm in [
            lambda: _try_get("nvidia", get_nvidia_llm, model="moonshotai/kimi-k2.5", temperature=0.2),
            lambda: _try_get("groq", get_groq_llm, model="moonshotai/kimi-k2-instruct", temperature=0.2),
            lambda: _try_get("cerebras", get_cerebras_llm, model="gpt-oss-120b", temperature=0.2),
            lambda: _try_get("zhipu", get_zhipu_llm, temperature=0.2),
        ]:
            result = llm()
            if result:
                return result

    # Research Analyst: Groq → NVIDIA → Cerebras → Zhipu
    if role == "research_analyst":
        for llm in [
            lambda: _try_get("groq", get_groq_llm, model="llama-3.3-70b-versatile", temperature=0.5),
            lambda: _try_get("nvidia", get_nvidia_llm, model="deepseek-ai/deepseek-v3.2", temperature=0.5),
            lambda: _try_get("cerebras", get_cerebras_llm, model="gpt-oss-120b", temperature=0.5),
            lambda: _try_get("zhipu", get_zhipu_llm, temperature=0.5),
        ]:
            result = llm()
            if result:
                return result

    # MVP Strategist: NVIDIA → Cerebras → Zhipu → Groq
    if role == "mvp_strategist":
        for llm in [
            lambda: _try_get("nvidia", get_nvidia_llm, model="qwen/qwen3.5-397b-a17b", temperature=0.6),
            lambda: _try_get("cerebras", get_cerebras_llm, model="gpt-oss-120b", temperature=0.6),
            lambda: _try_get("zhipu", get_zhipu_llm, temperature=0.6),
            lambda: _try_get("groq", get_groq_llm, model="llama-3.3-70b-versatile", temperature=0.6),
        ]:
            result = llm()
            if result:
                return result

    # QA Reviewer: Cerebras → Groq → NVIDIA → Zhipu
    if role == "qa_reviewer":
        for llm in [
            lambda: _try_get("cerebras", get_cerebras_llm, model="gpt-oss-120b", temperature=0.2),
            lambda: _try_get("groq", get_groq_llm, model="llama-3.3-70b-versatile", temperature=0.2),
            lambda: _try_get("nvidia", get_nvidia_llm, model="deepseek-ai/deepseek-v3.2", temperature=0.2),
            lambda: _try_get("zhipu", get_zhipu_llm, temperature=0.2),
        ]:
            result = llm()
            if result:
                return result

    # Data Engineer: Cerebras → NVIDIA → Groq → Zhipu
    if role == "data_engineer":
        for llm in [
            lambda: _try_get("cerebras", get_cerebras_llm, model="gpt-oss-120b", temperature=0.1),
            lambda: _try_get("nvidia", get_nvidia_llm, model="deepseek-ai/deepseek-v3.2", temperature=0.1),
            lambda: _try_get("groq", get_groq_llm, model="llama-3.3-70b-versatile", temperature=0.1),
            lambda: _try_get("zhipu", get_zhipu_llm, temperature=0.1),
        ]:
            result = llm()
            if result:
                return result

    # Organizer: Groq → Cerebras → Zhipu → NVIDIA
    if role == "project_organizer":
        for llm in [
            lambda: _try_get("groq", get_groq_llm, model="qwen/qwen3-32b", temperature=0.3),
            lambda: _try_get("cerebras", get_cerebras_llm, model="gpt-oss-120b", temperature=0.3),
            lambda: _try_get("zhipu", get_zhipu_llm, temperature=0.3),
            lambda: _try_get("nvidia", get_nvidia_llm, model="deepseek-ai/deepseek-v3.2", temperature=0.3),
        ]:
            result = llm()
            if result:
                return result

    # Narrative: Cerebras → Zhipu → NVIDIA → Groq
    if role == "narrative_content":
        for llm in [
            lambda: _try_get("cerebras", get_cerebras_llm, model="gpt-oss-120b", temperature=0.7),
            lambda: _try_get("zhipu", get_zhipu_llm, temperature=0.7),
            lambda: _try_get("nvidia", get_nvidia_llm, model="deepseek-ai/deepseek-v3.2", temperature=0.7),
            lambda: _try_get("groq", get_groq_llm, temperature=0.7),
        ]:
            result = llm()
            if result:
                return result

    # Verifier: Cerebras → Groq → NVIDIA → Zhipu
    if role == "verifier":
        for llm in [
            lambda: _try_get("cerebras", get_cerebras_llm, model="gpt-oss-120b", temperature=0.2),
            lambda: _try_get("groq", get_groq_llm, model="llama-3.3-70b-versatile", temperature=0.2),
            lambda: _try_get("nvidia", get_nvidia_llm, model="deepseek-ai/deepseek-v3.2", temperature=0.2),
            lambda: _try_get("zhipu", get_zhipu_llm, temperature=0.2),
        ]:
            result = llm()
            if result:
                return result

    # Default: cualquier provider disponible
    for llm in [
        lambda: _try_get("cerebras", get_cerebras_llm, temperature=0.5),
        lambda: _try_get("nvidia", get_nvidia_llm, temperature=0.5),
        lambda: _try_get("groq", get_groq_llm, temperature=0.5),
        lambda: _try_get("zhipu", get_zhipu_llm, temperature=0.5),
    ]:
        result = llm()
        if result:
            return result

    raise ValueError(f"Todos los providers están agotados. No hay LLM disponible para {role}.")


# ═══════════════════════════════════════════════════════
# SMART ROUTER — Elige modelo por contexto + rol
# ═══════════════════════════════════════════════════════

def estimate_tokens(text: str) -> int:
    """Estimación rápida de tokens (~4 chars = 1 token)."""
    return len(text) // 4


def get_llm_smart(role: str, task_text: str = "", context_size: int = 0):
    """
    Router inteligente (respeta providers agotados):
    - Si contexto > 200K tokens → Gemini (1M context)
    - Si tarea de código → Kimi K2.5 (NVIDIA)
    - Si tarea rápida/simple → Cerebras (0.3s)
    - Default → routing por rol con fallback completo
    """
    total_tokens = estimate_tokens(task_text) + context_size

    if total_tokens > 200_000:
        gemini = get_gemini_llm(temperature=0.5)
        if gemini:
            return gemini

    code_keywords = ["código", "code", "script", "debug", "función", "api", "endpoint",
                     "solidity", "rust", "python", "typescript", "smart contract"]
    is_code_task = any(kw in task_text.lower() for kw in code_keywords)
    if is_code_task and role != "code_architect":
        nvidia = _try_get("nvidia", get_nvidia_llm, model="moonshotai/kimi-k2.5", temperature=0.2)
        if nvidia:
            return nvidia

    reasoning_keywords = ["analiza", "razona", "estrategia", "plan", "diseña", "architecture",
                          "reasoning", "strategy", "evaluate", "compare"]
    is_reasoning_task = any(kw in task_text.lower() for kw in reasoning_keywords)
    if is_reasoning_task and role not in ("mvp_strategist", "code_architect"):
        nvidia_qwen = _try_get("nvidia", get_nvidia_llm, model="qwen/qwen3.5-397b-a17b", temperature=0.4)
        if nvidia_qwen:
            return nvidia_qwen

    if total_tokens < 5_000 and role not in ("research_analyst", "mvp_strategist"):
        cerebras = _try_get("cerebras", get_cerebras_llm, temperature=0.3)
        if cerebras:
            return cerebras

    # Fallback: routing por rol (ya tiene cadenas completas de 4 providers)
    return get_llm_for_role(role)


# ═══════════════════════════════════════════════════════
# VALIDACIÓN
# ═══════════════════════════════════════════════════════

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
