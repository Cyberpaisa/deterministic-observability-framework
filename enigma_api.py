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
        ollama_url = "http://127.0.0.1:11434/api/generate"
        payload = {
            "model": "enigma",
            "prompt": req.message,
            "stream": False,
            "system": ENIGMA_SYSTEM_PROMPT
        }
        
        response = requests.post(ollama_url, json=payload, timeout=120)
        if response.status_code == 200:
            return {"response": response.json()["response"]}
        else:
            # Fallback a llama3 si enigma fallara por alguna razón
            payload["model"] = "llama3"
            response = requests.post(ollama_url, json=payload, timeout=120)
            return {"response": response.json()["response"]}
            
    except Exception as e:
        print(f"❌ Error API: {e}")
        return {"response": "⚠️ Error de conexión con el cerebro local. Verifica que Ollama esté activo."}

import psutil

import subprocess

class ExecRequest(BaseModel):
    command: str

@app.post("/api/exec")
async def run_task(req: ExecRequest):
    # Authorized tasks for the agent
    safe_commands = ["ollama list", "ps -ax", "ls -R super_skills", "python3 --version"]
    if any(cmd.startswith(req.command) for cmd in safe_commands) or "check" in req.command:
        try:
            result = subprocess.check_output(req.command, shell=True, stderr=subprocess.STDOUT, text=True)
            return {"output": result}
        except Exception as e:
            return {"output": f"Error: {str(e)}"}
    return {"output": "Comando no autorizado por el protocolo DOF Shield."}

@app.get("/api/swarm")
async def get_swarm():
    # Fetch mission state for the sub-agents
    agents = ["charlie", "ralph", "sentinel"]
    swarm_status = []
    for agent in agents:
        try:
            with open(f"swarm/{agent}/MISSION.md", "r") as f:
                content = f.read()
                status = "ACTIVE" if "ACTIVE" in content else "STANDBY"
                swarm_status.append({"name": agent.capitalize(), "status": status, "role": agent})
        except:
             swarm_status.append({"name": agent.capitalize(), "status": "OFFLINE", "role": agent})
    return {"swarm": swarm_status}

@app.get("/api/skills")
async def get_skills():
    skills_path = Path("./super_skills")
    if skills_path.exists():
        return {"skills": [f.name for f in skills_path.iterdir()]}
    return {"skills": []}

@app.get("/api/stats")
async def get_stats():
    # Hardware stats for the M4 Max / Mac
    mem = psutil.virtual_memory()
    # Dummy GPU for now as psutil doesn't get Apple Silicon GPU easily without extra libs, 
    # but we will use load as a proxy or just CPU for now.
    cpu = psutil.cpu_percent()
    return {
        "memory_percent": mem.percent,
        "cpu_percent": cpu,
        "memory_total": "36GB",
        "status": "ELITE"
    }

@app.get("/health")
async def health():
    return {"status": "Sovereign", "identity": "Enigma #1686"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8005)
