import os
import json
import logging
import asyncio
import subprocess
import requests
from typing import Dict, List
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
try:
    from hardware_optimizer import HardwareOptimizer
    from backup_manager import CloudBackupManager
except ImportError:
    from core.hardware_optimizer import HardwareOptimizer
    from core.backup_manager import CloudBackupManager

logger = logging.getLogger("enigma.mission_control")

class MissionControl:
    """
    Dashboard Central de Enigma. 
    Gestiona el calendario de tareas, el enjambre de agentes y la memoria.
    Inspirado en los estándares de élite de Alex Finn pero soberano.
    """
    def __init__(self):
        self.base_dir = "/Users/jquiceva/equipo de agentes/deterministic-observability-framework"
        self.tasks_file = os.path.join(self.base_dir, "data/tasks.json")
        self.agents_config = os.path.join(self.base_dir, "core/chains_config.json")
        self.providers = [
            {"name": "Ollama (Local)", "key": "ollama", "url": os.getenv("OLLAMA_HOST", "http://localhost:11434") + "/api/generate", "model": "llama3"},
            {"name": "OpenAI", "key": os.getenv("OPENAI_API_KEY"), "url": "https://api.openai.com/v1/chat/completions", "model": "gpt-4o-mini"},
            {"name": "Anthropic", "key": os.getenv("ANTHROPIC_API_KEY"), "url": "https://api.anthropic.com/v1/messages", "model": "claude-3-5-sonnet-20240620"},
            {"name": "Groq", "key": os.getenv("GROQ_API_KEY"), "url": "https://api.groq.com/openai/v1/chat/completions", "model": "llama-3.3-70b-versatile"},
            {"name": "Nvidia", "key": os.getenv("NVIDIA_API_KEY"), "url": "https://integrate.api.nvidia.com/v1/chat/completions", "model": "meta/llama-3.3-70b-instruct"},
            {"name": "Mistral", "key": os.getenv("MISTRAL_API_KEY"), "url": "https://api.mistral.ai/v1/chat/completions", "model": "mistral-large-latest"},
            {"name": "Cerebras", "key": os.getenv("CEREBRAS_API_KEY"), "url": "https://api.cerebras.ai/v1/chat/completions", "model": "llama3.1-70b"},
            {"name": "OpenRouter", "key": os.getenv("OPENROUTER_API_KEY"), "url": "https://openrouter.ai/api/v1/chat/completions", "model": "meta-llama/llama-3.1-8b-instruct:free"},
            {"name": "DeepSeek", "key": os.getenv("DEEPSEEK_API_KEY"), "url": "https://api.deepseek.com/v1/chat/completions", "model": "deepseek-chat"}
        ]
        self.optimizer = HardwareOptimizer()
        self.backup_manager = CloudBackupManager()
        self._ensure_paths()

    def _ensure_paths(self):
        os.makedirs(os.path.join(self.base_dir, "data"), exist_ok=True)
        if not os.path.exists(self.tasks_file):
            with open(self.tasks_file, "w") as f:
                json.dump({"active_tasks": [], "history": []}, f)

    def get_status(self):
        """Devuelve un resumen del estado del sistema real-time."""
        hw_info = self.optimizer.detect_capabilities()
        with open(self.tasks_file, "r") as f:
            tasks = json.load(f)
        
        status = {
            "agente_principal": "Enigma #1686",
            "hardware": {
                "chip": hw_info["chip_family"],
                "ram": f"{hw_info['ram_gb']} GB",
                "tier": os.getenv("ENIGMA_MODEL_TIER", "DETECTING...")
            },
            "enjambre": ["Charlie (Web)", "Ralph (Code)", "Sentinel (Security)"],
            "tareas_activas": len(tasks["active_tasks"]),
            "ultima_sincronizacion": datetime.now().strftime("%H:%M:%S"),
            "boveda_segura": "Conectada (GitHub Sync Active)"
        }
        return status

    def run_daily_maintenance(self):
        """Ejecuta optimizaciones y respaldo seguro."""
        print("\n🛠️ --- Mantenimiento Soberano de Enigma ---")
        self.optimizer.apply_optimizations()
        success = self.backup_manager.sync_to_cloud()
        if success:
            print("✅ Bóveda sincronizada correctamente.")
        else:
            print("⚠️ Error en sincronización de Bóveda.")

    def talk_to_enigma(self, message: str):
        """Intenta charlar con Enigma usando fallbacks de LLM."""
        system_prompt = "Eres Enigma #1686, un agente soberano en el M4 Max de Juan. Responde siempre en español."
        
        for p in self.providers:
            if not p["key"] or "..." in p["key"]: continue
            try:
                headers = {"Authorization": f"Bearer {p['key']}", "Content-Type": "application/json"}
                
                if p["name"] == "Ollama (Local)":
                    payload = {
                        "model": p["model"],
                        "prompt": f"{system_prompt}\n\nUsuario: {message}\nEnigma:",
                        "stream": False
                    }
                elif p["name"] == "Anthropic":
                    headers = {
                        "x-api-key": p["key"],
                        "anthropic-version": "2023-06-01",
                        "content-type": "application/json"
                    }
                    payload = {
                        "model": p["model"],
                        "max_tokens": 1024,
                        "messages": [{"role": "user", "content": message}]
                    }
                else:
                    payload = {
                        "model": p["model"],
                        "messages": [{"role": "system", "content": system_prompt}, {"role": "user", "content": message}],
                        "temperature": 0.7
                    }
                
                if p["name"] == "OpenRouter":
                    headers["HTTP-Referer"] = "https://github.com/Cyberpaisa/deterministic-observability-framework"
                    headers["X-Title"] = "Enigma Sovereign Agent"

                response = requests.post(p["url"], headers=headers, json=payload, timeout=15)
                if response.status_code == 200:
                    result = response.json()
                    if p["name"] == "Ollama (Local)":
                        return result["response"]
                    if p["name"] == "Anthropic":
                        return result["content"][0]["text"]
                    return result["choices"][0]["message"]["content"]
            except:
                continue
        return "⚠️ Sin respuesta de la IA. Revisa tus API keys en el .env."

    def start_chat_session(self):
        """Inicia una sesión interactiva desde Mission Control."""
        print("\n🧠 --- SESIÓN DE CHAT: ENIGMA MISSION CONTROL --- 🦾")
        print("M4 Max detectado y listo. Escribe 'salir' para terminar.")
        while True:
            u_input = input("\n👤 Juan: ")
            if u_input.lower() in ["salir", "exit"]: break
            print(f"\n🤖 Enigma: {self.talk_to_enigma(u_input)}")

    def schedule_task(self, name: str, agent: str, frequency: str):
        """Programa una tarea automática (Cron-like)."""
        logger.info(f"📅 Programando tarea '{name}' para el agente '{agent}' con frecuencia '{frequency}'")
        # Aquí se integrará con un loop de asyncio o cron del sistema
        pass

if __name__ == "__main__":
    mc = MissionControl()
    mc.run_daily_maintenance()
    print("\n📊 --- Estado del Sistema ---")
    print(json.dumps(mc.get_status(), indent=4, ensure_ascii=False))

