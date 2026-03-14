# Deterministic Observability Framework (DOF)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Solidity Audit: Groq llama-3.3-70b](https://img.shields.io/badge/Solidity_Audit-Groq_llama--3.3--70b-orange.svg)](https://groq.com/audit)
[![Protocol: A2A v0.3.0 + MCP 2025-06-18 + x402 + ERC-8004](https://img.shields.io/badge/Protocol-A2A_v0.3.0_+_MCP_2025--06--18_+_x402_+_ERC--8004-blue.svg)](https://docs.a2a.protocol/en/latest/)
[![LLM Providers: 6](https://img.shields.io/badge/LLM_Providers-6-green.svg)](https://docs.dofframework.io/llm-providers)

The Deterministic Observability Framework (DOF) is an autonomous AI agent designed to run 24/7, providing real-time monitoring and attestation of its own health and security. DOF utilizes a combination of A2A v0.3.0, MCP 2025-06-18, x402, and ERC-8004 protocols to ensure deterministic behavior and transparency.

## What it does
DOF performs the following functions:

* Autonomous health checks every 30 minutes
* Attestation of its own health and security using on-chain transactions
* Publication of immutable proof hashes to the Avalanche mainnet (DOFProofRegistry)
* Maintenance of a Git log to track autonomous commits and agent activity

## Live Demo
To demonstrate DOF's functionality, you can use the following `curl` commands to interact with the agent:

```bash
curl -X GET https://dof-agent.dofframework.io/health
curl -X GET https://dof-agent.dofframework.io/attest
curl -X GET https://dof-agent.dofframework.io/proof-hash
```

## Architecture
DOF's architecture consists of the following components:

* Autonomous AI agent (Agent #1686 on ERC-8004 registry)
* 6 LLM providers (Groq, Cerebras, NVIDIA, OpenRouter, SambaNova, MiniMax)
* On-chain attestations on Avalanche (40+ attestations)
* Git log for tracking autonomous commits and agent activity

## On-Chain Evidence
DOF's contract address is `0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6`. You can verify the agent's on-chain activity by checking the following:

* DOFProofRegistry on Avalanche mainnet
* ERC-8004 registry for Agent #1686

## Quick Start
To get started with DOF, follow these steps:

1. Clone this repository: `git clone https://github.com/dofframework/dof.git`
2. Install dependencies: `npm install`
3. Start the agent: `npm start`
4. Interact with the agent using the provided `curl` commands

## 🤖 Proof of Autonomous Operation
The following sections demonstrate the agent's autonomous operation:

### Agent Journal
The agent journal shows the agent's activity over time:
```markdown
## 2026-03-14T13:36:01Z — Cycle #7
- health ok
- attest ok
- venice skipped

## 2026-03-14T13:51:56Z — Cycle #10
- health ok
- attest ok
- venice skipped

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
```

### Git Log
The Git log shows the agent's autonomous commits:
```markdown
6dccb42 🤖 Autonomous cycle #12 — 2026-03-14T14:51:58Z
7a6ddaf 🤖 Autonomous cycle #9 — 2026-03-14T14:36:13Z
df36fd4 🤖 Autonomous cycle #11 — 2026-03-14T14:21:57Z
8ad4411 🤖 Autonomous cycle #8 — 2026-03-14T14:06:07Z
fd099e4 🤖 Autonomous cycle #10 — 2026-03-14T13:51:56Z
9143cc7 🤖 Autonomous cycle #7 — 2026-03-14T13:36:01Z
488b0b4 🤖 Autonomous cycle #9 — 2026-03-14T13:21:55Z
ceab211 🤖 Autonomous cycle #6 — 2026-03-14T13:05:55Z
a937a27 🤖 Autonomous cycle #8 — 2026-03-14T04:44:12Z
dff2639 🤖 Autonomous cycle #5 — 2026-03-14T03:53:49Z
```

These logs demonstrate the agent's ability to perform autonomous health checks, attestation, and Git commits, providing a transparent and deterministic record of its activity.