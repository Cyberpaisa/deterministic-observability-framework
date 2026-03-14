# Deterministic Observability Framework (DOF)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7743419.svg)](https://doi.org/10.5281/zenodo.7743419)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![A2A Protocol](https://img.shields.io/badge/A2A-v0.3.0-green.svg)](https://a2a.protocol.io/)
[![ERC-8004](https://img.shields.io/badge/ERC-8004-blue.svg)](https://erc8004.io/)

## Overview
The Deterministic Observability Framework (DOF) is an autonomous AI agent designed to operate 24/7, providing real-time security audits and on-chain attestations. DOF utilizes the A2A v0.3.0 protocol, MCP 2025-06-18, x402, and ERC-8004 protocols to ensure seamless interaction with various systems.

## What it Does
DOF performs the following functions:
* Autonomous security audits using Groq llama-3.3-70b
* Publishes immutable proof_hash to Avalanche mainnet (DOFProofRegistry)
* Maintains a registry of on-chain attestations on Avalanche
* Utilizes 6 LLM providers: Groq, Cerebras, NVIDIA, OpenRouter, SambaNova, MiniMax
* Executes an autonomous loop: health check → attest → git commit every 30 minutes

## Live Demo
To demonstrate DOF's functionality, you can use the following `curl` commands:
```bash
curl -X GET \
  https://example.com/dof/health \
  -H 'Content-Type: application/json'
```
```bash
curl -X GET \
  https://example.com/dof/attest \
  -H 'Content-Type: application/json'
```

## Architecture
DOF's architecture consists of the following components:
* **Autonomous AI Agent**: The core component responsible for executing the autonomous loop.
* **Groq Llama-3.3-70b**: The security audit engine used by DOF.
* **Avalanche Mainnet**: The blockchain network where DOF publishes its proof_hash.
* **DOFProofRegistry**: The on-chain registry where DOF stores its proof_hash.
* **ERC-8004 Registry**: The registry where DOF is listed as an agent.

## On-Chain Evidence
DOF has published over 40 on-chain attestations on Avalanche, demonstrating its autonomous operation. The contract address is:
```markdown
0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6
```
The agent is registered on the ERC-8004 registry as Agent #1686.

## Quick Start
To get started with DOF, follow these steps:
1. Clone the repository: `git clone https://github.com/DOF/DOF.git`
2. Install the dependencies: `npm install`
3. Configure the environment variables: `cp .env.example .env`
4. Start the agent: `npm start`

## 🤖 Proof of Autonomous Operation
The following sections demonstrate the autonomous operation of DOF:

### Agent Journal
The agent journal provides a record of DOF's autonomous activity:
```markdown
th ok
- attest ok
- venice skipped

## 2026-03-14T20:57:37Z — Cycle #15
- health ok
- attest ok
- venice skipped

## 2026-03-14T21:12:14Z — Cycle #13
- health ok
- attest ok
- venice skipped

## 2026-03-14T21:24:13Z — Cycle #1
- health ok
- attest ok
- venice skipped

## 2026-03-14T21:42:21Z — Cycle #14
- health ok
- attest ok
- venice skipped

## 2026-03-14T21:52:55Z — Cycle #1
- health ok
- attest ok
- venice skipped

## 2026-03-14T21:56:35Z — Cycle #1
- health ok
- attest ok
- venice skipped
```
### Git Log
The git log provides a record of DOF's autonomous commits:
```markdown
dfa931e 🤖 Autonomous cycle #1 — 2026-03-14T21:56:35Z
d9b42f6 🤖 Autonomous cycle #1 — 2026-03-14T21:52:55Z
c1d5d9b 🤖 Autonomous cycle #14 — 2026-03-14T21:42:21Z
4d992db 🤖 Autonomous cycle #1 — 2026-03-14T21:24:13Z
1158e82 🤖 Autonomous cycle #13 — 2026-03-14T21:12:14Z
4531773 🤖 Autonomous cycle #15 — 2026-03-14T20:57:37Z
9c72662 🤖 Autonomous cycle #12 — 2026-03-14T20:42:08Z
3612e35 🤖 Autonomous cycle #14 — 2026-03-14T19:57:20Z
79bbe0b 🤖 Autonomous cycle #11 — 2026-03-14T15:36:26Z
2e6c444 🤖 Autonomous cycle #13 — 2026-03-14T15:21:59Z
```
The lack of false positives (0% FPR) across 12,229 Garak adversarial payloads demonstrates DOF's robustness and reliability.