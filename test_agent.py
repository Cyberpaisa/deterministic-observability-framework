#!/usr/bin/env python3
import sys
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

print("🤖 DOF Agent #1686 - Modo interactivo")
print("⚡ Escribe tu mensaje (o 'salir' para terminar)")
print("-" * 50)

while True:
    try:
        user_input = input("\n👤 Tú: ").strip()
        if user_input.lower() in ['salir', 'exit', 'quit']:
            break
        if not user_input:
            continue
            
        print("🤖 Agente pensando...", end="", flush=True)
        
        # Usar Mistral API (gratis)
        headers = {
            "Authorization": f"Bearer {os.getenv('MISTRAL_API_KEY')}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": "mistral-small-latest",
            "messages": [{"role": "user", "content": user_input}],
            "temperature": 0.7
        }
        
        response = requests.post(
            "https://api.mistral.ai/v1/chat/completions",
            headers=headers,
            json=data,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            answer = result['choices'][0]['message']['content']
            print(f"\r🤖 Agente: {answer}")
        else:
            print(f"\r❌ Error: {response.status_code}")
            
    except KeyboardInterrupt:
        break
    except Exception as e:
        print(f"\r❌ Error: {e}")

print("\n👋 ¡Hasta luego!")
