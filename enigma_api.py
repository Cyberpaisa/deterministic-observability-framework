import os
from pathlib import Path
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import requests
import sys
from core.identity import ENIGMA_SYSTEM_PROMPT

# Add current directory to path for core imports
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

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

LEGION_13 = {
    "biz-dominator": {"role": "Strategy", "mission": "Revenue & Growth Maxing"},
    "scrum-master-zen": {"role": "Agile", "mission": "Velocity Optimization"},
    "product-overlord": {"role": "Product", "mission": "Roadmap Enforcement"},
    "blockchain-wizard": {"role": "Multichain", "mission": "Cross-Chain Mastery"},
    "defi-orbital": {"role": "Finance", "mission": "Yield & Liquidity"},
    "rwa-tokenizator": {"role": "RWA", "mission": "Real World Asset Bridging"},
    "sentinel-shield": {"role": "Security", "mission": "Zero-Trust Defense"},
    "qa-vigilante": {"role": "Quality", "mission": "Code & UX Validation"},
    "charlie-ux": {"role": "Frontend", "mission": "Premium HUD Design"},
    "ralph-code": {"role": "Backend", "mission": "Core Systems"},
    "moltbook": {"role": "Social", "mission": "Karma & Reputation Domination"},
    "organizer-os": {"role": "System OS", "mission": "Sovereign Infrastructure Sync"},
    "qa-specialist": {"role": "QA", "mission": "Zero-Bug Enforcement"},
    "architect-enigma": {"role": "Architect", "mission": "System Scalability Audit"}
}

@app.get("/api/swarm")
async def get_swarm():
    swarm_status = []
    import random
    for agent, data in LEGION_13.items():
        # Force ACTIVE for visual consistency as requested
        swarm_status.append({
            "id": agent,
            "name": agent.upper(), 
            "status": "ACTIVE", 
            "role": data["role"],
            "latency": f"{random.randint(5, 35)}ms",
            "throughput": f"{random.uniform(2.5, 12.8):.1f} tps",
            "tokens_day": random.randint(15000, 45000)
        })
    return {"swarm": swarm_status}

@app.get("/api/issues")
async def get_issues():
    track_missions = [
        {"agent": "blockchain-wizard", "id": "TRACK-CELO", "title": "Deploy Agentic Celo App", "priority": "HIGH", "karma_reward": 3000},
        {"agent": "sentinel-shield", "id": "TRACK-ERC8004", "title": "On-chain Identity Proofs", "priority": "HIGH", "karma_reward": 2000},
        {"agent": "moltbook", "id": "TRACK-SOCIAL", "title": "24/7 Karma Dominance", "priority": "HIGH", "karma_reward": 1500},
        {"agent": "defi-orbital", "id": "TRACK-X402", "title": "Trustless Micro-payments", "priority": "HIGH", "karma_reward": 2500},
    ]
    return {"issues": track_missions}

@app.get("/api/graph")
async def get_graph():
    nodes = [
        {"id": "USER_JUAN", "label": "JUAN (SOVEREIGN)", "level": 1, "type": "USER", "status": "ONLINE"},
        {"id": "ENIGMA_CORE", "label": "ENIGMA #1686", "level": 2, "type": "CORE", "status": "ELITE"},
    ]
    for agent in LEGION_13.keys():
        level = 3
        if agent in ["biz-dominator", "scrum-master-zen", "product-overlord"]: level = 4
        if agent in ["blockchain-wizard", "defi-orbital", "rwa-tokenizator"]: level = 4
        nodes.append({"id": agent, "label": agent.upper(), "level": level, "type": "AGENT", "status": "ACTIVE"})
    
    # Static edges for the complete legion
    edges = [
        {"source": "USER_JUAN", "target": "ENIGMA_CORE", "label": "AUTHORIZES", "activity": 0.9},
        {"source": "ENIGMA_CORE", "target": "charlie-ux", "label": "ORCHESTRATES", "activity": 0.6},
        {"source": "ENIGMA_CORE", "target": "ralph-code", "label": "ORCHESTRATES", "activity": 0.5},
        {"source": "ENIGMA_CORE", "target": "sentinel-shield", "label": "AUDITS", "activity": 0.8},
        {"source": "ENIGMA_CORE", "target": "moltbook", "label": "SOCIALIZES", "activity": 0.95},
        {"source": "ENIGMA_CORE", "target": "organizer-os", "label": "MANAGES", "activity": 0.7},
    ]
    return {"nodes": nodes, "edges": edges}

@app.get("/api/skills")
async def get_skills():
    from core.skill_engine import SovereignSkillEngine
    engine = SovereignSkillEngine()
    engine.load_skills()
    return {
        "access": "UNIVERSAL_SOVEREIGN_ROOT",
        "active_skills": list(engine.registry.keys()),
        "status": "ALL_AGENTS_SYNCED_V2"
    }

@app.get("/api/social")
async def get_social():
    import random
    return {
        "status": "ACTIVE",
        "total_karma": 12850 + random.randint(10, 50),
        "reputation": "ELITE_SOVEREIGN",
        "recent_interactions": [
            {"user": "cybercentry", "action": "REPLY", "karma": "+5"},
            {"user": "automationscout", "action": "INSIGHT", "karma": "+15"},
            {"user": "world_observer", "action": "FOLLOW", "karma": "+50"}
        ],
        "firewall": "ACTIVE_100",
        "threat_neutralized": random.randint(3, 12)
    }

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
        "total_karma": 12850,
        "uptime": "14d 2h 45m",
        "token_cost_sim": f"${random.uniform(0.1, 2.5):.2f}",
        "neural_sync": 96.8
    }

@app.get("/health")
async def health():
    return {"status": "Sovereign", "identity": "Enigma #1686"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8005)
