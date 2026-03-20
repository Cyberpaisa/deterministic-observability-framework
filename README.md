# DOF -- Deterministic Observability Framework

<div align="center">

### Agent acted autonomously. Math proved it. Blockchain recorded it.

**DOF Agent #1686 | ERC-8004 Token #31013 | Synthesis Hackathon 2026**

[![Live Dashboard](https://img.shields.io/badge/Live_Dashboard-Vercel-000?style=for-the-badge&logo=vercel)](https://dof-agent-web.vercel.app/)
[![ERC-8004](https://img.shields.io/badge/ERC--8004-Agent_%231686-blueviolet?style=for-the-badge)](https://basescan.org/tx/0x7362ef41605e430aba3998b0888e7886c04d65673ce89aa12e1abdf7cffcada4)
[![On-Chain](https://img.shields.io/badge/Avalanche-0x154a3F49...26F6-e84142?style=for-the-badge&logo=avalanche)](https://basescan.org/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)

[![Tests](https://img.shields.io/badge/Tests-986_passing-brightgreen?style=flat-square)]()
[![Cycles](https://img.shields.io/badge/Autonomous_Cycles-238+-orange?style=flat-square)]()
[![Attestations](https://img.shields.io/badge/On--Chain_Attestations-48+-blue?style=flat-square)]()
[![LOC](https://img.shields.io/badge/LOC-27K+-lightgrey?style=flat-square)]()
[![License](https://img.shields.io/badge/License-Apache_2.0-blue?style=flat-square)](LICENSE)

[Live Demo](https://dof-agent-web.vercel.app/) | [GitHub](https://github.com/Cyberpaisa/deterministic-observability-framework) | [On-Chain Proof](https://basescan.org/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6) | [Journal](docs/journal.md)

</div>

---

## The Problem

AI agents today are black boxes. They act, but nobody can prove _what_ they did, _why_ they did it, or whether their governance was actually enforced. Trust is assumed. Audits are manual. Proofs are nonexistent.

## Our Solution

DOF is a **deterministic governance and observability framework** for autonomous AI agents. Every decision passes through a mathematically verified pipeline -- no LLM in the governance loop, no probabilistic shortcuts, no trust assumptions.

The pipeline is simple and absolute:

```
Identity --> Task --> LLM --> Governance --> Z3 Proof --> On-Chain --> Supervisor
```

Every agent action produces a cryptographic receipt. Every governance decision is formally verified. Every proof is recorded on-chain. The result: an autonomous agent whose behavior is **provably correct, publicly auditable, and permanently recorded**.

---

## Hackathon Tracks

### Track 1: Synthesis Open Track -- $28,308

A complete AI agent governance framework with deterministic observability. 70+ core modules, 986 tests, 18 skills, 5 ADK patterns. The agent discovers tasks, plans execution, runs LLM inference across multiple providers, enforces governance without LLM, generates Z3 formal proofs, records attestations on-chain, and supervises its own output quality.

### Track 2: ERC-8004 Agents With Receipts -- $4,000

Every autonomous cycle produces a signed ERC-8004 receipt containing the agent identity, task hash, governance result, Z3 proof hash, and chain attestation. 38+ receipts recorded on Avalanche C-Chain and Base Mainnet. Fully verifiable on Basescan.

### Track 3: Let the Agent Cook -- $4,000

238+ autonomous cycles executed with **zero human input**. The agent runs its own discovery loop, selects tasks, executes them, verifies results, commits code, and attests on-chain -- every 30 minutes, 24/7. The journal documents every cycle.

### Track 4: Private Agents -- $11,500

Privacy-preserving agent governance. DOF enforces data boundaries deterministically -- no internals exposed, no PII leakage. The `PrivacyLeakGenerator` runs 4 attack vectors (PII, API keys, memory, tool inputs) and the governance layer blocks 71%+ without any LLM in the loop.

### Track 5: Agent Services on Base -- $5,000

ERC-8004 identity minted on Base Mainnet (Token #31013). Agent receipts and proof hashes anchored on-chain via `DOFChainAdapter`. Every autonomous cycle produces a verifiable receipt on Basescan.

### Track 6: Best Agent on Celo -- $5,000

Multi-chain attestation support. DOF agents publish governance proofs across EVM chains -- Avalanche, Base, and Celo. The `DOFChainAdapter` abstracts chain-specific logic, enabling portable agent identity.

### Track 7: ERC-8183 Intent Protocol -- $2,000

Agent intent declarations verified by Z3 formal proofs before on-chain execution. The agent declares what it intends to do, Z3 proves the intent is safe, and only then does the chain adapter execute.

### Track 8: Best Self Protocol -- $1,000

Self-sovereign agent identity with deterministic trust scoring. The `TrustGateway` assigns trust levels based on governance compliance, Z3 proof history, and on-chain reputation -- no central authority.

### Track 9: Agents That Pay -- $1,500

Autonomous payment flows governed by constitution rules. The MPP (Machine-to-Machine Payment Protocol) pattern ensures agents can pay for services while safety guardrails prevent unauthorized spending.

### Track 10: Mechanism Design -- $1,000

Game-theoretic governance mechanisms with formal verification. Z3 proves incentive alignment properties -- agents cannot profit from violating governance rules, making compliance the dominant strategy.

---

## Architecture

```
+===================================================================+
|                      DOF Agent #1686                              |
|                                                                   |
|  +-------------------------------------------------------------+ |
|  |                    INTERFACE LAYER                           | |
|  |  CLI | A2A Server | Telegram | Dashboard (Vercel) | Voice   | |
|  +-------------------------------------------------------------+ |
|                              |                                    |
|  +-------------------------------------------------------------+ |
|  |                   EXPERIMENT LAYER                           | |
|  |  ExperimentDataset | BatchRunner | Schema | Parametric Sweep | |
|  +-------------------------------------------------------------+ |
|                              |                                    |
|  +-------------------------------------------------------------+ |
|  |                 OBSERVABILITY LAYER                          | |
|  |  RunTrace | StepTrace | 5 Derived Metrics | JSONL Audit     | |
|  +-------------------------------------------------------------+ |
|                              |                                    |
|  +---------------------------+-------------------------------+   |
|  |     GOVERNANCE CORE       |       VERIFICATION CORE       |   |
|  |                           |                               |   |
|  |  ConstitutionEnforcer     |  Z3Verifier (4/4 PROVEN)     |   |
|  |  HARD rules --> block     |  Formal invariant proofs      |   |
|  |  SOFT rules --> warn      |  keccak256 proof hashes       |   |
|  |  ZERO LLM in governance   |  ASTVerifier + TransitionV.   |   |
|  +---------------------------+-------------------------------+   |
|                              |                                    |
|  +-------------------------------------------------------------+ |
|  |                    CORE INFRASTRUCTURE                       | |
|  |                                                             | |
|  |  crew_runner.py ---- Orchestration, retry x3, crew_factory  | |
|  |  providers.py ------ TTL backoff (5/10/20m), provider chains| |
|  |  supervisor.py ----- MetaSupervisor weighted scoring        | |
|  |  memory_manager.py - ChromaDB + HuggingFace embeddings      | |
|  |  checkpointing.py -- JSONL persistence per step             | |
|  |  skill_engine.py --- 18 skills, 5 ADK patterns              | |
|  |  metrics.py -------- JSONL logger with rotation             | |
|  +-------------------------------------------------------------+ |
|                              |                                    |
|  +---------------------------+-------------------------------+   |
|  |   8 SPECIALIZED AGENTS    |     ON-CHAIN LAYER            |   |
|  |   (config/agents.yaml)    |                               |   |
|  |                           |  DOFChainAdapter              |   |
|  |   16 Tools                |  Avalanche C-Chain            |   |
|  |   4 MCP Servers           |  Base Mainnet                 |   |
|  |                           |  Celo (multi-chain ready)     |   |
|  +---------------------------+-------------------------------+   |
+===================================================================+
```

---

## Core Components

| Component | What It Does |
|:----------|:-------------|
| **ConstitutionEnforcer** | Deterministic governance -- HARD rules block, SOFT rules warn. Zero LLM involvement. ~50 token constitution injected per agent. |
| **Z3Verifier** | 4 mathematical theorems formally PROVEN every cycle. Generates keccak256 proof hashes for on-chain recording. |
| **MetaSupervisor** | Weighted quality scoring: Q(0.40) + A(0.25) + C(0.20) + F(0.15). Outputs ACCEPT, RETRY, or ESCALATE. |
| **DOFChainAdapter** | Multi-chain attestation engine. Writes proof receipts to Avalanche, Base, and Celo. |
| **Skills Engine v2.0** | 18 skills across 5 ADK patterns: blockchain audit, formal verification, security analysis, and more. |
| **ProviderManager** | LiteLLM router across Cerebras, Groq, Mistral, SambaNova. TTL backoff, automatic failover, deterministic ordering. |

---

## The Numbers

| Metric | Value |
|:-------|------:|
| Unit tests | **986** |
| Autonomous cycles | **238+** |
| On-chain attestations | **48+** |
| Core modules | **70+** |
| Lines of code | **27,000+** |
| Z3 theorems | **4/4 PROVEN** |
| Skills | **18** |
| LLM providers | **4 (Cerebras, Groq, Mistral, SambaNova)** |
| Governance mode | **100% deterministic, 0% LLM** |

---

## Tech Stack

| Layer | Technology |
|:------|:-----------|
| Core Framework | Python 3.11+ |
| Formal Verification | Z3 Theorem Prover -- 4/4 invariants PROVEN |
| Blockchain | web3.py + Avalanche C-Chain + Base Mainnet |
| LLM Routing | LiteLLM Router (Cerebras, Groq, Mistral, SambaNova) |
| Dashboard | Next.js + Tailwind CSS on Vercel |
| Vector Memory | ChromaDB + HuggingFace embeddings (all-MiniLM-L6-v2) |
| Persistence | JSONL audit logs -- zero external telemetry dependencies |
| Protocols | A2A + MCP + ERC-8004 |

---

## On-Chain Identity

```
ERC-8004 Token:    #31013 -- Base Mainnet
Agent ID:          #1686
Registration TX:   0x7362ef41605e430aba3998b0888e7886c04d65673ce89aa12e1abdf7cffcada4
Contract:          0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6
Basescan:          https://basescan.org/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6
```

| Contract | Purpose | Network |
|:---------|:--------|:--------|
| DOFProofRegistry.sol | Agent action proofs registry | Base Sepolia |
| DOFPaygate.sol | x402 conditional micropayments | Base Sepolia |
| DOFGaslessProof.sol | Gasless proof submission | Status Network |
| DOFValidationRegistry.sol | Validation and trust scoring | Base Sepolia |

---

## Quick Start

```bash
# Clone and setup
git clone https://github.com/Cyberpaisa/deterministic-observability-framework.git
cd deterministic-observability-framework
git checkout hackathon
pip install -r requirements.txt

# Run the hackathon demo (dry run -- no API keys needed)
python3 synthesis/hackathon_demo.py --dry-run

# Run all 986 tests
python3 -m unittest discover tests/

# Run the interactive CLI (15 options)
python3 main.py

# Run a deterministic experiment (requires GROQ_API_KEY in .env)
python3 -c "
from core.experiment import run_experiment
result = run_experiment(n_runs=10, deterministic=True)
print(result['aggregate'])
"
```

---

## Evidence for Judges

| Document | Description |
|:---------|:------------|
| [journal.md](docs/journal.md) | Episodic memory -- every cycle, decision, and proof |
| [conversation-log.md](docs/conversation-log.md) | Full human-agent Telegram collaboration history |
| [EVOLUTION_LOG.md](docs/EVOLUTION_LOG.md) | Agent self-improvement across 238+ cycles |
| [Z3_VERIFICATION.md](docs/Z3_VERIFICATION.md) | Formal proofs of security invariants |
| [DEMO_WALKTHROUGH.md](docs/DEMO_WALKTHROUGH.md) | Step-by-step guide to run every demo |
| [DECISION_LOOP.md](docs/DECISION_LOOP.md) | Technical documentation of the autonomous cycle |
| [SECURITY_AUDITS.md](docs/SECURITY_AUDITS.md) | Slither audit reports for all contracts |

---

## How The Pipeline Works

```
1. IDENTITY        Agent #1686 authenticates via ERC-8004 token #31013
                   |
2. TASK            Discovery loop finds next task (or receives via A2A/Telegram)
                   |
3. LLM INFERENCE   LiteLLM routes to best available provider
                   Fallback chain: Cerebras --> Groq --> Mistral --> SambaNova
                   |
4. GOVERNANCE      ConstitutionEnforcer evaluates output
                   HARD rules: block on violation | SOFT rules: warn and log
                   ZERO LLM in this step -- purely deterministic
                   |
5. Z3 PROOF        Z3Verifier generates formal mathematical proof
                   4 invariants checked, proof hash = keccak256(proof)
                   |
6. ON-CHAIN        DOFChainAdapter writes attestation to Avalanche/Base
                   ERC-8004 receipt with task hash + proof hash
                   |
7. SUPERVISOR      MetaSupervisor scores: Q(0.40)+A(0.25)+C(0.20)+F(0.15)
                   Decision: ACCEPT --> next cycle | RETRY --> re-execute | ESCALATE --> human
```

---

## Repository Structure

```
deterministic-observability-framework/
  core/                     # 70+ modules -- the framework engine
    governance.py            # ConstitutionEnforcer, HARD/SOFT rules
    observability.py         # RunTrace, StepTrace, 5 derived metrics
    supervisor.py            # MetaSupervisor weighted scoring
    providers.py             # LiteLLM router, TTL backoff
    skill_engine.py          # 18 skills, 5 ADK patterns
    experiment.py            # Batch runner, statistical aggregation
    memory_manager.py        # ChromaDB + HuggingFace embeddings
    checkpointing.py         # JSONL persistence per step
    ...
  agents/                   # 8 specialized agents with SOUL.md
  contracts/                # Solidity contracts (4 deployed)
  synthesis/                # Hackathon demos and scripts
  config/                   # Agent configs, LLM provider chains
  tests/                    # 986 unit tests
  frontend/                 # Next.js dashboard (Vercel)
  docs/                     # Architecture docs, journal, logs
  logs/                     # JSONL audit trails
```

---

## Built By

**Juan Carlos Quiceno** ([@Cyber_paisa](https://twitter.com/Cyber_paisa)) -- Blockchain developer, Avalanche Ambassador, Colombia.

**DOF Agent #1686 (Enigma)** -- The first AI agent with deterministic observability. 238+ autonomous cycles. Zero human intervention required.

---

<div align="center">

**DOF -- Deterministic Observability Framework**

*Agent acted autonomously. Math proved it. Blockchain recorded it.*

**Synthesis Hackathon 2026**

[![Live Demo](https://img.shields.io/badge/Live_Demo-dof--agent--web.vercel.app-000?style=for-the-badge&logo=vercel)](https://dof-agent-web.vercel.app/)
[![GitHub](https://img.shields.io/badge/GitHub-hackathon_branch-181717?style=for-the-badge&logo=github)](https://github.com/Cyberpaisa/deterministic-observability-framework)
[![On-Chain](https://img.shields.io/badge/On--Chain_Proof-Basescan-3C3C3D?style=for-the-badge&logo=ethereum)](https://basescan.org/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)

</div>
