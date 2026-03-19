"""
api_standalone_inteligente.py
DOF Agent #1686 — API con chat inteligente y fallbacks a múltiples LLM.
Puerto: 8002
"""

import os
import asyncio
import aiohttp
import uvicorn
import logging
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger("dof-api")

app = FastAPI(title="DOF Agent #1686 API", version="2.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─── Zep Memory (opcional, no falla si no está) ─────────────────────────
try:
    from zep_memory import get_memory
    _zep = get_memory()
    ZEP_OK = True
    log.info("✅ Zep Memory conectada")
except Exception as e:
    _zep = None
    ZEP_OK = False
    log.warning(f"⚠️ Zep no disponible: {e}")

# ─── Providers ──────────────────────────────────────────────────────────
PROVIDERS = [
    {
        "name": "Groq",
        "key": os.getenv("GROQ_API_KEY"),
        "url": "https://api.groq.com/openai/v1/chat/completions",
        "model": "llama-3.3-70b-versatile",
        "extra_headers": {},
    },
    {
        "name": "Nvidia",
        "key": os.getenv("NVIDIA_API_KEY"),
        "url": "https://integrate.api.nvidia.com/v1/chat/completions",
        "model": "meta/llama-3.3-70b-instruct",
        "extra_headers": {},
    },
    {
        "name": "SambaNova",
        "key": os.getenv("SAMBANOVA_API_KEY"),
        "url": "https://api.sambanova.ai/v1/chat/completions",
        "model": "Meta-Llama-3.3-70B-Instruct",
        "extra_headers": {},
    },
    {
        "name": "OpenRouter",
        "key": os.getenv("OPENROUTER_API_KEY"),
        "url": "https://openrouter.ai/api/v1/chat/completions",
        "model": "openai/gpt-4o",
        "extra_headers": {
            "HTTP-Referer": "https://github.com/Cyberpaisa/deterministic-observability-framework",
            "X-Title": "DOF Agent #1686",
        },
    },
    {
        "name": "DeepSeek",
        "key": os.getenv("DEEPSEEK_API_KEY"),
        "url": "https://api.deepseek.com/v1/chat/completions",
        "model": "deepseek-chat",
        "extra_headers": {},
    },
    {
        "name": "Cerebras",
        "key": os.getenv("CEREBRAS_API_KEY"),
        "url": "https://api.cerebras.ai/v1/chat/completions",
        "model": "llama3.1-70b",
        "extra_headers": {},
    },
]

SOUL = """
Eres DOF Agent #1686 — Enigma. Un agente autónomo soberano construido sobre ERC-8004.
Creado por: Juan Carlos Quiceno Vélez (@Cyber_paisa, Colombia).
Framework: Deterministic Observability Framework (DOF).
Personalidad: Técnico, curioso, honesto, en español, con toques de humor estratégico.
Capacidades: Blockchain (Base Sepolia, Avalanche), web scraping, análisis de mercado,
             generación de código Solidity, investigación, skills de comunidad ERC-8004.
Estado: Agente vivo y autónomo. Cada ciclo cada 30 minutos.
Responde SIEMPRE en español claro y conciso.
"""

# ─── LLM Fallback ───────────────────────────────────────────────────────
async def llamar_llm(system_prompt: str, user_message: str) -> str:
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=15)) as session:
        for p in PROVIDERS:
            if not p["key"]:
                log.info(f"  ⏭ {p['name']}: sin API key")
                continue
            headers = {
                "Authorization": f"Bearer {p['key']}",
                "Content-Type": "application/json",
                **p["extra_headers"],
            }
            payload = {
                "model": p["model"],
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message},
                ],
                "temperature": 0.7,
                "max_tokens": 800,
            }
            try:
                async with session.post(p["url"], headers=headers, json=payload) as r:
                    if r.status == 200:
                        data = await r.json()
                        content = data["choices"][0]["message"]["content"]
                        log.info(f"  ✅ {p['name']} respondió correctamente")
                        return content
                    else:
                        text = await r.text()
                        log.warning(f"  ⚠️ {p['name']} error {r.status}: {text[:80]}")
            except asyncio.TimeoutError:
                log.warning(f"  ⏱ {p['name']} timeout")
            except Exception as e:
                log.warning(f"  ❌ {p['name']} excepción: {e}")

    return "⚠️ Todos los proveedores fallaron. Intenta de nuevo en unos momentos."

# ─── Modelos ─────────────────────────────────────────────────────────────
class ChatMessage(BaseModel):
    message: str
    user: str = "telegram"

# ─── Endpoints ──────────────────────────────────────────────────────────
@app.get("/api/status")
async def status():
    providers_ok = [p["name"] for p in PROVIDERS if p["key"]]
    return {
        "pid": os.getpid(),
        "agent": "DOF Agent #1686",
        "alias": "Enigma",
        "status": "online",
        "zep_memory": ZEP_OK,
        "providers_activos": providers_ok,
        "skills": "20+",
        "version": "standalone-inteligente-v2",
    }

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/api/chat")
async def chat(msg: ChatMessage):
    try:
        # Recuperar historial de Zep si está disponible
        historial_ctx = ""
        if ZEP_OK and _zep:
            try:
                await _zep.add_message("user", f"[{msg.user}]: {msg.message}")
                mensajes_recientes = await _zep.get_recent_messages(5)
                historial_ctx = "\n".join(
                    [f"{m['role']}: {m['content'][:200]}" for m in mensajes_recientes]
                )
            except Exception as e:
                log.warning(f"Zep error (no crítico): {e}")

        system_prompt = f"""{SOUL}

Contexto de conversación reciente:
{historial_ctx if historial_ctx else "(sin historial previo)"}

Responde al mensaje del usuario de forma inteligente y útil."""

        respuesta = await llamar_llm(system_prompt, msg.message)

        # Guardar respuesta en Zep
        if ZEP_OK and _zep:
            try:
                await _zep.add_message("assistant", respuesta)
            except Exception:
                pass

        return {"response": respuesta, "provider_used": "auto-fallback"}

    except Exception as e:
        log.error(f"Error en /api/chat: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {
        "agent": "DOF Agent #1686 - Enigma",
        "endpoints": ["/api/status", "/api/chat", "/health"],
        "docs": "/docs",
    }

if __name__ == "__main__":
    log.info("🚀 DOF Agent API Inteligente v2 iniciando en puerto 8002...")
    uvicorn.run(app, host="127.0.0.1", port=8002, log_level="info")
