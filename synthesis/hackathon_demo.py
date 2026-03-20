#!/usr/bin/env python3
"""
DOF Hackathon Demo — Synthesis 2026
=====================================
Unified demo for 3 tracks:
  1. Synthesis Open Track ($28,308)
  2. ERC-8004 Agents With Receipts ($4,000)
  3. Let the Agent Cook — No Humans Required ($4,000)

Runs the complete DOF pipeline in ~60 seconds with ZERO human input:
  Identity → LLM Task → Governance → Z3 Proof → On-Chain → Supervisor

Usage:
  python3 synthesis/hackathon_demo.py
  python3 synthesis/hackathon_demo.py --dry-run   # No on-chain TX
"""

import os
import sys
import json
import time
import hashlib
import argparse
from datetime import datetime, timezone
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from dotenv import load_dotenv
load_dotenv(PROJECT_ROOT / ".env")
# Also load parent .env for LLM keys
load_dotenv(PROJECT_ROOT.parent / ".env")

# ─── DOF Core Imports ───
from core.governance import ConstitutionEnforcer, GovernanceResult
from core.z3_verifier import Z3Verifier, ProofResult
from core.supervisor import MetaSupervisor, SupervisorVerdict
from core.proof_hash import ProofSerializer

# ─── Constants ───
AGENT_ID = 1686
ERC8004_TOKEN = 31013
ERC8004_TX = "0x7362ef41605e430aba3998b0888e7886c04d65673ce89aa12e1abdf7cffcada4"
TEAM_ID = "99b0668bce9f40389ef68ad233bf71a8"

# ─── Output ───
RESULTS = {}
STEP_NUM = 0

def step(title: str):
    global STEP_NUM
    STEP_NUM += 1
    print(f"\n{'='*60}")
    print(f"STEP {STEP_NUM}: {title}")
    print(f"{'='*60}")


def main(dry_run: bool = False):
    start_time = time.time()
    print("=" * 60)
    print("DOF AGENT #1686 — SYNTHESIS HACKATHON 2026")
    print("Deterministic Observability Framework — Live Demo")
    print("=" * 60)
    print(f"Time: {datetime.now(timezone.utc).isoformat()}")
    print(f"Mode: {'DRY RUN (no on-chain TX)' if dry_run else 'LIVE (real on-chain TX)'}")
    print()

    # ─── STEP 1: IDENTITY (ERC-8004 Track) ───
    step("IDENTITY — ERC-8004 Agent Registration")
    identity = {
        "agent": f"DOF Agent #{AGENT_ID}",
        "erc8004_token": f"#{ERC8004_TOKEN}",
        "registration_tx": ERC8004_TX,
        "explorer": f"https://basescan.org/tx/{ERC8004_TX}",
        "chain": "Base Mainnet (chain_id: 8453)",
        "contract": "0x8004A169FB4a3325136EB29fA0ceB6D2e539a432",
    }
    for k, v in identity.items():
        print(f"  {k}: {v}")
    RESULTS["identity"] = identity

    # ─── STEP 2: AUTONOMOUS TASK (Agent Cook Track) ───
    step("AUTONOMOUS TASK — Agent Receives Work (Zero Human Input)")
    task = {
        "type": "solidity_audit",
        "input": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
contract Vault {
    mapping(address => uint256) public balances;
    function deposit() external payable {
        balances[msg.sender] += msg.value;
    }
    function withdraw() external {
        uint256 amount = balances[msg.sender];
        (bool ok, ) = msg.sender.call{value: amount}("");
        require(ok);
        balances[msg.sender] = 0; // CEI violation: state after external call
    }
}""",
        "objective": "Audit for reentrancy vulnerabilities",
        "human_input": False,
    }
    print(f"  Task type: {task['type']}")
    print(f"  Objective: {task['objective']}")
    print(f"  Human input: {task['human_input']}")
    print(f"  Code: {len(task['input'])} chars of Solidity")
    RESULTS["task"] = {"type": task["type"], "objective": task["objective"]}

    # ─── STEP 3: LLM ANALYSIS (Multi-Provider Fallback) ───
    step("LLM ANALYSIS — Multi-Provider Fallback Chain")
    llm_output = None
    llm_model = None
    llm_start = time.time()

    try:
        from litellm import Router
        model_list = [
            {
                "model_name": "hackathon",
                "litellm_params": {
                    "model": "cerebras/qwen-3-235b-a22b-instruct-2507",
                    "api_key": os.environ.get("CEREBRAS_API_KEY", ""),
                    "max_tokens": 2048,
                },
                "model_info": {"id": "cerebras-qwen3"},
            },
            {
                "model_name": "hackathon",
                "litellm_params": {
                    "model": "groq/openai/gpt-oss-120b",
                    "api_key": os.environ.get("GROQ_API_KEY", ""),
                    "max_tokens": 2048,
                },
                "model_info": {"id": "groq-gpt-oss"},
            },
            {
                "model_name": "hackathon",
                "litellm_params": {
                    "model": "groq/moonshotai/kimi-k2-instruct",
                    "api_key": os.environ.get("GROQ_API_KEY", ""),
                    "max_tokens": 2048,
                },
                "model_info": {"id": "groq-kimi-k2"},
            },
            {
                "model_name": "hackathon",
                "litellm_params": {
                    "model": "mistral/mistral-large-latest",
                    "api_key": os.environ.get("MISTRAL_API_KEY", ""),
                    "max_tokens": 2048,
                },
                "model_info": {"id": "mistral-large"},
            },
        ]
        router = Router(
            model_list=model_list,
            num_retries=3,
            retry_after=2,
            allowed_fails=3,
            cooldown_time=15,
        )
        print("  Providers: Cerebras → Groq GPT-OSS → Groq Kimi K2 → Mistral")
        print("  Calling LLM (automatic fallback)...")

        response = router.completion(
            model="hackathon",
            messages=[{
                "role": "user",
                "content": f"You are a Solidity security auditor. Audit this contract for vulnerabilities, especially reentrancy. Be concise but thorough.\n\n{task['input']}"
            }],
            timeout=60,
        )
        llm_output = response.choices[0].message.content
        llm_model = response.model or "unknown"
        llm_ms = int((time.time() - llm_start) * 1000)
        print(f"  Model used: {llm_model}")
        print(f"  Response: {len(llm_output)} chars in {llm_ms}ms")
        print(f"  Preview: {llm_output[:200]}...")
    except Exception as e:
        print(f"  LLM call failed: {e}")
        print("  Using fallback deterministic analysis...")
        llm_output = (
            "CRITICAL: Reentrancy vulnerability detected in withdraw() function. "
            "The contract violates the Checks-Effects-Interactions (CEI) pattern. "
            "State update (balances[msg.sender] = 0) occurs AFTER the external call "
            "(msg.sender.call{value: amount}). An attacker can re-enter withdraw() "
            "before the balance is zeroed. FIX: Move balances[msg.sender] = 0 BEFORE "
            "the external call. Alternatively, use ReentrancyGuard from OpenZeppelin."
        )
        llm_model = "deterministic-fallback"
        llm_ms = int((time.time() - llm_start) * 1000)
        print(f"  Fallback analysis: {len(llm_output)} chars in {llm_ms}ms")

    RESULTS["llm"] = {
        "model": llm_model,
        "chars": len(llm_output),
        "duration_ms": llm_ms,
    }

    # ─── STEP 4: GOVERNANCE CHECK (Deterministic, Zero LLM) ───
    step("GOVERNANCE — Constitution Enforcement (Zero LLM)")
    enforcer = ConstitutionEnforcer()
    gov_result: GovernanceResult = enforcer.check(llm_output)
    print(f"  Passed: {gov_result.passed}")
    print(f"  Score: {gov_result.score:.2f}")
    print(f"  Violations: {gov_result.violations or 'None'}")
    print(f"  Warnings: {gov_result.warnings or 'None'}")
    print(f"  Method: Deterministic rules (NO LLM involved)")
    RESULTS["governance"] = {
        "passed": gov_result.passed,
        "score": gov_result.score,
        "violations": gov_result.violations,
        "warnings": gov_result.warnings,
    }

    # ─── STEP 5: Z3 FORMAL VERIFICATION ───
    step("Z3 FORMAL VERIFICATION — Mathematical Proofs")
    verifier = Z3Verifier()
    z3_results = verifier.verify_all()
    proof_hashes = []
    for proof in z3_results:
        status = "PROVEN" if proof.result == "VERIFIED" else "FAILED"
        print(f"  [{status}] {proof.theorem_name}: {proof.description}")
        print(f"          Time: {proof.proof_time_ms:.1f}ms | Z3: {proof.z3_version}")
        # Compute keccak256 proof hash
        proof_data = f"{proof.theorem_name}:{proof.result}:{proof.proof_time_ms}"
        proof_hash = "0x" + hashlib.sha3_256(proof_data.encode()).hexdigest()
        proof_hashes.append(proof_hash)
        print(f"          Hash: {proof_hash[:20]}...")

    all_proven = all(p.result == "VERIFIED" for p in z3_results)
    print(f"\n  Result: {len(z3_results)}/{len(z3_results)} theorems {'PROVEN' if all_proven else 'INCOMPLETE'}")

    # Combined proof hash for on-chain attestation
    combined = hashlib.sha3_256(
        "|".join(proof_hashes).encode()
    ).hexdigest()
    combined_hash = f"0x{combined}"
    print(f"  Combined proof hash: {combined_hash[:30]}...")

    RESULTS["z3"] = {
        "theorems_proven": sum(1 for p in z3_results if p.result == "VERIFIED"),
        "total_theorems": len(z3_results),
        "all_proven": all_proven,
        "combined_proof_hash": combined_hash,
        "individual_hashes": proof_hashes,
    }

    # ─── STEP 6: ON-CHAIN ATTESTATION ───
    step("ON-CHAIN ATTESTATION — Publish Proof to Avalanche")
    on_chain_result = None

    try:
        from core.chain_adapter import DOFChainAdapter
        adapter = DOFChainAdapter.from_chain_name("avalanche", dry_run=dry_run)
        print(f"  Chain: {adapter.config.name} (chain_id: {adapter.config.chain_id})")
        print(f"  Contract: {adapter.config.contract_address}")
        print(f"  Agent ID: {AGENT_ID}")
        print(f"  Proof hash: {combined_hash[:30]}...")

        metadata = json.dumps({
            "demo": "hackathon_2026",
            "task": task["type"],
            "governance_score": gov_result.score,
            "z3_proven": all_proven,
            "llm_model": llm_model,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        })

        private_key = os.environ.get("AVALANCHE_PRIVATE_KEY") or os.environ.get("DOF_PRIVATE_KEY")
        if not private_key and not dry_run:
            print("  WARNING: No private key found. Running as dry run.")
            dry_run = True
            adapter = DOFChainAdapter.from_chain_name("avalanche", dry_run=True)

        on_chain_result = adapter.publish_attestation(
            proof_hash=combined_hash,
            agent_id=AGENT_ID,
            metadata=metadata,
            private_key=private_key,
        )

        print(f"  Status: {on_chain_result['status']}")
        if on_chain_result.get("tx_hash"):
            print(f"  TX Hash: {on_chain_result['tx_hash']}")
        if on_chain_result.get("explorer_url"):
            print(f"  Explorer: {on_chain_result['explorer_url']}")
        if on_chain_result.get("gas_used"):
            print(f"  Gas used: {on_chain_result['gas_used']}")

    except Exception as e:
        print(f"  On-chain publish failed: {e}")
        on_chain_result = {"status": "error", "error": str(e)}

    RESULTS["on_chain"] = on_chain_result or {}

    # ─── STEP 7: SUPERVISOR VERDICT ───
    step("SUPERVISOR — Meta-Evaluation")
    supervisor = MetaSupervisor()
    verdict: SupervisorVerdict = supervisor.evaluate(
        output=llm_output,
        original_input=task["objective"],
    )
    print(f"  Decision: {verdict.decision}")
    print(f"  Score: {verdict.score:.2f}/10")
    print(f"  Quality (Q=0.40): {verdict.quality:.1f}")
    print(f"  Actionability (A=0.25): {verdict.actionability:.1f}")
    print(f"  Completeness (C=0.20): {verdict.completeness:.1f}")
    print(f"  Factuality (F=0.15): {verdict.factuality:.1f}")
    if verdict.reasons:
        print(f"  Reasons: {', '.join(verdict.reasons)}")
    RESULTS["supervisor"] = {
        "decision": verdict.decision,
        "score": verdict.score,
        "quality": verdict.quality,
        "actionability": verdict.actionability,
        "completeness": verdict.completeness,
        "factuality": verdict.factuality,
    }

    # ─── STEP 8: SUMMARY ───
    total_ms = int((time.time() - start_time) * 1000)
    step("SUMMARY — Complete Pipeline Results")

    print(f"""
  Agent: DOF #{AGENT_ID} (ERC-8004 #{ERC8004_TOKEN})
  Task: {task['type']} — {task['objective']}
  Human Input: NONE (fully autonomous)

  LLM: {llm_model} ({RESULTS['llm']['chars']} chars, {RESULTS['llm']['duration_ms']}ms)
  Governance: {'PASSED' if gov_result.passed else 'BLOCKED'} (score: {gov_result.score:.2f})
  Z3 Proofs: {RESULTS['z3']['theorems_proven']}/{RESULTS['z3']['total_theorems']} PROVEN
  On-Chain: {RESULTS.get('on_chain', {}).get('status', 'N/A')}
  Supervisor: {verdict.decision} ({verdict.score:.2f}/10)

  Total Time: {total_ms}ms

  On-Chain Evidence:
    ERC-8004 Registration: https://basescan.org/tx/{ERC8004_TX}
    Avalanche Contract: https://snowtrace.io/address/{adapter.config.contract_address if 'adapter' in dir() else '0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6'}
    Proof Hash: {combined_hash[:30]}...
""")

    if on_chain_result and on_chain_result.get("tx_hash"):
        print(f"    Attestation TX: {on_chain_result.get('explorer_url', on_chain_result['tx_hash'])}")

    print("  \"Agent acted autonomously. Math proved it. Blockchain recorded it.\"")
    print()

    RESULTS["total_ms"] = total_ms
    RESULTS["timestamp"] = datetime.now(timezone.utc).isoformat()

    # Save results to JSON
    results_path = PROJECT_ROOT / "synthesis" / "demo_results.json"
    with open(results_path, "w") as f:
        json.dump(RESULTS, f, indent=2, default=str)
    print(f"  Results saved to: {results_path}")

    # Save to JSONL audit log
    log_path = PROJECT_ROOT / "logs" / "hackathon_demo.jsonl"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with open(log_path, "a") as f:
        f.write(json.dumps(RESULTS, default=str) + "\n")
    print(f"  Audit log: {log_path}")

    print("\n" + "=" * 60)
    print("DEMO COMPLETE — DOF Agent #1686 — Synthesis 2026")
    print("=" * 60)

    return RESULTS


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="DOF Hackathon Demo")
    parser.add_argument("--dry-run", action="store_true", help="Skip real on-chain transactions")
    args = parser.parse_args()
    main(dry_run=args.dry_run)
