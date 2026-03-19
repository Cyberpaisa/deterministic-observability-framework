import os
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
API_URL = "http://127.0.0.1:8001"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 *DOF Agent - CONECTADO AL CEREBRO*\n\n"
        "✅ Responde INMEDIATAMENTE\n"
        "✅ Usa la inteligencia del agente\n"
        "✅ Memoria Zep activa\n\n"
        "Comandos:\n"
        "/status - Ver estado del cerebro",
        parse_mode="Markdown"
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        r = requests.get(f"{API_URL}/api/status", timeout=2)
        data = r.json()
        await update.message.reply_text(
            f"📊 *ESTADO DEL CEREBRO*\n"
            f"🧠 PID: {data['pid']}\n"
            f"✅ Conectado vía API",
            parse_mode="Markdown"
        )
    except:
        await update.message.reply_text("❌ Error conectando al cerebro")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_msg = update.message.text
    
    try:
        # Consultar al agente vía API
        r = requests.post(
            f"{API_URL}/api/chat",
            json={"message": user_msg, "user": "telegram"},
            timeout=5
        )
        
        if r.status_code == 200:
            respuesta = r.json().get("response", "✅ Procesado")
        else:
            respuesta = "❌ Error en el agente"
            
    except Exception as e:
        respuesta = f"⚠️ Error: {str(e)[:50]}"
    
    await update.message.reply_text(respuesta, parse_mode="Markdown")

def main():
    print("🚀 Iniciando bot conectado al agente...")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("✅ Bot listo! Conectado al agente PID 70450")
    app.run_polling()

if __name__ == "__main__":
    main()
