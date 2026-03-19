import os
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
API_URL = "http://127.0.0.1:8002"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 *DOF Agent - Conectado a API*\n\n"
        "✅ Usando API standalone\n"
        "✅ Responde INMEDIATAMENTE",
        parse_mode="Markdown"
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        r = requests.get(f"{API_URL}/api/status", timeout=2)
        data = r.json()
        await update.message.reply_text(
            f"📊 *API Status*\nPID: {data['pid']}\nMemoria: {data['memory']}",
            parse_mode="Markdown"
        )
    except:
        await update.message.reply_text("❌ API no disponible")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_msg = update.message.text
    
    try:
        r = requests.post(
            f"{API_URL}/api/chat",
            json={"message": user_msg, "user": "telegram"},
            timeout=5
        )
        respuesta = r.json().get("response", "✅ Procesado")
    except:
        respuesta = "⚠️ Error conectando a la API"
    
    await update.message.reply_text(respuesta, parse_mode="Markdown")

def main():
    print("🚀 Iniciando bot con API standalone...")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("✅ Bot listo!")
    app.run_polling()

if __name__ == "__main__":
    main()
