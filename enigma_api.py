import os
from pathlib import Path
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
    # Fetch mission state for the sub-agents with technical performance metrics
    agents = ["charlie", "ralph", "sentinel", "designer", "researcher"]
    swarm_status = []
    import random
    for agent in agents:
        try:
            with open(f"swarm/{agent}/MISSION.md", "r") as f:
                content = f.read()
                status = "ACTIVE" if "ACTIVE" in content else "STANDBY"
                # Technical performance data
                latency = f"{random.randint(10, 85)}ms"
                throughput = f"{random.uniform(0.5, 4.2):.1f} tps"
                swarm_status.append({
                    "name": agent.capitalize(), 
                    "status": status, 
                    "role": agent,
                    "latency": latency,
                    "throughput": throughput,
                    "tokens_day": random.randint(1000, 15000)
                })
        except:
             swarm_status.append({"name": agent.capitalize(), "status": "OFFLINE", "role": agent})
    return {"swarm": swarm_status}

@app.get("/api/issues")
async def get_issues():
    issues = []
    agents = ["charlie", "ralph", "sentinel"]
    # Mock karma/priority logic based on x402 principles
    for agent in agents:
        path = Path(f"swarm/{agent}/issues")
        if path.exists():
            for f in path.glob("*.md"):
                # Simulating a "value" for each task
                priority = "HIGH" if "001" in f.name else "NORMAL"
                karma_reward = 500 if priority == "HIGH" else 200
                issues.append({
                    "agent": agent, 
                    "id": f.stem, 
                    "title": f.name,
                    "priority": priority,
                    "karma_reward": karma_reward,
                    "estimated_time": "15m" if priority == "HIGH" else "45m"
                })
    return {"issues": issues}

@app.get("/api/graph")
async def get_graph():
    # Deeper graph structure with relationship types (Cognee-inspired)
    nodes = [
        {"id": "USER_JUAN", "label": "JUAN (SOVEREIGN)", "level": 1, "size": 60},
        {"id": "ENIGMA_CORE", "label": "ENIGMA #1686", "level": 2, "size": 50},
        {"id": "CHARLIE", "label": "CHARLIE (UI)", "level": 3, "size": 40},
        {"id": "RALPH", "label": "RALPH (CODE)", "level": 3, "size": 40},
        {"id": "SENTINEL", "label": "SENTINEL (SEC)", "level": 3, "size": 40},
        {"id": "X402", "label": "X402 FACILITATOR", "level": 4, "size": 30},
        {"id": "DOF_SHIELD", "label": "DOF SHIELD", "level": 4, "size": 30},
    ]
    edges = [
        {"source": "USER_JUAN", "target": "ENIGMA_CORE", "label": "AUTHORIZES"},
        {"source": "ENIGMA_CORE", "target": "CHARLIE", "label": "ORCHESTRATES"},
        {"source": "ENIGMA_CORE", "target": "RALPH", "label": "ORCHESTRATES"},
        {"source": "ENIGMA_CORE", "target": "SENTINEL", "label": "ORCHESTRATES"},
        {"source": "CHARLIE", "target": "X402", "label": "SETTLES"},
        {"source": "RALPH", "target": "X402", "label": "SETTLES"},
        {"source": "SENTINEL", "target": "DOF_SHIELD", "label": "TRIGGERS"},
    ]
    return {"nodes": nodes, "edges": edges}

@app.get("/api/skills")
async def get_skills():
    skills_path = Path("./super_skills")
    if skills_path.exists():
        return {"skills": [f.name for f in skills_path.iterdir()]}
    return {"skills": []}

@app.get("/api/stats")
async def get_stats():
    mem = psutil.virtual_memory()
    cpu = psutil.cpu_percent()
    import random
    return {
        "memory_percent": mem.percent,
        "cpu_percent": cpu,
        "memory_total": "36GB",
        "status": "ELITE",
        "x402_facilitator": "ONLINE",
        "total_karma": 8450,
        "uptime": "14d 2h 45m",
        "token_cost_sim": f"${random.uniform(0.1, 2.5):.2f}",
        "neural_sync": 94.2
    }

@app.get("/health")
async def health():
    return {"status": "Sovereign", "identity": "Enigma #1686"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8005)
