# DOF-MESH — Deterministic Observability Framework

<div align="center">

### "Most frameworks verify what happened. DOF-MESH verifies what is *about to happen*."

**Conflux Global Hackfest 2026 Submission**

[![Conflux](https://img.shields.io/badge/Conflux-eSpace_Testnet-1AAB9B?style=for-the-badge)](https://evmtestnet.confluxscan.io/address/0x554cCa8ceBE30dF95CeeFfFBB9ede5bA7C7A9B83)
[![Gasless](https://img.shields.io/badge/Gasless-SponsorWhitelistControl_Active-00C853?style=for-the-badge)](https://evmtestnet.confluxscan.io/tx/014b6bedde7fa449d48822752371bc6ee275d62325117a66ef7d8dfbea52d3b7)
[![Z3](https://img.shields.io/badge/Z3_Formal_Proofs-4%2F4_PROVEN-6c5ce7?style=for-the-badge)](./CONFLUX_PROOF.md)
[![Tests](https://img.shields.io/badge/Tests-4%2C308_passing-brightgreen?style=flat-square)]()
[![Chains](https://img.shields.io/badge/Chains-8_active-blue?style=flat-square)]()
[![License](https://img.shields.io/badge/License-Apache_2.0-blue?style=flat-square)](LICENSE)

[dofmesh.com](https://dofmesh.com) · [On-Chain Contract](https://evmtestnet.confluxscan.io/address/0x554cCa8ceBE30dF95CeeFfFBB9ede5bA7C7A9B83) · [Full Proof Evidence](./CONFLUX_PROOF.md) · [Quick Start](#quick-start)

</div>

---

## The Problem

AI agents act autonomously — but nobody can prove *what* they decided, *why*, or whether governance was actually enforced. Trust is assumed. Audits are manual. The result: autonomous systems with no verifiable correctness guarantees.

## The Solution

DOF-MESH is a **deterministic governance framework** that mathematically proves every AI agent action is compliant *before* it executes. The verification path contains **zero LLM calls** — every decision is deterministic: regex, AST analysis, Z3 theorems, formal scoring.

```
Agent Output
     ↓
[1] Constitution    →  Hard rules block. Soft rules warn. YAML-defined. Zero LLM.
     ↓
[2] AST Verifier   →  Static analysis of any generated code before execution.
     ↓
[3] Z3 Verifier    →  4 formal theorems PROVEN in <35ms:
                       GCR_INVARIANT · SS_FORMULA · SS_MONOTONICITY · SS_BOUNDARIES
     ↓
[4] TRACER Score   →  Multi-dimensional quality score (Quality · Accuracy · Compliance · Format)
     ↓
[5] Proof Hash     →  keccak256 of full governance payload — immutable fingerprint
     ↓
[6] Conflux TX     →  Proof recorded on-chain. Gasless. Permanent. Publicly verifiable.
```

---

## Conflux Integration

### Why Conflux

Conflux has one capability no other EVM chain offers natively: **Gas Sponsorship via `SponsorWhitelistControl`**. This is not a wrapper or workaround — it is a Core Space internal contract (`0x0888000000000000000000000000000000000001`) that lets a deployer sponsor all transaction fees for users of a given contract.

For a governance framework, this is the right primitive: **agents prove their compliance on-chain without needing to hold any CFX**. The protocol sponsors the gas. Zero friction for agent adoption.

### Live Contract — DOFProofRegistry

| Field | Value |
|---|---|
| Contract Address | `0x554cCa8ceBE30dF95CeeFfFBB9ede5bA7C7A9B83` |
| Network | Conflux eSpace Testnet (Chain ID: 71) |
| RPC | `https://evmtestnet.confluxrpc.com` |
| Proofs Registered | 36+ |
| Gasless Status | **Active** — SponsorWhitelistControl configured April 6, 2026 |
| Explorer | [View on ConfluxScan](https://evmtestnet.confluxscan.io/address/0x554cCa8ceBE30dF95CeeFfFBB9ede5bA7C7A9B83) |

### Gas Sponsorship Setup — Verified On-Chain

Three transactions activated gasless operation on April 6, 2026:

| Step | Function | CFX Deposited | TX Hash | Status |
|---|---|---|---|---|
| 1 | `setSponsorForGas` | 10 CFX (upper bound: 1,000,000 drip) | [`014b6bed...d3b7`](https://evmtestnet.confluxscan.io/tx/014b6bedde7fa449d48822752371bc6ee275d62325117a66ef7d8dfbea52d3b7) | ✅ Confirmed |
| 2 | `setSponsorForCollateral` | 10 CFX | [`d6199877...c9f`](https://evmtestnet.confluxscan.io/tx/d6199877d1ff08c204e3ef60dd914852d305bdacde23c29058067c20e621cc9f) | ✅ Confirmed |
| 3 | `addPrivilegeByAdmin` | — (global whitelist `0x00...0`) | [`2e47f3fd...2a3`](https://evmtestnet.confluxscan.io/tx/2e47f3fd80d82c251a1c572cadbc2b87c377eeb2a092893094d939ce676862a3) | ✅ Confirmed |

**Result:** Any address can register governance proofs on `DOFProofRegistry` at zero gas cost.

### Hackathon Attestation TX

The complete governance cycle was executed and attested on-chain for this hackathon. The proof payload is encoded directly in the transaction log:

| Field | Value |
|---|---|
| TX Hash | [`0x6994475597c4052f...b2343`](https://evmtestnet.confluxscan.io/tx/0x6994475597c4052f33012458ed75fac6458b53a88f2fa991ff0e3943ab9b2343) |
| Block | 248,350,045 |
| Agent ID | #1687 |
| Decoded Payload | `dof-v0.6.0 conflux-hackathon z3=4/4 tracer=0.504` |
| Timestamp | April 6, 2026 |
| Sponsoring Wallet | `0xEAFdc9C3019fC80620f16c30313E3B663248A655` |

---

## Quick Start

```bash
git clone https://github.com/Cyberpaisa/deterministic-observability-framework
cd deterministic-observability-framework
pip install -r requirements.txt

# Run full governance cycle — dry-run, no wallet required
python3 scripts/conflux_demo.py --dry-run

# Run with real Conflux TX (add CONFLUX_PRIVATE_KEY to .env)
python3 scripts/conflux_demo.py
```

**Expected output (real mode):**

```
━━━ STEP 1: Constitution (zero LLM) ━━━
  Passed: True  |  Score: 1.0000  |  Violations: 0  |  Warnings: 1

━━━ STEP 2: Z3 Formal Verification ━━━
  GCR invariant:    PROVEN (24.2ms)
  SS formula:       PROVEN (2.4ms)
  SS monotonicity:  PROVEN (7.7ms)
  SS boundaries:    PROVEN (0.5ms)
  ✅ 4/4 PROVEN — 34.8ms total

━━━ STEP 3: TRACER Score ━━━
  ✅ 0.504/1.0  (Q=0.6  A=0.45  C=0.62  F=0.5)

━━━ STEP 4: Proof Hash ━━━
  0x05235c88f0f826c279...781e2d6f

━━━ STEP 5: On-Chain Attestation (Conflux Testnet) ━━━
  Contract: 0x554cCa8ceBE30dF95CeeFfFBB9ede5bA7C7A9B83
  Chain ID: 71
  ✅ TX confirmed — gasless

━━━ STEP 6: Summary ━━━
  Constitution: ✅  Z3: ✅ 4/4  TRACER: ✅  Conflux: ✅

╔══════════════════════════════════════════════════════╗
║    DOF-MESH x Conflux — Global Hackfest 2026         ║
║  Agent acted autonomously. Math proved it.           ║
║  Blockchain recorded it. On Conflux.                 ║
╚══════════════════════════════════════════════════════╝
```

---

## Architecture

```
DOF-MESH v0.6.0
│
├── 7-Layer Governance Pipeline
│   ├── Constitution          — YAML rules, zero LLM, HARD_RULES block, SOFT_RULES warn
│   ├── AST Verifier          — static code analysis before execution
│   ├── Tool Hook Gate PRE    — intercepts all tool calls before they run
│   ├── Supervisor Engine     — Q(0.4) + A(0.25) + C(0.2) + F(0.15) cross-turn monitoring
│   ├── Adversarial Guard     — red/blue pipeline, 11 injection patterns
│   ├── Memory Layer          — ChromaDB + reproducible session state
│   └── Z3 SMT Verifier       — 4/4 invariants PROVEN (GCR · SS · SS_MONO · SS_BOUND)
│
├── Conflux Layer
│   ├── core/adapters/conflux_gateway.py   — web3.py v7 compatible gateway
│   ├── SponsorWhitelistControl            — 0x0888...0001, gasless for all users
│   └── DOFProofRegistry.sol               — same ABI deployed across 8 chains
│
├── 4,308 tests  ·  142 modules  ·  57K+ LOC
├── 238+ autonomous cycles in logs/daemon/cycles.jsonl
└── 8 active chains: Avalanche · Base · Celo · Conflux · Polygon · SKALE · Fuji · Base Sepolia
```

### ConfluxGateway Usage

```python
from core.adapters.conflux_gateway import ConfluxGateway
from core.chain_adapter import DOFChainAdapter

# Connect to Conflux eSpace Testnet
gw = ConfluxGateway(use_testnet=True)

# Access SponsorWhitelistControl (internal contract)
sponsor = gw.get_sponsor_contract()

# Publish a governance proof — gasless for the caller
adapter = DOFChainAdapter.from_chain_name("conflux_testnet")
result = adapter.publish_attestation(
    proof_hash="0x...",
    agent_id=1687,
    metadata="dof-v0.6.0 z3=4/4 tracer=0.504"
)
# → {"tx_hash": "0x...", "chain": "conflux_testnet"}
```

---

## Test the Conflux Integration

```bash
# Conflux-specific tests (9/9)
python3 -m unittest tests.test_conflux_gateway tests.test_conflux_integration -v

# Full test suite (4,308 tests)
python3 -m unittest discover -s tests

# Run demo in dry-run (no wallet, no gas, 6/6 steps)
python3 scripts/conflux_demo.py --dry-run
```

---

## Verified Metrics

| Metric | Value | How to Verify |
|---|---|---|
| Tests passing | **4,308** | `python3 -m unittest discover -s tests` |
| Z3 theorems proven | **4/4** | `python3 scripts/conflux_demo.py --dry-run` |
| Z3 proof time | **34.8ms** | `logs/z3_proofs.json` |
| Autonomous cycles logged | **238+** | `logs/daemon/cycles.jsonl` |
| On-chain proofs (Conflux) | **36+** | [ConfluxScan](https://evmtestnet.confluxscan.io/address/0x554cCa8ceBE30dF95CeeFfFBB9ede5bA7C7A9B83) |
| On-chain proofs (all chains) | **80+** | 8 chains active |
| LLM calls in governance path | **0** | `grep -rn "llm_call" core/governance.py` → 0 |
| Gasless sponsorship | **Active** | [3 TXs confirmed](./CONFLUX_PROOF.md) |
| Codebase | **57K+ LOC · 142 modules** | `find core/ -name "*.py" \| wc -l` |

---

## Why DOF-MESH Stands Out

| What Judges Want to See | DOF-MESH |
|---|---|
| Real on-chain TX with meaningful payload | ✅ `conflux-hackathon z3=4/4` encoded in block 248,350,045 |
| Native use of Conflux features | ✅ SponsorWhitelistControl — gasless proof registration |
| Formal/mathematical verification | ✅ Z3 SMT, 4 theorems, not "pretty confident" |
| Working code with tests | ✅ 4,308 tests, clone and run in 3 commands |
| Autonomous operation evidence | ✅ 238+ cycles in logs, not a prepared demo |
| Zero LLM in trust path | ✅ Governance is pure deterministic logic |

---

## Full On-Chain Evidence

All transaction hashes, block numbers, decoded payloads, and gasless verification:

**→ [CONFLUX_PROOF.md](./CONFLUX_PROOF.md)**

---

## Contact

**Cyber Paisa** — Enigma Group, Medellín, Colombia  
GitHub: [Cyberpaisa/deterministic-observability-framework](https://github.com/Cyberpaisa/deterministic-observability-framework)  
Site: [dofmesh.com](https://dofmesh.com) · X: [@Cyber_paisa](https://x.com/Cyber_paisa)

---

> *"Agent acted autonomously. Math proved it. Blockchain recorded it. On Conflux."*
