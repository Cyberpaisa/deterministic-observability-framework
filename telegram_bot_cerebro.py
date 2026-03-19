import os
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CEREBRO_API = "http://127.0.0.1:8002"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 *DOF Agent - Conectado al CEREBRO REAL*\n\n"
        "✅ Consultando al agente autónomo\n"
        "✅ Respuestas INTELIGENTES",
        parse_mode="Markdown"
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        r = requests.get(f"{CEREBRO_API}/api/status", timeout=2)
        data = r.json()
        await update.message.reply_text(
            f"📊 *ESTADO DEL CEREBRO*\n"
            f"🧠 PID: {data['pid']}\n"
            f"🔄 Ciclo: #{data.get('ultimo_ciclo', 'N/A')}\n"
            f"💾 Skills: {data.get('skills', '20+')}",
            parse_mode="Markdown"
        )
    except Exception as e:
        await update.message.reply_text(f"❌ Cerebro no disponible: {str(e)[:50]}")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_msg = update.message.text
    
    try:
        # Consultar al CEREBRO REAL
        r = requests.post(
            f"{CEREBRO_API}/api/chat",
            json={"message": user_msg, "user": "telegram"},
            timeout=5
        )
        if r.status_code == 200:
            respuesta = r.json().get("response", "✅ Procesado por el cerebro")
        else:
            respuesta = f"❌ Error {r.status_code}"
    except Exception as e:
        respuesta = f"⚠️ Error conectando al cerebro: {str(e)[:50]}"
    
    await update.message.reply_text(respuesta, parse_mode="Markdown")

def main():
    print("🚀 Iniciando bot conectado al CEREBRO REAL (puerto 8002)...")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("✅ Bot listo! Conectado al agente autónomo")
    app.run_polling()

if __name__ == "__main__":
    main()
