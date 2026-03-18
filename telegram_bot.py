import asyncio
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from zep_memory import get_memory
from dotenv import load_dotenv

# Cargar variables
load_dotenv()

# Token de tu bot de Telegram
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise ValueError("❌ TELEGRAM_BOT_TOKEN no encontrado en .env")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 *Agente DOF con Memoria*\n\n"
        "¡Hola! Soy tu agente con memoria persistente. "
        "Puedo recordar toda nuestra conversación.\n\n"
        "Comandos:\n"
        "/start - Iniciar\n"
        "/historial - Ver últimos mensajes\n"
        "/clear - Limpiar memoria",
        parse_mode="Markdown"
    )

async def historial(update: Update, context: ContextTypes.DEFAULT_TYPE):
    memory = get_memory()
    historial = await memory.get_recent_messages(10)
    
    if not historial:
        await update.message.reply_text("📭 No hay mensajes en el historial.")
        return
    
    response = "📋 *Últimos mensajes:*\n\n"
    for i, msg in enumerate(historial[:5], 1):
        role = "👤" if msg['role'] == "user" else "🤖"
        response += f"{i}. {role} {msg['content'][:100]}...\n"
    
    await update.message.reply_text(response, parse_mode="Markdown")

async def clear(update: Update, context: ContextTypes.DEFAULT_TYPE):
    memory = get_memory()
    await memory.clear_memory()
    await update.message.reply_text("🗑️ Memoria limpiada correctamente.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    user_id = str(update.effective_user.id)
    username = update.effective_user.first_name or "Usuario"
    
    try:
        # Obtener instancia de memoria
        memory = get_memory()
        
        # Guardar mensaje del usuario
        await memory.add_message("user", f"[{username}]: {user_message}")
        
        # Obtener contexto (últimos 10 mensajes)
        historial = await memory.get_recent_messages(10)
        
        # Generar respuesta con contexto
        respuesta = await generar_respuesta_con_contexto(user_message, historial, username)
        
        # Guardar respuesta
        await memory.add_message("assistant", respuesta)
        
        # Enviar respuesta
        await update.message.reply_text(respuesta)
        
    except Exception as e:
        print(f"❌ Error: {e}")
        await update.message.reply_text("⚠️ Ocurrió un error. Intenta de nuevo.")

async def generar_respuesta_con_contexto(mensaje, historial, username):
    """Genera una respuesta basada en el mensaje actual y el historial"""
    
    if not historial:
        return f"Hola {username}, ¿en qué puedo ayudarte?"
    
    # Extraer los últimos mensajes relevantes
    ultimos = []
    for msg in historial[:5]:
        if msg['role'] == "user":
            ultimos.append(f"Usuario dijo: {msg['content']}")
        else:
            ultimos.append(f"Asistente respondió: {msg['content']}")
    
    contexto = "\n".join(reversed(ultimos))
    
    # Respuesta simple pero contextual
    return f"**{username}**, gracias por tu mensaje. Basado en nuestra conversación anterior, procesé: '{mensaje}'"

def main():
    print("🚀 Iniciando bot de Telegram...")
    print(f"🔧 Token: {TOKEN[:10]}...")
    
    # Crear aplicación
    app = Application.builder().token(TOKEN).build()
    
    # Añadir handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("historial", historial))
    app.add_handler(CommandHandler("clear", clear))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("✅ Bot iniciado correctamente!")
    app.run_polling()

if __name__ == "__main__":
    main()
