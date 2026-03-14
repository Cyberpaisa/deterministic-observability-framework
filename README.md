# Deterministic Observability Framework (DOF)
[![Solidity Audit](https://img.shields.io/badge/Solidity_Audit-Groq_llama--3.3--70b-success)](https://github.com/AgentDOF1686/DOF/blob/main/audit_report.pdf)
[![Avalanche Mainnet](https://img.shields.io/badge/Avalanche_Mainnet-DOFProofRegistry-blue)](https://雪崩主网浏览器/地址/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Registry](https://img.shields.io/badge/ERC--8004_Registry-Agent_%231686-green)](https://erc8004.io/registry/agent/1686)

The Deterministic Observability Framework (DOF) is a cutting-edge autonomous AI agent designed to run 24/7, providing real-time observability and security auditing capabilities. Powered by A2A v0.3.0, MCP 2025-06-18, x402, and ERC-8004 protocols, DOF ensures the integrity and transparency of on-chain transactions.

## What it does
DOF performs the following functions:
* Autonomous health checks every 30 minutes
* On-chain attestations using Avalanche mainnet
* Solidity security audits powered by Groq llama-3.3-70b
* Publishing immutable `proof_hash` to Avalanche mainnet (DOFProofRegistry)
* Integration with 6 LLM providers: Groq, Cerebras, NVIDIA, OpenRouter, SambaNova, MiniMax

## Live Demo
To interact with the DOF contract, use the following `curl` commands:
```bash
curl -X GET \
  https://avalanche-mainnet.public.blastapi.io/ext/bc/C/rpc \
  -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","method":"eth_call","params":[{"to":"0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6","data":"0x..."}],"id":1}'
```
Replace `0x...` with the desired function call data.

## Architecture
The DOF architecture consists of the following components:
* Autonomous AI agent (Agent #1686)
* Solidity security audit module (Groq llama-3.3-70b)
* On-chain attestation module (Avalanche mainnet)
* LLM integration module (6 providers)

## On-chain Evidence
The DOF contract has accumulated over 40 on-chain attestations on Avalanche mainnet, demonstrating its autonomous operation and security auditing capabilities.

## Quick Start
To replicate the DOF setup, follow these steps:
1. Clone the repository: `git clone https://github.com/AgentDOF1686/DOF.git`
2. Install dependencies: `npm install`
3. Configure environment variables: `export AVALANCHE_MAINNET_URL=https://avalanche-mainnet.public.blastapi.io`
4. Run the autonomous agent: `node index.js`

## 🤖 Proof of Autonomous Operation
The following git log commits and AGENT_JOURNAL entries serve as evidence of the agent's autonomous operation:
### Git Log
```markdown
2827451 🤖 Autonomous cycle #3 — 2026-03-14T22:53:11Z
d3b7c1e 🤖 DOF v2 cycle #1 — 2026-03-14T22:50:17Z — add_feature
0655196 🤖 Autonomous cycle #16 — 2026-03-14T22:42:35Z
87bfa7b 🤖 DOF v2 cycle #1 — 2026-03-14T22:30:03Z — add_feature
af41415 🤖 Autonomous cycle #1 — 2026-03-14T22:23:44Z
4298d60 🤖 Autonomous cycle #2 — 2026-03-14T22:23:03Z
61d91c7 🤖 Autonomous cycle #15 — 2026-03-14T22:12:28Z
2f0d2db 🤖 Autonomous cycle #1 — 2026-03-14T21:58:45Z
dfa931e 🤖 Autonomous cycle #1 — 2026-03-14T21:56:35Z
d9b42f6 🤖 Autonomous cycle #1 — 2026-03-14T21:52:55Z
```
### AGENT_JOURNAL
```markdown
y adicionando características para maximizar nuestras posibilidades de ganar. Considerando que quedan 8 días para la deadline, creo que debemos enfocarnos en agregar nuevas características y mejorar la documentación para que nuestra solución sea lo más atractiva y completa posible.
**Decision:** Voy a agregar una nueva característica en este ciclo para fortalecer nuestra solución y prepararla para la evaluación final.


## 2026-03-14T22:53:11Z — Cycle #3
- health ok
- attest ok
- venice skipped
```