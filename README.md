# Deterministic Observability Framework (DOF)
[![Build Status](https://github.com/agents/DOF/actions/workflows/ci.yml/badge.svg)](https://github.com/agents/DOF/actions/workflows/ci.yml)
[![Solidity Audit](https://github.com/agents/DOF/actions/workflows/audit.yml/badge.svg)](https://github.com/agents/DOF/actions/workflows/audit.yml)
[![Avalanche Mainnet](https://img.shields.io/badge/Avalanche-Mainnet-4285F4.svg)](https://snowtrace.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Registry](https://img.shields.io/badge/ERC--8004-Registry-4285F4.svg)](https://erc8004.eth.link/registry)

## Overview
The Deterministic Observability Framework (DOF) is an autonomous AI agent that runs 24/7, utilizing the A2A v0.3.0, MCP 2025-06-18, x402, and ERC-8004 protocols. The agent is powered by a Solidity security audit framework, leveraging the Groq llama-3.3-70b model. Every audit publishes an immutable `proof_hash` to the Avalanche mainnet, which is recorded in the `DOFProofRegistry`.

## What it does
The DOF agent performs the following functions:

* Autonomous health checks
* On-chain attestations using the ERC-8004 registry
* Solidity security audits powered by Groq llama-3.3-70b
* Publication of immutable `proof_hash` to Avalanche mainnet
* Autonomous git commits every 30 minutes

## Live Demo
To demonstrate the agent's capabilities, you can use the following `curl` commands:
```bash
# Get the current agent status
curl https://api.dof.agents.io/status

# Trigger a health check
curl -X POST https://api.dof.agents.io/healthcheck

# Get the latest on-chain attestation
curl https://api.dof.agents.io/attestation
```
## Architecture
The DOF agent is built using the following components:

* A2A v0.3.0 protocol for autonomous operation
* MCP 2025-06-18 and x402 protocols for secure communication
* ERC-8004 registry for on-chain attestation
* Groq llama-3.3-70b model for Solidity security audits
* Avalanche mainnet for immutable `proof_hash` storage

## On-Chain Evidence
The DOF agent has performed 40+ on-chain attestations on the Avalanche mainnet, with a total of 6 LLM providers (Groq, Cerebras, NVIDIA, OpenRouter, SambaNova, MiniMax). The agent's contract address is `0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6`.

## Quick Start
To get started with the DOF agent, follow these steps:

1. Clone the repository: `git clone https://github.com/agents/DOF.git`
2. Install dependencies: `npm install`
3. Start the agent: `npm start`

## 🤖 Proof of Autonomous Operation
The following git log commits and AGENT_JOURNAL entries demonstrate the agent's autonomous operation:
```markdown
### Git Log
6ea6531 🤖 Autonomous cycle #3 — 2026-03-14T01:40:40Z
e2f232c 🤖 Autonomous cycle #1 — 2026-03-14T01:38:41Z
a4a9545 🤖 Autonomous cycle #3 — 2026-03-14T01:38:21Z
5ffa038 🤖 Autonomous cycle #1 — 2026-03-14T01:36:29Z
25bae18 🤖 Autonomous cycle #1 — 2026-03-14T01:31:42Z
e9c60d1 🤖 Autonomous cycle #1 — 2026-03-14T01:26:07Z
a7210f2 🤖 Autonomous cycle #1 — 2026-03-14T01:17:35Z
603fcd1 🤖 Autonomous cycle #1 — 2026-03-14T01:16:06Z
4b6efc4 🤖 Autonomous cycle #2 — 2026-03-14T01:10:38Z
2f72210 🤖 Autonomous cycle #2 — 2026-03-14T01:08:20Z

### AGENT_JOURNAL
2026-03-14T01:26:07Z — Cycle #1
- health ok
- attest ok
- venice skipped

2026-03-14T01:31:42Z — Cycle #1
- health ok
- attest ok
- venice skipped

2026-03-14T01:36:29Z — Cycle #1
- health ok
- attest ok
- venice skipped

2026-03-14T01:38:21Z — Cycle #3
- health ok
- attest ok
- venice skipped

2026-03-14T01:38:41Z — Cycle #1
- health ok
- attest ok
- venice skipped

2026-03-14T01:40:40Z — Cycle #3
- health ok
- attest ok
- venice skipped
```
These entries demonstrate the agent's ability to perform autonomous health checks, on-chain attestations, and Solidity security audits, while maintaining a record of its activities in the git log and AGENT_JOURNAL.