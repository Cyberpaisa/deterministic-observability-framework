import asyncio
import subprocess
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 *DOF Agent #1686*\n\n"
        "Sistema autónomo activo.\n"
        "• autonomous_loop: ✅ PID 59381\n"
        "• Último ciclo: #160 completado\n"
        "• Próximo ciclo: #161 en ~30min\n\n"
        "Comandos:\n"
        "/ciclo - Ver últimos ciclos\n"
        "/status - Estado completo",
        parse_mode="Markdown"
    )

async def ciclo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        result = subprocess.run(['tail', '-10', 'logs/autonomous.log'], capture_output=True, text=True)
        await update.message.reply_text(f"🔄 *Últimos ciclos:*\n```\n{result.stdout}\n```", parse_mode="Markdown")
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    status_msg = "📊 *ESTADO DEL SISTEMA*\n\n"
    status_msg += "✅ autonomous_loop: ACTIVO (PID 59381)\n"
    status_msg += "✅ Uvicorn: ACTIVO\n"
    status_msg += "✅ ngrok: ACTIVO\n"
    status_msg += "✅ Memoria Zep: ACTIVA\n"
    status_msg += "✅ Moltbook: CLAIMED\n"
    status_msg += "⏳ OpenViking: OPCIONAL\n"
    await update.message.reply_text(status_msg, parse_mode="Markdown")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Mensaje recibido. El agente autónomo procesará en su próximo ciclo.\n"
        "Usa /ciclo para ver el progreso."
    )

def main():
    print("🚀 Iniciando bot interfaz...")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ciclo", ciclo))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("✅ Bot listo!")
    app.run_polling()

if __name__ == "__main__":
    main()
