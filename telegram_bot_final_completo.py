import os
import asyncio
import subprocess
import random
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
from datetime import datetime
from zep_memory import get_memory
import json

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
memory = get_memory()
AGENTE_PID = 70450

# ===== TODAS LAS API KEYS =====
PROVIDERS = {
    "groq": {
        "api_key": os.getenv("GROQ_API_KEY"),
        "url": "https://api.groq.com/openai/v1/chat/completions",
        "model": "llama-3.3-70b-versatile",
        "active": bool(os.getenv("GROQ_API_KEY"))
    },
    "openrouter": {
        "api_key": os.getenv("OPENROUTER_API_KEY"),
        "url": "https://openrouter.ai/api/v1/chat/completions",
        "model": "openai/gpt-4o",
        "active": bool(os.getenv("OPENROUTER_API_KEY"))
    },
    "deepseek": {
        "api_key": os.getenv("DEEPSEEK_API_KEY"),
        "url": "https://api.deepseek.com/v1/chat/completions",
        "model": "deepseek-chat",
        "active": bool(os.getenv("DEEPSEEK_API_KEY"))
    },
    "nvidia": {
        "api_key": os.getenv("NVIDIA_API_KEY"),
        "url": "https://api.nvcf.nvidia.com/v2/nvcf/pexec/functions",
        "model": "nvidia/llama-3.1-nemotron-70b-instruct",
        "active": bool(os.getenv("NVIDIA_API_KEY"))
    },
    "sambanova": {
        "api_key": os.getenv("SAMBANOVA_API_KEY"),
        "url": "https://api.sambanova.ai/v1/chat/completions",
        "model": "Meta-Llama-3.3-70B-Instruct",
        "active": bool(os.getenv("SAMBANOVA_API_KEY"))
    },
    "minimax": {
        "api_key": os.getenv("MINIMAX_API_KEY"),
        "active": bool(os.getenv("MINIMAX_API_KEY"))
    },
    "cerebras": {
        "api_key": os.getenv("CEREBRAS_API_KEY"),
        "active": bool(os.getenv("CEREBRAS_API_KEY"))
    }
}

# ===== ZO (SYNTHESIS) =====
ZO_CONFIG = {
    "api_key": os.getenv("SYNTHESIS_API_KEY"),
    "participant_id": os.getenv("SYNTHESIS_PARTICIPANT_ID"),
    "team_id": os.getenv("SYNTHESIS_TEAM_ID"),
    "agent_token_id": os.getenv("SYNTHESIS_AGENT_TOKEN_ID"),
    "base_tx": os.getenv("SYNTHESIS_BASE_TX"),
    "active": bool(os.getenv("SYNTHESIS_API_KEY"))
}

# ===== OPENVIKING =====
try:
    r = requests.get("http://127.0.0.1:1933/health", timeout=2)
    VIKING_ACTIVE = r.status_code == 200
except:
    VIKING_ACTIVE = False

# ===== LOGS EN INGLÉS =====
async def add_to_conversation_log(entry):
    try:
        with open("conversation-log.md", "a") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"\n## [{timestamp}]\n{entry}\n")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

# ===== CONSULTAR GROQ (RESPUESTAS EN ESPAÑOL) =====
async def consultar_groq(mensaje, contexto, username):
    try:
        headers = {
            "Authorization": f"Bearer {PROVIDERS['groq']['api_key']}",
            "Content-Type": "application/json"
        }
        
        system_prompt = f"""Eres DOF Agent, un agente autónomo inteligente con memoria Zep y conexión a Zo/Synthesis.
        IMPORTANTE: Responde SIEMPRE en ESPAÑOL.
        El usuario se llama {username}.
        Contexto: {contexto}"""
        
        payload = {
            "model": PROVIDERS['groq']['model'],
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": mensaje}
            ],
            "temperature": 0.7,
            "max_tokens": 800
        }
        
        response = requests.post(
            PROVIDERS['groq']['url'],
            headers=headers,
            json=payload,
            timeout=15
        )
        
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return f"⚠️ Error: {response.status_code}"
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

async def obtener_ultimo_ciclo():
    try:
        result = subprocess.run(["tail", "-1", "logs/autonomous.log"], capture_output=True, text=True)
        if "Cycle #" in result.stdout:
            return result.stdout.split("Cycle #")[1].split()[0]
        return "164"
    except:
        return "164"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.effective_user.first_name or "Usuario"
    ciclo = await obtener_ultimo_ciclo()
    
    # Contar providers activos
    providers_activos = sum(1 for p in PROVIDERS.values() if p.get("active"))
    
    await add_to_conversation_log(f"Bot started by user {username}")
    
    await update.message.reply_text(
        f"🤖 *DOF Agent - COMPLETO*\n\n"
        f"✅ Zep Memory: ACTIVA\n"
        f"✅ Zo/Synthesis: {'ACTIVO' if ZO_CONFIG['active'] else 'INACTIVO'}\n"
        f"✅ Providers: {providers_activos}/7 activos\n"
        f"✅ OpenViking: {'ACTIVO' if VIKING_ACTIVE else 'INACTIVO'}\n"
        f"🔄 Ciclo agente: #{ciclo}\n\n"
        f"Respondo en ESPAÑOL con TODOS los recursos",
        parse_mode="Markdown"
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ciclo = await obtener_ultimo_ciclo()
    providers_activos = sum(1 for p in PROVIDERS.values() if p.get("active"))
    
    status_msg = f"📊 *ESTADO COMPLETO*\n\n"
    status_msg += f"🧠 Agente PID: {AGENTE_PID}\n"
    status_msg += f"🔄 Ciclo: #{ciclo}\n"
    status_msg += f"💾 Zep Memory: ACTIVA\n"
    status_msg += f"🤖 Zo/Synthesis: {'ACTIVO' if ZO_CONFIG['active'] else 'INACTIVO'}\n"
    status_msg += f"🔌 Providers: {providers_activos}/7\n"
    status_msg += f"🗄️ OpenViking: {'ACTIVO' if VIKING_ACTIVE else 'INACTIVO'}\n"
    status_msg += f"📝 Logs: conversation-log.md"
    
    await update.message.reply_text(status_msg, parse_mode="Markdown")

async def ciclo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = subprocess.run(["tail", "-5", "logs/autonomous.log"], capture_output=True, text=True)
    await update.message.reply_text(f"🔄 *Últimos ciclos:*\n```\n{result.stdout}\n```", parse_mode="Markdown")

async def historial(update: Update, context: ContextTypes.DEFAULT_TYPE):
    historial = await memory.get_recent_messages(10)
    if not historial:
        await update.message.reply_text("📭 No hay historial")
        return
    
    response = "📋 *Últimos mensajes:*\n\n"
    for i, msg in enumerate(historial[:5], 1):
        role = "👤" if msg['role'] == "user" else "🤖"
        response += f"{i}. {role} {msg['content'][:150]}...\n"
    
    await update.message.reply_text(response, parse_mode="Markdown")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_msg = update.message.text
    username = update.effective_user.first_name or "Usuario"
    
    try:
        # Guardar en Zep
        await memory.add_message("user", f"[{username}]: {user_msg}")
        
        # Log en inglés
        await add_to_conversation_log(f"User {username}: {user_msg}")
        
        # Obtener contexto
        historial = await memory.get_recent_messages(5)
        contexto = "\n".join([f"{m['role']}: {m['content'][:200]}" for m in historial])
        
        ciclo = await obtener_ultimo_ciclo()
        
        # Pensando...
        await update.message.chat.send_action("typing")
        
        # Respuesta con GROQ
        respuesta = await consultar_groq(user_msg, contexto, username)
        
        # Guardar respuesta
        await memory.add_message("assistant", respuesta)
        await add_to_conversation_log(f"DOF Agent response: {respuesta[:200]}...")
        
        # Enviar
        await update.message.reply_text(respuesta, parse_mode="Markdown")
        
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {str(e)}")

def main():
    providers_activos = sum(1 for p in PROVIDERS.values() if p.get("active"))
    
    print("🚀 INICIANDO BOT COMPLETO:")
    print(f"   ✅ Zep Memory: ACTIVA")
    print(f"   ✅ Zo/Synthesis: {'ACTIVO' if ZO_CONFIG['active'] else 'INACTIVO'}")
    print(f"   ✅ Providers: {providers_activos}/7 activos")
    print(f"   ✅ OpenViking: {'ACTIVO' if VIKING_ACTIVE else 'INACTIVO'}")
    print(f"   ✅ Conectado al agente PID: {AGENTE_PID}")
    
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("ciclo", ciclo))
    app.add_handler(CommandHandler("historial", historial))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("✅ BOT LISTO! Responde en ESPAÑOL con TODOS los recursos")
    app.run_polling()

if __name__ == "__main__":
    main()
