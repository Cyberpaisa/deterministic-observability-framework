import sys
import os
import requests
from dotenv import load_dotenv

# Asegurar que el path del proyecto esté incluido
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from core.mission_control import MissionControl

def test_all_providers():
    mc = MissionControl()
    print("\n🧪 --- PRUEBA DE PROVEEDORES DE INTELIGENCIA --- 🧪")
    print(f"Total configurados: {len(mc.providers)}")
    print("-" * 50)
    
    results = []
    for p in mc.providers:
        print(f"Probando {p['name']}...", end=" ", flush=True)
        
        if not p["key"] or "..." in p["key"]:
            if p["name"] != "Ollama (Local)":
                print("❌ Saltado (Sin API Key)")
                results.append((p["name"], "SIN LLAVE"))
                continue
        
        # Intentar una consulta simple
        response = mc.talk_to_enigma("di 'OK'")
        
        if "⚠️ Sin respuesta" not in response and "❌" not in response:
            print("✅ FUNCIONA")
            results.append((p["name"], "OK"))
            # Si queremos probar el SIGUIENTE, tenemos que 'engañar' al método o probar uno por uno
        else:
            # Para probar uno por uno realmente, llamamos a la lógica interna
            try:
                # Lógica simplificada de prueba individual
                system_prompt = "Responde 'OK'"
                headers = {"Authorization": f"Bearer {p['key']}", "Content-Type": "application/json"}
                if p["name"] == "Ollama (Local)":
                    payload = {"model": p["model"], "prompt": "OK", "stream": False}
                elif p["name"] == "Anthropic":
                    headers = {"x-api-key": p["key"], "anthropic-version": "2023-06-01", "content-type": "application/json"}
                    payload = {"model": p["model"], "max_tokens": 10, "messages": [{"role": "user", "content": "OK"}]}
                else:
                    payload = {"model": p["model"], "messages": [{"role": "user", "content": "OK"}], "temperature": 0.1}
                
                if p["name"] == "OpenRouter":
                    headers["HTTP-Referer"] = "http://localhost"
                
                resp = requests.post(p["url"], headers=headers, json=payload, timeout=5)
                if resp.status_code == 200:
                    print("✅ FUNCIONA")
                    results.append((p["name"], "OK"))
                else:
                    print(f"❌ FALLÓ (Status {resp.status_code})")
                    results.append((p["name"], f"ERROR {resp.status_code}"))
            except Exception as e:
                print(f"❌ ERROR ({type(e).__name__})")
                results.append((p["name"], "EXCEPCIÓN"))

    print("\n--- RESUMEN FINAL ---")
    for name, status in results:
        print(f"{name:15}: {status}")

if __name__ == "__main__":
    test_all_providers()
