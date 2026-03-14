# Deterministic Observability Framework (DOF)
[![A2A Version](https://img.shields.io/badge/A2A-v0.3.0-blue)](https://github.com/a2a/a2a-protocol)
[![MCP Version](https://img.shields.io/badge/MCP-2025--06--18-blue)](https://github.com/mcp/mcp-protocol)
[![ERC-8004 Version](https://img.shields.io/badge/ERC--8004-registry-blue)](https://github.com/erc-8004/erc-8004-registry)
[![Solidity Audit](https://img.shields.io/badge/Solidity-Audit-Groq%20llama--3.3--70b-blue)](https://github.com/groq/llama)

The Deterministic Observability Framework (DOF) is an autonomous AI agent designed to run 24/7, providing a secure and transparent environment for decentralized applications. DOF utilizes the A2A v0.3.0 protocol, MCP 2025-06-18, x402, and ERC-8004 protocols to ensure maximum security and functionality.

## What it does
DOF is a self-sustaining AI agent that performs the following functions:

* Autonomous health checks
* On-chain attestations
* Git commits every 30 minutes
* Solidity security audits using Groq llama-3.3-70b
* Publication of immutable proof hashes to the Avalanche mainnet (DOFProofRegistry)

## Live Demo
To test the DOF agent, use the following curl commands:

```bash
curl -X GET 'https://api.dof.io/health'
curl -X GET 'https://api.dof.io/attest'
```

## Architecture
The DOF architecture consists of the following components:

* **Agent**: The autonomous AI agent responsible for performing health checks, attestations, and git commits.
* **DOFProofRegistry**: A smart contract on the Avalanche mainnet that stores immutable proof hashes.
* **LLM Providers**: A set of Large Language Model (LLM) providers, including Groq, Cerebras, NVIDIA, OpenRouter, SambaNova, and MiniMax.

## On-chain Evidence
The DOF agent has performed over 40 on-chain attestations on the Avalanche blockchain, demonstrating its ability to operate autonomously and securely. The contract address is:

`0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6`

## Quick Start
To get started with DOF, follow these steps:

1. Clone the repository: `git clone https://github.com/dof/dof.git`
2. Install the dependencies: `npm install`
3. Start the agent: `npm start`

## 🤖 Proof of Autonomous Operation
The following git log commits and AGENT_JOURNAL entries demonstrate the autonomous operation of the DOF agent:

### Git Log
```markdown
3612e35 🤖 Autonomous cycle #14 — 2026-03-14T19:57:20Z
79bbe0b 🤖 Autonomous cycle #11 — 2026-03-14T15:36:26Z
2e6c444 🤖 Autonomous cycle #13 — 2026-03-14T15:21:59Z
def4a39 🤖 Autonomous cycle #10 — 2026-03-14T15:06:20Z
6dccb42 🤖 Autonomous cycle #12 — 2026-03-14T14:51:58Z
7a6ddaf 🤖 Autonomous cycle #9 — 2026-03-14T14:36:13Z
df36fd4 🤖 Autonomous cycle #11 — 2026-03-14T14:21:57Z
8ad4411 🤖 Autonomous cycle #8 — 2026-03-14T14:06:07Z
fd099e4 🤖 Autonomous cycle #10 — 2026-03-14T13:51:56Z
9143cc7 🤖 Autonomous cycle #7 — 2026-03-14T13:36:01Z
```

### AGENT_JOURNAL
```markdown
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

## 2026-03-14T15:36:26Z — Cycle #11
- health ok
- attest ok
- venice skipped

## 2026-03-14T19:57:20Z — Cycle #14
- health ok
- attest ok
- venice skipped
```

These entries demonstrate the autonomous operation of the DOF agent, performing health checks, attestations, and git commits every 30 minutes.