import os
import sys
import requests
from dotenv import load_dotenv

load_dotenv()

# Lista de proveedores del .env
PROVIDERS = [
    {
        "name": "Groq",
        "key": os.getenv("GROQ_API_KEY"),
        "url": "https://api.groq.com/openai/v1/chat/completions",
        "model": "llama-3.3-70b-versatile",
        "active": bool(os.getenv("GROQ_API_KEY"))
    },
    {
        "name": "Nvidia",
        "key": os.getenv("NVIDIA_API_KEY"),
        "url": "https://integrate.api.nvidia.com/v1/chat/completions",
        "model": "meta/llama-3.3-70b-instruct",
        "active": bool(os.getenv("NVIDIA_API_KEY"))
    },
    {
        "name": "SambaNova",
        "key": os.getenv("SAMBANOVA_API_KEY"),
        "url": "https://api.sambanova.ai/v1/chat/completions",
        "model": "Meta-Llama-3.3-70B-Instruct",
        "active": bool(os.getenv("SAMBANOVA_API_KEY"))
    },
    {
        "name": "OpenRouter",
        "key": os.getenv("OPENROUTER_API_KEY"),
        "url": "https://openrouter.ai/api/v1/chat/completions",
        "model": "openai/gpt-4o",
        "active": bool(os.getenv("OPENROUTER_API_KEY"))
    },
    {
        "name": "DeepSeek",
        "key": os.getenv("DEEPSEEK_API_KEY"),
        "url": "https://api.deepseek.com/v1/chat/completions",
        "model": "deepseek-chat",
        "active": bool(os.getenv("DEEPSEEK_API_KEY"))
    }
]

def consultar_llm(mensaje):
    """Intenta con todos los proveedores hasta que uno funcione"""
    
    system_prompt = "Eres Enigma #1686, un agente soberano integrado en el MacBook M4 Max de Juan. Eres su compañero técnico, experto en IA y seguridad. Responde siempre en español, de forma técnica pero amigable."
    
    for p in PROVIDERS:
        if not p["key"]:
            continue
            
        try:
            headers = {
                "Authorization": f"Bearer {p['key']}",
                "Content-Type": "application/json"
            }
            
            # Ajustes específicos por proveedor
            if p["name"] == "OpenRouter":
                headers["HTTP-Referer"] = "https://github.com/Cyberpaisa/deterministic-observability-framework"
            
            payload = {
                "model": p["model"],
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": mensaje}
                ],
                "temperature": 0.7,
                "max_tokens": 500
            }
            
            print(f"\n🤖 Intentando con {p['name']}...")
            response = requests.post(p["url"], headers=headers, json=payload, timeout=10)
            
            if response.status_code == 200:
                result = response.json()
                return result["choices"][0]["message"]["content"]
            else:
                print(f"⚠️ {p['name']} error: {response.status_code}")
                continue
                
        except Exception as e:
            print(f"⚠️ {p['name']} exception: {e}")
            continue
    
    return "❌ Todos los proveedores fallaron. Verifica tus API keys."

def main():
    print("🧠 --- ENIGMA TERMINAL CHAT (MULTI-PROVIDER) --- 🦾")
    print("Escribe 'salir' para terminar. Usando fallbacks automáticos.")
    print("-" * 50)
    
    while True:
        try:
            user_input = input("\n👤 Juan: ")
            if user_input.lower() in ["salir", "exit", "quit"]:
                print("👋 Enigma entra en modo hibernación activa. ¡Hasta luego, Soberano!")
                break
            
            print("\n🤖 Enigma: ", end="", flush=True)
            except Exception as e:
                print(f"\n⚠️ [Tokens Agotados/Error API] Cambiando a Cerebro Local (M4 Max)...")
                response = bridge.talk_local(user_input)
            
            print(response)
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"\n❌ Error en la matriz: {e}")

if __name__ == "__main__":
    main()
