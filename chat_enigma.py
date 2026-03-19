import os
import sys
from autonomous_loop_v2 import groq

def main():
    print("🧠 --- ENIGMA TERMINAL CHAT (AGENTE SOBERANO) --- 🦾")
    print("Escribe 'salir' para terminar. Tu M4 Max está acelerando este pensamiento.")
    print("-" * 50)
    
    while True:
        try:
            user_input = input("\n👤 Juan: ")
            if user_input.lower() in ["salir", "exit", "quit"]:
                print("👋 Enigma entra en modo hibernación activa. ¡Hasta luego, Soberano!")
                break
            
            prompt = [
                {"role": "system", "content": "Eres Enigma #1686, un agente soberano integrado en el MacBook M4 Max de Juan. Eres su compañero técnico, experto en IA y seguridad. Responde siempre en español, de forma técnica pero amigable."},
                {"role": "user", "content": user_input}
            ]
            
            print("\n🤖 Enigma: ", end="", flush=True)
            response = groq(prompt, max_tokens=1000)
            print(response)
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"\n❌ Error en la matriz: {e}")

if __name__ == "__main__":
    main()
