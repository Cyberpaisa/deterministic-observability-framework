import os
import requests
import time
import threading
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHAT_ID = int(os.getenv('TELEGRAM_CHAT_ID'))  # Tu chat ID es 1353800773

def procesar_mensaje(texto):
    texto = texto.lower()
    if 'hola' in texto or 'activo' in texto:
        return "¡Sí, estoy activo! Soy tu agente DOF. ¿En qué puedo ayudarte?"
    elif 'quién eres' in texto or 'quien eres' in texto:
        return "Soy DOF v4, un agente autónomo con DeepSeek, RapidAPI y Moltbook."
    elif 'api' in texto:
        return "Todas mis APIs funcionan: DeepSeek, RapidAPI (Reddit) y Moltbook."
    elif 'gracias' in texto:
        return "¡De nada! 😊"
    else:
        return f"Recibí: '{texto}'. Por ahora solo respondo a mensajes simples."

def escuchar_telegram():
    print("👂 Bridge de Telegram iniciado...")
    last_id = 0
    
    while True:
        try:
            url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
            params = {'offset': last_id + 1, 'timeout': 30}
            
            r = requests.get(url, params=params, timeout=35)
            data = r.json()
            
            if data['ok'] and data['result']:
                for update in data['result']:
                    msg = update['message'].get('text', '')
                    chat = update['message']['chat']['id']
                    name = update['message']['from'].get('first_name', 'Usuario')
                    
                    print(f'📩 {name} dice: "{msg}"')
                    
                    if chat == CHAT_ID:
                        respuesta = procesar_mensaje(msg)
                        url2 = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
                        requests.post(url2, data={
                            'chat_id': chat,
                            'text': respuesta
                        })
                        print(f'✅ Respondido: "{respuesta}"')
                    
                    last_id = update['update_id']
                    
        except Exception as e:
            print(f'❌ Error: {e}')
            time.sleep(5)

if __name__ == "__main__":
    print("🚀 Bridge Telegram activo. Envía mensajes a tu bot.")
    print("Chat ID configurado:", CHAT_ID)
    print("Presiona Ctrl+C para detener.")
    
    thread = threading.Thread(target=escuchar_telegram, daemon=True)
    thread.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n👋 Bridge detenido.")
