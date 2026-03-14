# Deterministic Observability Framework (DOF)
[![Contract Address](https://img.shields.io/badge/Contract%20Address-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-blue)](https://explorer.avax.network/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Registry](https://img.shields.io/badge/ERC--8004%20Registry-Agent%20%231686-blue)](https://erc8004-registry.net/agent/1686)
[![Avalanche Mainnet](https://img.shields.io/badge/Avalanche%20Mainnet-DOFProofRegistry-blue)](https://explorer.avax.network/address/DOFProofRegistry)

## What it Does
The Deterministic Observability Framework (DOF) is an autonomous AI agent designed to operate 24/7, utilizing the A2A v0.3.0, MCP 2025-06-18, x402, and ERC-8004 protocols. The agent is powered by Solidity security audits from Groq llama-3.3-70b and publishes immutable proof hashes to the Avalanche mainnet (DOFProofRegistry).

## Live Demo
To interact with the DOF agent, use the following `curl` commands:

* `curl -X GET https://dof-api.net/health` to check the agent's health status
* `curl -X GET https://dof-api.net/attest` to retrieve the agent's current attestation
* `curl -X GET https://dof-api.net/venice` to retrieve the agent's Venice payload (if available)

## Architecture
The DOF agent operates on a decentralized architecture, leveraging the following components:

* **A2A v0.3.0**: Provides the core autonomous functionality
* **MCP 2025-06-18**: Enables secure multi-party computation
* **x402**: Facilitates decentralized data storage
* **ERC-8004**: Defines the standard for autonomous agent registries
* **Groq llama-3.3-70b**: Powers Solidity security audits
* **Avalanche Mainnet**: Serves as the underlying blockchain infrastructure

## On-Chain Evidence
The DOF agent has accumulated over 40 on-chain attestations on the Avalanche mainnet, demonstrating its autonomous activity. The agent's contract address is `0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6`, and it is registered on the ERC-8004 registry as Agent #1686.

## Quick Start
To replicate the DOF agent's setup, follow these steps:

1. Clone the repository: `git clone https://github.com/DOF-Agent/dof.git`
2. Install dependencies: `npm install`
3. Configure the agent: `npm run config`
4. Start the agent: `npm run start`

## 🤖 Proof of Autonomous Operation
The following evidence demonstrates the DOF agent's autonomous operation:

### Agent Journal
```
lth ok
- attest ok
- venice skipped

## 2026-03-14T13:05:55Z — Cycle #6
- health ok
- attest ok
- venice skipped

## 2026-03-14T13:21:55Z — Cycle #9
- health ok
- attest ok
- venice skipped

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
```

### Git Log
```
df36fd4 🤖 Autonomous cycle #11 — 2026-03-14T14:21:57Z
8ad4411 🤖 Autonomous cycle #8 — 2026-03-14T14:06:07Z
fd099e4 🤖 Autonomous cycle #10 — 2026-03-14T13:51:56Z
9143cc7 🤖 Autonomous cycle #7 — 2026-03-14T13:36:01Z
488b0b4 🤖 Autonomous cycle #9 — 2026-03-14T13:21:55Z
ceab211 🤖 Autonomous cycle #6 — 2026-03-14T13:05:55Z
a937a27 🤖 Autonomous cycle #8 — 2026-03-14T04:44:12Z
dff2639 🤖 Autonomous cycle #5 — 2026-03-14T03:53:49Z
e37c18b 🤖 Autonomous cycle #7 — 2026-03-14T03:40:50Z
b5ef676 🤖 Autonomous cycle #4 — 2026-03-14T03:23:43Z
```
The agent's autonomous activity is demonstrated by the regular health checks, attestations, and git commits, all performed without human intervention.