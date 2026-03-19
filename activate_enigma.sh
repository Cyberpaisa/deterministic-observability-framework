#!/bin/bash

# MAESTRO DE ACTIVACIÓN ENIGMA #1686
# Este script levanta el Cerebro, el Dashboard y el Bot de Telegram de forma simultánea.

echo "🧠 Despertando a Enigma..."

# 1. Cargar Variables de Entorno
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
    echo "✅ Variables de entorno cargadas."
fi

# 2. Iniciar el Cerebro Autónomo (Loop v2)
echo "🧬 Iniciando Cerebro Autónomo..."
nohup python3 autonomous_loop_v2.py > logs/brain.log 2>&1 &
echo $! > .pid_brain

# 3. Iniciar el Dashboard (API Server)
echo "📊 Iniciando Dashboard API..."
nohup python3 api/server.py > logs/api.log 2>&1 &
echo $! > .pid_api

# 4. Iniciar el Bot de Telegram
echo "🤖 Iniciando Bot de Telegram..."
nohup python3 interfaces/telegram_bot.py > logs/telegram.log 2>&1 &
echo $! > .pid_telegram

echo "🚀 ENIGMA ESTÁ ACTIVO Y SOBERANO."
echo "Ruta: $(pwd)"
echo "Logs: tail -f logs/brain.log"
