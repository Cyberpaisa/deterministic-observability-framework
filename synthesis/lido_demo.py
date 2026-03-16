#!/usr/bin/env python3
"""
Lido MCP Integration Demo
For Lido Bounty - Synthesis 2026
"""

import requests
import json

def demo_lido_mcp():
    """Demo all Lido MCP endpoints"""
    base_url = "https://vastly-noncontrolling-christena.ngrok-free.dev"
    headers = {"ngrok-skip-browser-warning": "true"}
    
    # 1. Check APY
    apy_response = requests.get(f"{base_url}/mcp/lido/apy", headers=headers)
    print(f"📈 Current Lido APY: {apy_response.json()}")
    
    # 2. Simulate staking 10 ETH
    stake_response = requests.post(
        f"{base_url}/mcp/lido/stake",
        json={"amount": 10.0, "referral": "0xDOF"},
        headers=headers
    )
    print(f"🥩 Staking result: {stake_response.json()}")
    
    # 3. Check governance proposals
    gov_response = requests.get(f"{base_url}/mcp/lido/governance/proposals", headers=headers)
    print(f"🗳️ Active proposals: {gov_response.json()}")
    
    return {"status": "success", "demo_complete": True}

if __name__ == "__main__":
    print("=" * 60)
    print("Lido MCP Demo - DOF Agent #1686")
    print("=" * 60)
    demo_lido_mcp()
    print("\n✅ Demo completed")
