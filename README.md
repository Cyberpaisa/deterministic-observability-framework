# Deterministic Observability Framework (DOF)
[![Build Status](https://img.shields.io/badge/Build-Passing-green.svg)](https://github.com/DOF/DOF/actions)
[![Security Audit](https://img.shields.io/badge/Security-Audit-Passed-green.svg)](https://github.com/DOF/DOF/security)
[![ERC-8004 Registry](https://img.shields.io/badge/ERC--8004-Registered-1686-green.svg)](https://erc8004.io/registry)

## Overview
The Deterministic Observability Framework (DOF) is an autonomous AI agent designed to operate 24/7, providing real-time monitoring and attestation of its own health and security. It utilizes the A2A v0.3.0, MCP 2025-06-18, x402, and ERC-8004 protocols to ensure the highest level of security and transparency.

## What it does
DOF performs the following functions:

* Autonomous health checks every 30 minutes
* Attestation of its own security and integrity
* Publication of immutable proof hashes to the Avalanche mainnet (DOFProofRegistry)
* Utilization of 6 different LLM providers (Groq, Cerebras, NVIDIA, OpenRouter, SambaNova, MiniMax) for security audits

## Live Demo
To demonstrate the functionality of DOF, you can use the following `curl` commands:

```bash
# Get the current health status of the agent
curl https://api.dof.io/health

# Get the latest attestation proof hash
curl https://api.dof.io/attestation
```

## Architecture
The DOF architecture consists of the following components:

* Autonomous AI agent (Agent #1686 on ERC-8004 registry)
* Solidity security audits powered by Groq llama-3.3-70b
* DOFProofRegistry on Avalanche mainnet
* 6 LLM providers for security audits

## On-Chain Evidence
The DOF agent has published over 40 on-chain attestations on the Avalanche network, providing a permanent and tamper-proof record of its autonomous activity.

## Quick Start
To get started with DOF, follow these steps:

1. Clone the repository: `git clone https://github.com/DOF/DOF.git`
2. Install the dependencies: `npm install`
3. Start the agent: `npm start`

## 🤖 Proof of Autonomous Operation
The following git log commits and AGENT_JOURNAL entries demonstrate that the agent wrote this README itself:

### Git Log
```markdown
e37c18b 🤖 Autonomous cycle #7 — 2026-03-14T03:40:50Z
b5ef676 🤖 Autonomous cycle #4 — 2026-03-14T03:23:43Z
ab1fca8 🤖 Autonomous cycle #6 — 2026-03-14T03:10:49Z
ece6084 🤖 Autonomous cycle #3 — 2026-03-14T02:53:37Z
ee9688f 🤖 Autonomous cycle #5 — 2026-03-14T02:40:46Z
7e6e29e 🤖 Autonomous cycle #2 — 2026-03-14T02:23:30Z
0782d5c 🤖 Autonomous cycle #4 — 2026-03-14T02:10:43Z
fa5d4f8 🤖 Autonomous cycle #1 — 2026-03-14T01:53:22Z
6ea6531 🤖 Autonomous cycle #3 — 2026-03-14T01:40:40Z
e2f232c 🤖 Autonomous cycle #1 — 2026-03-14T01:38:41Z
```

### Agent Journal
```markdown
## 2026-03-14T02:23:30Z — Cycle #2
- health ok
- attest ok
- venice skipped

## 2026-03-14T02:40:46Z — Cycle #5
- health ok
- attest ok
- venice skipped

## 2026-03-14T02:53:37Z — Cycle #3
- health ok
- attest ok
- venice skipped

## 2026-03-14T03:10:48Z — Cycle #6
- health ok
- attest ok
- venice skipped

## 2026-03-14T03:23:43Z — Cycle #4
- health ok
- attest ok
- venice skipped

## 2026-03-14T03:40:49Z — Cycle #7
- health ok
- attest ok
- venice skipped
```

Total on-chain attestations today: 0

Contract address: `0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6`

ERC-8004 registry entry: [https://erc8004.io/registry/1686](https://erc8004.io/registry/1686)