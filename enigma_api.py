import os
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import requests
from core.identity import ENIGMA_SYSTEM_PROMPT

app = FastAPI(title="Enigma Sovereign API")

# Habilitar CORS para localhost:3001
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str
    user: str = "Juan"

@app.post("/api/chat")
async def chat_endpoint(req: ChatRequest):
    try:
        # Hablar directamente con Ollama usando el prompt de Enigma
        # Se asume que el modelo 'enigma' ya fue creado
        ollama_url = "http://localhost:11434/api/generate"
        payload = {
            "model": "enigma",
            "prompt": req.message,
            "stream": False,
            "system": ENIGMA_SYSTEM_PROMPT
        }
        
        response = requests.post(ollama_url, json=payload, timeout=30)
        if response.status_code == 200:
            return {"response": response.json()["response"]}
        else:
            # Fallback a llama3 si enigma fallara por alguna razón
            payload["model"] = "llama3"
            response = requests.post(ollama_url, json=payload, timeout=30)
            return {"response": response.json()["response"]}
            
    except Exception as e:
        print(f"❌ Error API: {e}")
        return {"response": "⚠️ Error de conexión con el cerebro local. Verifica que Ollama esté activo."}

@app.get("/health")
async def health():
    return {"status": "Sovereign", "identity": "Enigma #1686"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8005)
