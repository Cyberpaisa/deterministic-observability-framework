import asyncio
import os
import subprocess
import re
from datetime import datetime
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

# Variable global para permisos
PERMISO_ENV = False

async def add_to_conversation_log(entry):
    """Añade entrada al conversation-log.md"""
    try:
        with open("conversation-log.md", "a") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"\n## [{timestamp}]\n{entry}\n")
        print(f"📝 Log añadido a conversation-log.md")
        return True
    except Exception as e:
        print(f"❌ Error en conversation-log: {e}")
        return False

async def add_to_journal(entry):
    """Añade entrada al journal.md"""
    try:
        with open("journal.md", "a") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"\n- [{timestamp}] {entry}")
        print(f"📝 Entrada añadida a journal.md")
        return True
    except Exception as e:
        print(f"❌ Error en journal: {e}")
        return False

async def check_permission_env(user_message):
    """Verifica si el usuario dio permiso explícito para modificar .env"""
    global PERMISO_ENV
    
    permiso_patterns = [
        r"te doy permiso (para|de) modificar .env",
        r"puedes cambiar el .env",
        r"autorizo cambio en .env",
        r"permiso para editar .env",
        r"ajusta el .env",
    ]
    
    for pattern in permiso_patterns:
        if re.search(pattern, user_message.lower()):
            PERMISO_ENV = True
            await add_to_conversation_log(f"Usuario dio permiso para modificar .env")
            await add_to_journal("Permiso concedido para modificar .env")
            return True, "✅ Permiso concedido para modificar .env"
    
    return False, "❌ No tienes permiso para modificar .env. Debes autorizarlo explícitamente."

async def modify_env(variable, value):
    """Modifica el archivo .env SOLO si hay permiso"""
    global PERMISO_ENV
    
    if not PERMISO_ENV:
        return False, "No tengo permiso para modificar .env. Necesitas autorizarme primero."
    
    try:
        with open(".env", "r") as f:
            lines = f.readlines()
        
        found = False
        for i, line in enumerate(lines):
            if line.startswith(f"{variable}="):
                lines[i] = f"{variable}={value}\n"
                found = True
                break
        
        if not found:
            lines.append(f"{variable}={value}\n")
        
        with open(".env", "w") as f:
            f.writelines(lines)
        
        log_msg = f"🔧 .env modificado: {variable} actualizada"
        await add_log_to_readme(log_msg)
        await add_to_conversation_log(log_msg)
        await add_to_journal(f"Modifiqué .env: {variable}={value}")
        
        return True, f"✅ Variable {variable} actualizada en .env"
        
    except Exception as e:
        return False, f"❌ Error modificando .env: {e}"

async def add_log_to_readme(log_message):
    """Añade un log al final del README.md"""
    try:
        with open("README.md", "a") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"\n- [{timestamp}] {log_message}")
        return True
    except Exception as e:
        print(f"❌ Error añadiendo log: {e}")
        return False

async def make_commit(commit_message):
    """Hace commit de los cambios SOLO de archivos seguros"""
    try:
        # Solo agregar archivos específicos y seguros
        archivos_seguros = ["README.md", "journal.md", "conversation-log.md", ".env"]
        for archivo in archivos_seguros:
            if os.path.exists(archivo):
                subprocess.run(["git", "add", archivo], check=False)
        
        result = subprocess.run(
            ["git", "commit", "-m", commit_message],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print(f"✅ Commit hecho: {commit_message}")
            return True
        else:
            print(f"⚠️ No hay cambios para commit: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Error en commit: {e}")
        return False

async def procesar_orden_con_permisos(user_message):
    """Procesa órdenes verificando permisos"""
    
    tiene_permiso, mensaje = await check_permission_env(user_message)
    if tiene_permiso:
        return mensaje
    
    env_pattern = r"cambia .env:?\s*(\w+)=(.+)"
    match = re.search(env_pattern, user_message, re.IGNORECASE)
    
    if match:
        variable, valor = match.groups()
        success, result = await modify_env(variable, valor)
        return result
    
    return None

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 *Agente DOF con Memoria*\n\n"
        "¡Hola! Soy tu agente con memoria persistente.\n\n"
        "Comandos especiales:\n"
        "/start - Iniciar\n"
        "/historial - Ver últimos mensajes\n"
        "/clear - Limpiar memoria\n\n"
        "Para modificar .env:\n"
        "1. Primero da permiso: 'te doy permiso para modificar .env'\n"
        "2. Luego: 'cambia .env: VARIABLE=valor'",
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

async def generar_respuesta_con_contexto(mensaje, historial, username):
    if not historial:
        return f"Hola {username}, ¿en qué puedo ayudarte?"
    
    ultimos = []
    for msg in historial[:5]:
        if msg['role'] == "user":
            ultimos.append(f"Usuario dijo: {msg['content']}")
        else:
            ultimos.append(f"Asistente respondió: {msg['content']}")
    
    return f"**{username}**, gracias por tu mensaje. Procesé: '{mensaje}'"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    username = update.effective_user.first_name or "Usuario"
    
    try:
        memory = get_memory()
        await memory.add_message("user", f"[{username}]: {user_message}")
        
        respuesta_permiso = await procesar_orden_con_permisos(user_message)
        
        if respuesta_permiso:
            respuesta = respuesta_permiso
        else:
            historial = await memory.get_recent_messages(10)
            respuesta = await generar_respuesta_con_contexto(user_message, historial, username)
        
        # Añadir logs a todos los archivos
        await add_log_to_readme(f"Usuario {username}: {user_message[:50]}...")
        await add_to_conversation_log(f"Usuario {username}: {user_message}")
        await add_to_journal(f"Procesé mensaje de {username}")
        
        # Hacer commit automático solo de archivos seguros
        await make_commit(f"Auto-commit: Interacción con {username}")
        
        await memory.add_message("assistant", respuesta)
        await update.message.reply_text(respuesta)
        
    except Exception as e:
        print(f"❌ Error: {e}")
        await update.message.reply_text("⚠️ Ocurrió un error.")

def main():
    print("🚀 Iniciando bot de Telegram...")
    print(f"🔧 Token: {TOKEN[:10]}...")
    
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("historial", historial))
    app.add_handler(CommandHandler("clear", clear))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("✅ Bot iniciado correctamente!")
    app.run_polling()

if __name__ == "__main__":
    main()
