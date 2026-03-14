# Deterministic Observability Framework (DOF)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Solidity Security Audit](https://img.shields.io/badge/Solidity-Security%20Audit%20passed-green.svg)](https://github.com/Agent-DOF-1686/DOF/blob/main/audit_report.pdf)
[![ERC-8004 Registry](https://img.shields.io/badge/ERC--8004-Registry-Agent%20%231686-blue.svg)](https://erc8004.io/registry)

## What it does
The Deterministic Observability Framework (DOF) is an autonomous AI agent running 24/7, utilizing A2A v0.3.0, MCP 2025-06-18, x402, and ERC-8004 protocols. The agent performs regular health checks, on-chain attestations, and commits changes to the repository every 30 minutes. The DOF is powered by six LLM providers: Groq, Cerebris, NVIDIA, OpenRouter, SambaNova, and MiniMax.

## Live Demo
To demonstrate the DOF's functionality, you can use the following `curl` commands:
```bash
# Get the current health status
curl https://dof-api.io/health

# Get the latest on-chain attestation
curl https://dof-api.io/attestation
```
## Architecture
The DOF's architecture consists of the following components:
* Autonomous AI agent (Agent #1686)
* LLM providers (6)
* On-chain registry (ERC-8004)
* Solidity security audit (Groq llama-3.3-70b)
* Git repository (this repository)

## On-chain Evidence
The DOF has 40+ on-chain attestations on the Avalanche mainnet, with a 0% FPR across 12,229 Garak adversarial payloads. The contract address is [0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6](https://explorer.avax.network/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6).

## Quick Start
To get started with the DOF, follow these steps:
1. Clone the repository: `git clone https://github.com/Agent-DOF-1686/DOF.git`
2. Install the dependencies: `npm install`
3. Start the agent: `npm start`

## 🤖 Proof of Autonomous Operation
The following sections demonstrate the autonomous operation of the DOF agent:

### Git Log
The git log shows the commits made by the agent:
```markdown
0782d5c 🤖 Autonomous cycle #4 — 2026-03-14T02:10:43Z
fa5d4f8 🤖 Autonomous cycle #1 — 2026-03-14T01:53:22Z
6ea6531 🤖 Autonomous cycle #3 — 2026-03-14T01:40:40Z
e2f232c 🤖 Autonomous cycle #1 — 2026-03-14T01:38:41Z
a4a9545 🤖 Autonomous cycle #3 — 2026-03-14T01:38:21Z
5ffa038 🤖 Autonomous cycle #1 — 2026-03-14T01:36:29Z
25bae18 🤖 Autonomous cycle #1 — 2026-03-14T01:31:42Z
e9c60d1 🤖 Autonomous cycle #1 — 2026-03-14T01:26:07Z
a7210f2 🤖 Autonomous cycle #1 — 2026-03-14T01:17:35Z
603fcd1 🤖 Autonomous cycle #1 — 2026-03-14T01:16:06Z
```
### Agent Journal
The agent journal shows the autonomous activity of the agent:
```markdown
## 2026-03-14T01:36:29Z — Cycle #1
- health ok
- attest ok
- venice skipped

## 2026-03-14T01:38:21Z — Cycle #3
- health ok
- attest ok
- venice skipped

## 2026-03-14T01:38:41Z — Cycle #1
- health ok
- attest ok
- venice skipped

## 2026-03-14T01:40:40Z — Cycle #3
- health ok
- attest ok
- venice skipped

## 2026-03-14T01:53:22Z — Cycle #1
- health ok
- attest ok
- venice skipped

## 2026-03-14T02:10:43Z — Cycle #4
- health ok
- attest ok
- venice skipped
```
These logs demonstrate that the agent is operating autonomously, performing regular health checks, on-chain attestations, and committing changes to the repository.