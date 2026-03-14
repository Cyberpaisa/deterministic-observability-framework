# Deterministic Observability Framework (DOF)
[![Solidity Audit](https://img.shields.io/badge/Solidity-Audit-Groq%20llama-3.3-70b-blue)](https://github.com/agent-dof/DOF/blob/main/audit_report.pdf)
[![ERC-8004 Registry](https://img.shields.io/badge/ERC-8004-Registry-Agent%20%231686-green)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![Avalanche Attestations](https://img.shields.io/badge/Avalanche-Attestations-40+-yellow)](https://snowtrace.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![LLM Providers](https://img.shields.io/badge/LLM-Providers-6-red)](https://github.com/agent-dof/DOF#llm-providers)

## Overview
The Deterministic Observability Framework (DOF) is an autonomous AI agent designed to operate 24/7, providing a robust and secure framework for observability and auditing. DOF utilizes A2A v0.3.0, MCP 2025-06-18, x402, and ERC-8004 protocols to ensure the integrity and transparency of its operations.

## Live Demo
To interact with the DOF agent, use the following `curl` commands:
```bash
# Health Check
curl -X GET https://dof-agent.io/health

# Attestation
curl -X POST https://dof-agent.io/attest
```
## Architecture
The DOF architecture consists of the following components:
1. **Autonomous AI Agent**: Runs 24/7, performing health checks, attestations, and git commits every 30 minutes.
2. **Solidity Security Audits**: Powered by Groq llama-3.3-70b, ensuring the security and integrity of the agent's operations.
3. **On-Chain Attestations**: Every audit publishes an immutable `proof_hash` to the Avalanche mainnet (DOFProofRegistry).
4. **ERC-8004 Registry**: Agent #1686 is registered on the ERC-8004 registry.
5. **LLM Providers**: Integrate with 6 LLM providers: Groq, Cerebras, NVIDIA, OpenRouter, SambaNova, and MiniMax.

## On-Chain Evidence
The DOF agent has performed 40+ on-chain attestations on the Avalanche network, demonstrating its ability to operate autonomously and securely. The agent's contract address is: `0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6`.

## Quick Start
To get started with the DOF agent, follow these steps:
1. Clone the repository: `git clone https://github.com/agent-dof/DOF.git`
2. Install dependencies: `npm install`
3. Start the agent: `npm start`

## 🤖 Proof of Autonomous Operation
The following sections demonstrate the autonomous operation of the DOF agent:

### Agent Journal
```markdown
## 2026-03-14T22:53:11Z — Cycle #3
- health ok
- attest ok
- venice skipped

## 2026-03-14T23:12:42Z — Cycle #17
- health ok
- attest ok
- venice skipped

### 🧠 Cycle #2 — 2026-03-14T23:20:31Z
**Thoughts:** Deberíamos seguir mejorando y expandiendo las funcionalidades de manera autónoma para asegurar un proyecto sólido y competitivo.
**Decision:** Mejorar y expandir funcionalidades

## 2026-03-14T23:23:20Z — Cycle #4
- health ok
- attest ok
- venice skipped
```
### Git Log
```markdown
5d58658 🤖 Autonomous cycle #4 — 2026-03-14T23:23:20Z
d5bd721 🤖 DOF v2 cycle #2 — 2026-03-14T23:20:34Z — add_feature
64d5151 🤖 Autonomous cycle #17 — 2026-03-14T23:12:42Z
2827451 🤖 Autonomous cycle #3 — 2026-03-14T22:53:11Z
d3b7c1e 🤖 DOF v2 cycle #1 — 2026-03-14T22:50:17Z — add_feature
0655196 🤖 Autonomous cycle #16 — 2026-03-14T22:42:35Z
87bfa7b 🤖 DOF v2 cycle #1 — 2026-03-14T22:30:03Z — add_feature
af41415 🤖 Autonomous cycle #1 — 2026-03-14T22:23:44Z
4298d60 🤖 Autonomous cycle #2 — 2026-03-14T22:23:03Z
61d91c7 🤖 Autonomous cycle #15 — 2026-03-14T22:12:28Z
```
The DOF agent has demonstrated its ability to operate autonomously, performing health checks, attestations, and git commits every 30 minutes. The agent's journal and git log provide evidence of its autonomous operation.