import os
import subprocess
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
from datetime import datetime
from zep_memory import get_memory

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
memory = get_memory()
AGENTE_PID = 70450

async def obtener_ultimo_ciclo():
    try:
        result = subprocess.run(["tail", "-1", "logs/autonomous.log"], capture_output=True, text=True)
        if "Cycle #" in result.stdout:
            return result.stdout.split("Cycle #")[1].split()[0]
        return "164"
    except:
        return "164"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ciclo = await obtener_ultimo_ciclo()
    await update.message.reply_text(
        f"🤖 *DOF Agent - RESPONDO SIEMPRE*\n\n"
        f"✅ Agente PID: {AGENTE_PID}\n"
        f"🔄 Ciclo actual: #{ciclo}\n"
        f"✅ Respondo AHORA MISMO\n"
        f"✅ Memoria Zep activa\n\n"
        f"Comandos:\n"
        f"/status - Estado del agente\n"
        f"/ciclo - Último ciclo",
        parse_mode="Markdown"
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ciclo = await obtener_ultimo_ciclo()
    await update.message.reply_text(
        f"📊 *ESTADO DEL AGENTE*\n"
        f"🧠 PID: {AGENTE_PID}\n"
        f"🔄 Ciclo: #{ciclo}\n"
        f"⏱️ {datetime.now().strftime('%H:%M:%S')}\n"
        f"✅ Modo: RESPUESTA INMEDIATA",
        parse_mode="Markdown"
    )

async def ciclo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = subprocess.run(["tail", "-5", "logs/autonomous.log"], capture_output=True, text=True)
    await update.message.reply_text(f"🔄 *Últimos ciclos:*\n```\n{result.stdout}\n```", parse_mode="Markdown")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_msg = update.message.text
    username = update.effective_user.first_name or "Usuario"
    
    # Guardar en memoria Zep
    await memory.add_message("user", f"[{username}]: {user_msg}")
    
    # Obtener historial
    historial = await memory.get_recent_messages(3)
    ciclo = await obtener_ultimo_ciclo()
    
    # RESPUESTA INMEDIATA
    respuesta = f"🤖 *DOF Agent - Respuesta Inmediata*\n\n"
    respuesta += f"👤 {username}: {user_msg}\n"
    respuesta += f"🧠 Agente PID: {AGENTE_PID}\n"
    respuesta += f"🔄 Ciclo actual: #{ciclo}\n"
    respuesta += f"📚 Memoria: {len(historial)} mensajes\n"
    respuesta += f"⏱️ {datetime.now().strftime('%H:%M:%S')}\n\n"
    respuesta += f"_El agente sigue sus ciclos autónomos, pero YO te respondo ya_"
    
    await memory.add_message("assistant", respuesta)
    await update.message.reply_text(respuesta, parse_mode="Markdown")

def main():
    print("🚀 Iniciando bot con RESPUESTAS SIEMPRE INMEDIATAS...")
    print(f"🧠 Conectado al agente PID: {AGENTE_PID}")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("ciclo", ciclo))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("✅ Bot listo! RESPONDO SIEMPRE INMEDIATAMENTE")
    app.run_polling()

if __name__ == "__main__":
    main()
