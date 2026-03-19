import os
import logging
import requests
from typing import List, Dict

logger = logging.getLogger("enigma.llm_bridge")

class LLMBridge:
    """
    Puente de Inteligencia Multinivel.
    Gestiona el cambio entre modelos Premium (Gemini/Groq) y locales Gratuitos (Ollama/MLX).
    Asegura que Enigma nunca se quede sin 'tokens' para avanzar.
    """
    def __init__(self):
        self.local_url = os.getenv("OLLAMA_HOST", "http://localhost:11434/api/generate")
        self.primary_model = "qwen2.5:32b" # Recomendado para M4 Max
        self.fallback_model = "llama3.1:8b" # Rápido y ligero

    def talk_local(self, prompt: str, model: str = "") -> str:
        """Habla con el cerebro local (Ollama) si no hay internet o tokens."""
        target_model = model if model else self.primary_model
        try:
            payload = {
                "model": target_model,
                "prompt": prompt,
                "stream": False
            }
            response = requests.post(self.local_url, json=payload, timeout=60)
            if response.status_code == 200:
                return response.json().get("response", "Error: No response content")
            return f"Error Local: {response.status_code}"
        except Exception as e:
            logger.error(f"❌ Fallo en Cerebro Local: {e}")
            return "MODO_HIBERNACION: No tengo acceso a modelos locales."

    def smart_query(self, prompt: str) -> str:
        """
        Decide qué cerebro usar basado en complejidad.
        """
        if len(prompt) < 100: # Tareas simples van al local
             return self.talk_local(prompt, self.fallback_model)
        return self.talk_local(prompt, self.primary_model)

if __name__ == "__main__":
    bridge = LLMBridge()
    print("🧠 Puente de Inteligencia Activo.")
