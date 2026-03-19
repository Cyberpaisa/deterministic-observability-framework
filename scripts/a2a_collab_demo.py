# -*- coding: utf-8 -*-
"""
🧬 Demo: Colaboración A2A (Agent-to-Agent)
Muestra cómo dos instancias de Enigma colaboran en el cracking de una clave secp256k1.
"""

from core.sovereign_security_module import SovereignLab
import json

def run_a2a_demo():
    print("🚀 Iniciando Simulación de Colaboración A2A...")
    
    agent_alpha = SovereignLab()
    agent_beta = SovereignLab()
    
    # Objetivo compartido
    target_pub = "0479be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798"
    
    # Alpha delega un bloque a Beta
    work_block = {
        "range": "0x10000000 -> 0x1FFFFFFF",
        "target": target_pub,
        "difficulty": "STAGGERED"
    }
    
    print("\n[Agent Alpha] -> [Agent Beta]: Enviando bloque de trabajo ECC...")
    response = agent_beta.receive_a2a_block("ENIGMA_ALPHA", work_block)
    
    print(f"\n[Agent Beta] Response: {json.dumps(response, indent=2)}")
    
    if response["status"] == "ACK":
        print("\n✅ Consenso A2A Establecido. Cracking distribuido en progreso...")

if __name__ == "__main__":
    run_a2a_demo()
