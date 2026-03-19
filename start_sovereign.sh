#!/bin/bash
echo "🚀 Iniciando Ecosistema Soberano DOF & Enigma..."

# 1. Iniciar Ollama (asegurar que esté corriendo)
open -a Ollama

# 2. Iniciar el Loop Autónomo (Cerebro)
nohup python3 autonomous_loop_v2.py > logs/autonomous_loop.log 2>&1 &
echo "🧠 Cerebro (Loop v2) iniciado en segundo plano."

# 3. Iniciar el Dashboard (Front-End) - Si no está corriendo
# Suponiendo que el usuario lo lanzará manualmente o ya está en el puerto 3001
echo "🖥️ Dashboard disponible en http://localhost:3001"

# 4. Iniciar el Bot de Telegram (Interfaz)
nohup python3 interfaces/telegram_bot.py > logs/telegram_bot.log 2>&1 &
echo "🤖 Bot de Telegram iniciado en segundo plano."

echo "✅ Sistema fully operational. Soberanía activada."
