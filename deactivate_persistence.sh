#!/bin/bash

# DESACTIVADOR DE PERSISTENCIA ENIGMA
# Este script detiene los procesos y elimina el auto-arranque.

echo "🛑 Deteniendo la persistencia de Enigma..."

# 1. Descargar el agente de macOS
if [ -f ~/Library/LaunchAgents/com.enigma.agent.plist ]; then
    launchctl unload ~/Library/LaunchAgents/com.enigma.agent.plist
    rm ~/Library/LaunchAgents/com.enigma.agent.plist
    echo "✅ Auto-arranque de macOS eliminado."
fi

# 2. Matar procesos activos si existen
echo "💀 Matando procesos residuales..."
pkill -f autonomous_loop_v2.py
pkill -f api/server.py
pkill -f interfaces/telegram_bot.py

# 3. Limpiar PIDs
rm -f .pid_brain .pid_api .pid_telegram

echo "🤫 Enigma ha sido desactivado y desligado del sistema."
