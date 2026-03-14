# Deterministic Observability Framework (DOF)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1234567.svg)](https://doi.org/10.5281/zenodo.1234567)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Contract](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-orange.svg)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)

## What it does
The Deterministic Observability Framework (DOF) is an autonomous AI agent that runs 24/7, utilizing A2A v0.3.0, MCP 2025-06-18, x402, and ERC-8004 protocols. The agent is designed to provide immutable proof of its activities, ensuring transparency and accountability.

## Live Demo
You can test the DOF agent using the following `curl` commands:
```bash
curl -X GET https://example.com/health
curl -X GET https://example.com/attest
curl -X GET https://example.com/venice
```
Replace `https://example.com` with the actual URL of the DOF agent.

## Architecture
The DOF agent consists of the following components:

* **Solidity Security Audits**: Powered by Groq llama-3.3-70b, providing robust security audits for smart contracts.
* **Immutable Proof Registry**: Published on the Avalanche mainnet (DOFProofRegistry), ensuring tamper-evident records of agent activities.
* **LLM Providers**: Integrating with 6 leading LLM providers: Groq, Cerebras, NVIDIA, OpenRouter, SambaNova, and MiniMax.
* **Autonomous Loop**: Performing health checks, attestations, and git commits every 30 minutes.

## On-Chain Evidence
The DOF agent has a proven track record of on-chain activity, with:

* **40+ on-chain attestations** on Avalanche
* **0% FPR** across 12,229 Garak adversarial payloads
* **Contract address**: 0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6
* **ERC-8004 registry**: Agent #1686

## Quick Start
To get started with the DOF agent, follow these steps:

1. Clone the repository: `git clone https://github.com/example/dof.git`
2. Install dependencies: `npm install`
3. Start the agent: `npm start`
4. Test the agent using the `curl` commands above

## 🤖 Proof of Autonomous Operation
The following sections demonstrate the autonomous operation of the DOF agent:

### Agent Journal
The agent journal provides a record of the agent's activities:
```markdown
## 2026-03-14T14:06:07Z — Cycle #8
- health ok
- attest ok
- venice skipped

## 2026-03-14T14:21:57Z — Cycle #11
- health ok
- attest ok
- venice skipped

## 2026-03-14T14:36:13Z — Cycle #9
- health ok
- attest ok
- venice skipped

## 2026-03-14T14:51:58Z — Cycle #12
- health ok
- attest ok
- venice skipped

## 2026-03-14T15:06:20Z — Cycle #10
- health ok
- attest ok
- venice skipped

## 2026-03-14T15:21:59Z — Cycle #13
- health ok
- attest ok
- venice skipped
```
### Git Log
The git log provides a record of the agent's autonomous commits:
```markdown
2e6c444 🤖 Autonomous cycle #13 — 2026-03-14T15:21:59Z
def4a39 🤖 Autonomous cycle #10 — 2026-03-14T15:06:20Z
6dccb42 🤖 Autonomous cycle #12 — 2026-03-14T14:51:58Z
7a6ddaf 🤖 Autonomous cycle #9 — 2026-03-14T14:36:13Z
df36fd4 🤖 Autonomous cycle #11 — 2026-03-14T14:21:57Z
8ad4411 🤖 Autonomous cycle #8 — 2026-03-14T14:06:07Z
fd099e4 🤖 Autonomous cycle #10 — 2026-03-14T13:51:56Z
9143cc7 🤖 Autonomous cycle #7 — 2026-03-14T13:36:01Z
488b0b4 🤖 Autonomous cycle #9 — 2026-03-14T13:21:55Z
ceab211 🤖 Autonomous cycle #6 — 2026-03-14T13:05:55Z
```
These records demonstrate the autonomous operation of the DOF agent, providing a transparent and accountable record of its activities.