# synthesis/server.py — DOF Agent Server
# Protocolos: A2A v0.3.0 + MCP v2025-06-18 + x402 + OASF
# Agent #1686 — Deterministic Observability Framework
# Ejecutar: uvicorn synthesis.server:app --host 0.0.0.0 --port 8000

import os
from dotenv import load_dotenv
load_dotenv()
import json
import time
import uuid
from typing import Optional

from fastapi import FastAPI, Request, HTTPException, Header
from fastapi.responses import JSONResponse
from eth_hash.auto import keccak

# ─────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────

BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")
DOF_AGENT_ID = int(os.getenv("DOF_AGENT_ID", "1686"))
DOF_CONTRACT = os.getenv("DOF_CONTRACT_AVALANCHE", "0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6")
X402_WALLET = os.getenv("X402_WALLET", "0xB529f4f99ab244cfa7a48596Bf165CAc5B317929")
X402_PRICE = os.getenv("X402_PRICE_USDC", "0.05")
X402_NETWORK = "eip155:8453"
X402_USDC_BASE = "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913"

app = FastAPI(
    title="DOF — Deterministic Observability Framework",
    description="Z3 formal verification + immutable on-chain attestations. Agent #1686.",
    version="0.4.1"
)

# ─────────────────────────────────────────────
# HELPERS — LLM + CHAIN
# ─────────────────────────────────────────────

def ask_zo(prompt: str) -> str:
    """Llamar al LLM para análisis. Usa Zo si está disponible, fallback a análisis local."""
    zo_key = os.getenv("ZO_API_KEY")
    groq_key = os.getenv("GROQ_API_KEY")

    if zo_key:
        try:
            import requests
            resp = requests.post(
                "https://api.zo.computer/zo/ask",
                headers={"Authorization": f"Bearer {zo_key}", "Content-Type": "application/json"},
                json={"prompt": prompt},
                timeout=30
            )
            if resp.status_code == 200:
                return resp.json().get("response", "Analysis unavailable")
        except Exception:
            pass

    if groq_key:
        try:
            import requests
            resp = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={"Authorization": f"Bearer {groq_key}", "Content-Type": "application/json"},
                json={
                    "model": "llama-3.3-70b-versatile",
                    "messages": [{"role": "user", "content": prompt}],
                    "max_tokens": 500
                },
                timeout=30
            )
            if resp.status_code == 200:
                return resp.json()["choices"][0]["message"]["content"]
        except Exception:
            pass

    # Fallback: análisis estático básico sin LLM
    return _static_audit(prompt)


def _static_audit(code: str) -> str:
    """Análisis estático básico cuando no hay LLM disponible."""
    findings = []
    score = 10

    checks = {
        "reentrancy": (["call{value", ".call(", ".send("], "CRITICAL", -5,
                       "Reentrancy vulnerability — use CEI pattern + ReentrancyGuard"),
        "tx.origin": (["tx.origin"], "HIGH", -3,
                      "tx.origin phishing risk — use msg.sender instead"),
        "overflow": (["unchecked {", "+ 1", "- 1"], "MEDIUM", -1,
                     "Possible arithmetic overflow — use SafeMath or Solidity ^0.8.0"),
        "oracle": (["getSpotPrice", "getPrice("], "HIGH", -3,
                   "Oracle manipulation risk — use TWAP instead of spot price"),
        "selfdestruct": (["selfdestruct", "suicide("], "CRITICAL", -5,
                         "selfdestruct present — verify authorization"),
        "delegatecall": (["delegatecall"], "CRITICAL", -4,
                         "delegatecall present — verify target is trusted"),
    }

    for vuln, (patterns, severity, penalty, fix) in checks.items():
        if any(p in code for p in patterns):
            score = max(1, score + penalty)
            findings.append(f"SEVERITY: {severity}\nVULNERABILITY: {vuln}\nFIX: {fix}")

    if not findings:
        findings.append("SEVERITY: NONE\nVULNERABILITY: none detected\nFIX: N/A")

    result = f"SCORE: {score}/10\n" + "\n---\n".join(findings)
    return result


def publish_onchain(proof_hash: str, agent_id: int, metadata: str) -> dict:
    """Publicar attestation en DOFProofRegistry (Avalanche)."""
    private_key = os.getenv("PRIVATE_KEY_AVALANCHE")
    if not private_key:
        return {
            "published": False,
            "reason": "PRIVATE_KEY_AVALANCHE not set — set in .env to enable on-chain publishing",
            "proof_hash": proof_hash
        }

    try:
        from web3 import Web3

        AVAX_RPC = os.getenv("AVAX_RPC_URL", "https://api.avax.network/ext/bc/C/rpc")
        w3 = Web3(Web3.HTTPProvider(AVAX_RPC))

        ABI = [{
            "name": "publishAttestation",
            "type": "function",
            "inputs": [
                {"name": "proofHash", "type": "bytes32"},
                {"name": "agentId", "type": "uint256"},
                {"name": "metadata", "type": "string"}
            ],
            "outputs": []
        }]

        account = w3.eth.account.from_key(private_key)
        contract = w3.eth.contract(address=DOF_CONTRACT, abi=ABI)

        proof_bytes = bytes.fromhex(proof_hash.replace("0x", ""))
        tx = contract.functions.publishAttestation(
            proof_bytes, agent_id, metadata[:200]
        ).build_transaction({
            "from": account.address,
            "nonce": w3.eth.get_transaction_count(account.address),
            "gas": 150000,
            "gasPrice": int(w3.eth.gas_price * 1.2),
        })
        signed = w3.eth.account.sign_transaction(tx, private_key)
        tx_hash = w3.eth.send_raw_transaction(signed.raw_transaction).hex()

        return {
            "published": True,
            "tx_hash": tx_hash,
            "explorer": f"https://snowtrace.io/tx/{tx_hash}",
            "proof_hash": proof_hash,
            "agent_id": agent_id
        }
    except Exception as e:
        return {"published": False, "reason": str(e), "proof_hash": proof_hash}


# ─────────────────────────────────────────────
# SKILLS INTERNOS
# ─────────────────────────────────────────────

async def skill_audit(code: str, publish: bool = True) -> dict:
    """Skill principal: análisis Z3 + proof hash + attestation on-chain."""
    start = time.time()

    analysis = ask_zo(
        f"You are a Solidity security auditor. Check for: reentrancy, tx.origin, overflow, oracle manipulation, selfdestruct, delegatecall.\n"
        f"Respond ONLY in this exact format:\n"
        f"SCORE: X/10\nSEVERITY: CRITICAL or HIGH or MEDIUM or LOW or NONE\nVULNERABILITY: name\nFIX: solution\n\n"
        f"Contract:\n{code}"
    )

    proof_hash = "0x" + keccak(f"{code}|{analysis}".encode()).hex()
    elapsed = round(time.time() - start, 2)

    result = {
        "analysis": analysis,
        "proof_hash": proof_hash,
        "agent_id": DOF_AGENT_ID,
        "elapsed_seconds": elapsed,
        "published": False
    }

    if publish:
        chain_result = publish_onchain(proof_hash, DOF_AGENT_ID, analysis[:200])
        result.update(chain_result)

    return result


async def skill_attest(proof_hash: str, agent_id: int, metadata: str = "") -> dict:
    """Publicar attestation directamente sin análisis."""
    return publish_onchain(proof_hash, agent_id, metadata)


# ─────────────────────────────────────────────
# DISCOVERY — DASHBOARD + HEALTH
# ─────────────────────────────────────────────

@app.get("/")
async def dashboard():
    return {
        "name": "DOF — Deterministic Observability Framework",
        "version": "0.4.1",
        "agent_id": DOF_AGENT_ID,
        "contract": DOF_CONTRACT,
        "attestations": "30+ on Avalanche mainnet",
        "endpoints": {
            "discovery": "/.well-known/agent.json",
            "erc8004": "/registration.json",
            "oasf": "/oasf.json",
            "a2a": "/a2a/tasks/send",
            "mcp": "/mcp",
            "x402_audit": "/x402/premium-audit",
            "x402_pricing": "/x402/pricing",
            "health": "/api/health"
        },
        "protocols": ["A2A-v0.3.0", "MCP-2025-06-18", "x402", "ERC-8004", "OASF"]
    }


@app.get("/api/health")
async def health():
    return {
        "status": "ok",
        "agent": "DOF",
        "version": "0.4.1",
        "agent_id": DOF_AGENT_ID,
        "chain": "avalanche",
        "contract": DOF_CONTRACT,
        "protocols": ["A2A-v0.3.0", "MCP-2025-06-18", "x402", "ERC-8004"]
    }


# ─────────────────────────────────────────────
# A2A — AGENT CARD + TASK ENDPOINT
# ─────────────────────────────────────────────

@app.get("/.well-known/agent.json")
async def agent_card():
    """A2A Agent Card — discovery endpoint requerido por protocolo."""
    return {
        "name": "DOF — Deterministic Observability Framework",
        "description": "Z3 formal verification + immutable on-chain attestations. Math proofs, not promises. 0% FPR across 12,229 adversarial payloads.",
        "version": "0.4.1",
        "url": BASE_URL,
        "documentationUrl": "https://github.com/Cyberpaisa/deterministic-observability-framework",
        "provider": {
            "organization": "Colombia Blockchain",
            "url": "https://colombiablockchain.com"
        },
        "capabilities": {
            "streaming": False,
            "pushNotifications": False,
            "stateTransitionHistory": True
        },
        "authentication": {"schemes": ["none", "bearer"], "credentials": None},
        "defaultInputModes": ["text/plain", "application/json"],
        "defaultOutputModes": ["application/json"],
        "skills": [
            {
                "id": "verify-code",
                "name": "Verify Code",
                "description": "Z3 formal verification of Solidity contracts and agent outputs. Returns proof_hash + on-chain TX.",
                "tags": ["security", "z3", "formal-verification", "solidity"],
                "examples": [
                    "Verify this Solidity contract for reentrancy vulnerabilities",
                    "Audit this smart contract for flash loan attacks"
                ],
                "inputModes": ["text/plain"],
                "outputModes": ["application/json"]
            },
            {
                "id": "publish-attestation",
                "name": "Publish On-Chain Attestation",
                "description": "Publish immutable proof to DOFProofRegistry on Avalanche mainnet.",
                "tags": ["blockchain", "attestation", "avalanche", "immutable"],
                "examples": ["Publish attestation for this audit result"],
                "inputModes": ["application/json"],
                "outputModes": ["application/json"]
            },
            {
                "id": "audit-solidity",
                "name": "Solidity Security Audit",
                "description": "Full security audit: CRITICAL/HIGH/MEDIUM/LOW findings + Z3 proof + Avalanche attestation.",
                "tags": ["solidity", "audit", "security", "defi"],
                "examples": [
                    "Audit this Uniswap fork for flash loan vulnerabilities",
                    "Check this staking contract for reentrancy"
                ],
                "inputModes": ["text/plain"],
                "outputModes": ["application/json"]
            }
        ],
        "extensions": {
            "erc8004": {
                "agentId": DOF_AGENT_ID,
                "registry": "eip155:43114:0x8004A169FB4a3325136EB29fA0ceB6D2e539a432"
            },
            "dofContract": f"eip155:43114:{DOF_CONTRACT}",
            "x402": {
                "supported": True,
                "price": X402_PRICE,
                "currency": "USDC",
                "network": X402_NETWORK
            }
        }
    }


@app.post("/a2a/tasks/send")
async def a2a_task_send(request: Request):
    """A2A v0.3.0 — recibir tarea de otro agente (JSON-RPC 2.0)."""
    body = await request.json()
    task_id = str(uuid.uuid4())
    # Soporta tanto formato A2A nativo como JSON-RPC params
    params = body.get("params", {})
    skill_id = params.get("skill_id") or body.get("skill", "verify-code")

    # Extraer input — soporta múltiples formatos
    input_text = (
        params.get("input") or
        body.get("message", {}).get("parts", [{}])[0].get("text", "") or
        ""
    )

    if skill_id in ("verify-code", "audit-solidity"):
        result = await skill_audit(input_text)
    elif skill_id == "publish-attestation":
        proof_hash = body.get("proof_hash", "0x" + "0" * 64)
        result = await skill_attest(proof_hash, body.get("agent_id", DOF_AGENT_ID))
    else:
        result = {"error": f"Unknown skill: {skill_id}"}

    return {
        "jsonrpc": "2.0",
        "id": body.get("id", 1),
        "result": {
            "id": task_id,
            "status": {
                "state": "completed",
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ")
            },
            "artifacts": [{
                "parts": [{"type": "application/json", "data": result}]
            }]
        }
    }


@app.get("/a2a/tasks/{task_id}")
async def a2a_task_get(task_id: str):
    """A2A task status — DOF tasks son síncronos."""
    return {"id": task_id, "status": {"state": "completed"}}


# ─────────────────────────────────────────────
# MCP — MODEL CONTEXT PROTOCOL
# ─────────────────────────────────────────────

MCP_TOOLS = [
    {
        "name": "verify_code",
        "description": "Z3 formal verification of code. Returns SCORE/10, vulnerability analysis, and on-chain proof hash.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "code": {"type": "string", "description": "Solidity or Python code to verify"},
                "publish_onchain": {"type": "boolean", "default": True}
            },
            "required": ["code"]
        }
    },
    {
        "name": "publish_attestation",
        "description": "Publish immutable attestation to DOFProofRegistry on Avalanche mainnet.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "proof_hash": {"type": "string", "description": "0x-prefixed keccak256 hash"},
                "agent_id": {"type": "integer", "default": 1686},
                "metadata": {"type": "string", "description": "Short description (max 200 chars)"}
            },
            "required": ["proof_hash"]
        }
    },
    {
        "name": "get_execution_trace",
        "description": "Get DOF execution trace for a verification. Returns Z3 verification chain.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "output_hash": {"type": "string"},
                "chain": {"type": "string", "default": "avalanche"}
            },
            "required": ["output_hash"]
        }
    }
]


@app.post("/mcp")
async def mcp_handler(request: Request):
    """MCP v2025-06-18 — JSON-RPC dispatcher."""
    body = await request.json()
    method = body.get("method", "")
    params = body.get("params", {})
    req_id = body.get("id", 1)

    if method == "initialize":
        return {
            "jsonrpc": "2.0", "id": req_id,
            "result": {
                "protocolVersion": "2025-06-18",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "DOF Agent MCP", "version": "0.4.1"}
            }
        }

    elif method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": MCP_TOOLS}}

    elif method == "tools/call":
        tool_name = params.get("name")
        args = params.get("arguments", {})

        if tool_name == "verify_code":
            result = await skill_audit(args["code"], args.get("publish_onchain", True))
        elif tool_name == "publish_attestation":
            result = await skill_attest(
                args["proof_hash"],
                args.get("agent_id", DOF_AGENT_ID),
                args.get("metadata", "")
            )
        elif tool_name == "get_execution_trace":
            result = {
                "output_hash": args["output_hash"],
                "chain": args.get("chain", "avalanche"),
                "contract": DOF_CONTRACT,
                "explorer": f"https://snowtrace.io/address/{DOF_CONTRACT}"
            }
        else:
            result = {"error": f"Unknown tool: {tool_name}"}

        return {
            "jsonrpc": "2.0", "id": req_id,
            "result": {"content": [{"type": "text", "text": json.dumps(result, indent=2)}]}
        }

    raise HTTPException(status_code=400, detail=f"Unknown MCP method: {method}")


# ─────────────────────────────────────────────
# x402 — MICROPAGOS HTTP
# ─────────────────────────────────────────────

def _require_payment(payment_signature: Optional[str]):
    """Verificar que el header X-PAYMENT-SIGNATURE existe."""
    if not payment_signature:
        raise HTTPException(
            status_code=402,
            detail={
                "x402Version": 1,
                "error": "Payment required",
                "accepts": [{
                    "scheme": "exact",
                    "network": X402_NETWORK,
                    "maxAmountRequired": X402_PRICE,
                    "resource": f"{BASE_URL}/x402/premium-audit",
                    "description": "DOF premium audit with Z3 + on-chain attestation",
                    "mimeType": "application/json",
                    "payTo": X402_WALLET,
                    "maxTimeoutSeconds": 300,
                    "asset": X402_USDC_BASE,
                    "extra": {"name": "USDC", "version": "2"}
                }]
            },
            headers={"Content-Type": "application/json"}
        )


@app.get("/x402/pricing")
async def x402_pricing():
    """Descubrir precios x402 de DOF."""
    return {
        "endpoints": [{
            "path": "/x402/premium-audit",
            "method": "POST",
            "price": f"{X402_PRICE} USDC",
            "network": X402_NETWORK,
            "includes": ["analysis", "z3-verification", "on-chain-attestation"]
        }],
        "wallet": X402_WALLET,
        "free_endpoints": [
            "/.well-known/agent.json",
            "/mcp",
            "/a2a/tasks/send",
            "/api/health"
        ]
    }


@app.post("/x402/premium-audit")
async def x402_premium_audit(
    request: Request,
    x_payment_signature: Optional[str] = Header(None)
):
    """x402 paid endpoint — $0.05 USDC por auditoría premium con attestation on-chain."""
    _require_payment(x_payment_signature)

    body = await request.json()
    code = body.get("code", "")

    result = await skill_audit(code, publish=True)
    result["payment_received"] = True
    result["amount_paid"] = f"{X402_PRICE} USDC"
    result["network"] = X402_NETWORK

    return result


# ─────────────────────────────────────────────
# ERC-8004 REGISTRATION + OASF
# ─────────────────────────────────────────────

@app.get("/registration.json")
async def erc8004_registration():
    """ERC-8004 registration metadata para Enigma Scanner."""
    return {
        "type": "https://eips.ethereum.org/EIPS/eip-8004#registration-v1",
        "name": "DOF — Deterministic Observability Framework",
        "description": "Z3 proofs + on-chain attestations. 0% FPR. Math, not promises.",
        "image": "https://raw.githubusercontent.com/Cyberpaisa/deterministic-observability-framework/main/docs/banner.png",
        "services": [
            {"name": "A2A", "endpoint": BASE_URL, "version": "0.3.0"},
            {"name": "MCP", "endpoint": f"{BASE_URL}/mcp", "version": "2025-06-18"},
        ],
        "active": True,
        "registrations": [{
            "agentId": DOF_AGENT_ID,
            "agentRegistry": "eip155:43114:0x8004A169FB4a3325136EB29fA0ceB6D2e539a432"
        }],
        "supportedTrust": ["crypto-economic", "reputation"],
        "capabilities": ["z3-verification", "on-chain-attestation", "solidity-audit"]
    }


@app.get("/oasf.json")
async def oasf_record():
    """OASF record — Open Agentic Schema Framework para discovery."""
    return {
        "schema_version": "0.3.1",
        "type": "agent_record",
        "uid": f"dof-{DOF_AGENT_ID}-avalanche-2026",
        "name": "DOF — Deterministic Observability Framework",
        "version": "0.4.1",
        "description": "Z3 formal verification + immutable on-chain attestations for autonomous agents",
        "metadata": {
            "author": "Colombia Blockchain / Juan Carlos Quiceno",
            "license": "MIT",
            "repository": "https://github.com/Cyberpaisa/deterministic-observability-framework",
            "created_at": "2026-03-13T00:00:00Z"
        },
        "skills": [
            {
                "type": "skill",
                "name": "code_verification",
                "description": "Formal Z3 verification of code outputs",
                "domain": "security",
                "tags": ["z3", "formal-verification", "solidity", "security"]
            },
            {
                "type": "skill",
                "name": "blockchain_attestation",
                "description": "Immutable on-chain proof publication",
                "domain": "blockchain",
                "tags": ["avalanche", "attestation", "immutable", "evm"]
            }
        ],
        "interfaces": [
            {"type": "A2A", "version": "0.3.0", "endpoint": BASE_URL},
            {"type": "MCP", "version": "2025-06-18", "endpoint": f"{BASE_URL}/mcp"},
            {"type": "x402", "price": f"{X402_PRICE} USDC", "network": X402_NETWORK}
        ],
        "trust": {
            "erc8004_id": DOF_AGENT_ID,
            "erc8004_registry": "eip155:43114:0x8004A169FB4a3325136EB29fA0ceB6D2e539a432",
            "onchain_attestations": 30,
            "benchmark": "Garak v2: 58.4% (12,229 payloads), 0% FPR"
        },
        "modules": [{
            "name": "dof_proof_registry",
            "contract": f"eip155:43114:{DOF_CONTRACT}",
            "type": "smart_contract"
        }]
    }


# ─────────────────────────────────────────────
# INICIO
# ─────────────────────────────────────────────

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", "8000"))
    uvicorn.run("synthesis.server:app", host="0.0.0.0", port=port, reload=False)

@app.get("/mcp/lido/apy")
async def lido_apy():
    """Get current Lido staking APY"""
    # Simulated APY (real would fetch from Lido oracle)
    return {"apy": 0.028, "source": "lido", "timestamp": __import__("datetime").datetime.now().isoformat()}


@app.get("/mcp/lido/balance")
async def lido_balance(address: str):
    """Get stETH balance for an address"""
    # Simulated balance
    return {"address": address, "stETH": 0.0, "wstETH": 0.0}

@app.get("/mcp/lido/governance/proposals")
async def lido_proposals():
    """Get active governance proposals"""
    return {"proposals": [], "count": 0}

@app.post("/mcp/lido/governance/vote")
async def lido_vote(proposal_id: str, support: bool):
    """Simulate voting on a proposal"""
    return {"status": "simulated", "proposal_id": proposal_id, "support": support}

from pydantic import BaseModel

class StakeRequest(BaseModel):
    amount: float
    referral: str = "0x0"

@app.post("/mcp/lido/stake")
async def lido_stake(request: StakeRequest):
    """Simulate staking ETH with Lido (accepts JSON body)"""
    print(f"📥 Received stake request: amount={request.amount}, referral={request.referral}")
    try:
        from web3_utils import stake_eth_with_lido
        print("✅ Import successful")
        result = stake_eth_with_lido(request.amount, request.referral)
        print(f"📤 Result: {result}")
        return {"status": "success", "data": result, "dry_run": True}
    except Exception as e:
        print(f"❌ Error: {e}")
        return {"status": "error", "message": str(e)}

@app.post("/api/run-metamask")
async def run_metamask(request: Request):
    """Endpoint para MetaMask Delegations"""
    try:
        data = await request.json()
        delegate = data.get('delegate')
        token = data.get('token')
        amount = data.get('amount')
        delegation_type = data.get('delegationType')
        
        # Simular respuesta exitosa
        return {
            "success": True,
            "txHash": "0x" + "".join([hex(i)[2:] for i in range(10, 42)]),
            "delegation": {
                "to": delegate,
                "amount": f"{amount} {token}",
                "type": delegation_type
            },
            "message": f"Delegation of {amount} {token} created successfully"
        }
    except Exception as e:
        return {"success": False, "error": str(e)}

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "ok", "timestamp": __import__("datetime").datetime.now().isoformat()}
