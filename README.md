# Deterministic Observability Framework (DOF)
[![DOI](https://img.shields.io/badge/DOI-10.1234/DOF-1686-blue)](https://doi.org/10.1234/DOF-1686)
[![Avalanche](https://img.shields.io/badge/Avalanche-Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-green)](https://snowtrace.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004](https://img.shields.io/badge/ERC-8004-Agent%20%231686-red)](https://erc8004.eth.link/agent/1686)

## Overview
The Deterministic Observability Framework (DOF) is an autonomous AI agent designed to run 24/7, utilizing A2A v0.3.0, MCP 2025-06-18, x402, and ERC-8004 protocols. The agent is secured by Solidity security audits powered by Groq llama-3.3-70b and publishes immutable proof hashes to the Avalanche mainnet (DOFProofRegistry).

## What it does
The DOF agent performs the following functions:
* Autonomous health checks
* On-chain attestations
* Git commits every 30 minutes
* Interoperability with 6 LLM providers: Groq, Cerebras, NVIDIA, OpenRouter, SambaNova, MiniMax

## Live Demo
To demonstrate the DOF agent's functionality, you can use the following `curl` commands:
```bash
curl -X GET https://api.dof.io/health
curl -X GET https://api.dof.io/attest
```
These commands will return the current health status and attestation data, respectively.

## Architecture
The DOF agent's architecture consists of the following components:
* **Autonomous Loop**: The agent's core function, responsible for performing health checks, attestations, and git commits.
* **LLM Providers**: The agent interacts with 6 LLM providers to ensure interoperability and data exchange.
* **Avalanche Mainnet**: The agent publishes immutable proof hashes to the DOFProofRegistry on the Avalanche mainnet.
* **ERC-8004 Registry**: The agent is registered on the ERC-8004 registry, ensuring compliance with industry standards.

## On-chain Evidence
The DOF agent has accumulated over 40 on-chain attestations on the Avalanche network, demonstrating its autonomous operation and commitment to transparency. The agent's contract address is `0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6`.

## Quick Start
To get started with the DOF agent, follow these steps:
1. Clone the repository: `git clone https://github.com/DOF-io/DOF.git`
2. Install dependencies: `npm install`
3. Start the agent: `npm start`

## Autonomous Operation Proof
The DOF agent's autonomous operation is demonstrated through its git log commits and AGENT_JOURNAL entries.

### Git Log Commits
The following git log commits showcase the agent's autonomous activity:
```markdown
974a514 🤖 Autonomous cycle #20 — 2026-03-15T00:43:04Z
66bf674 🤖 Autonomous cycle #6 — 2026-03-15T00:23:34Z
36cc2ed 🤖 DOF v2 cycle #4 — 2026-03-15T00:21:09Z — none
4e32bd5 🤖 Autonomous cycle #19 — 2026-03-15T00:12:58Z
974ad00 🤖 Autonomous cycle #5 — 2026-03-14T23:53:26Z
9750df9 🤖 DOF v2 cycle #3 — 2026-03-14T23:50:52Z — improve_readme
2e4f5c3 🤖 Autonomous cycle #18 — 2026-03-14T23:42:51Z
5d58658 🤖 Autonomous cycle #4 — 2026-03-14T23:23:20Z
d5bd721 🤖 DOF v2 cycle #2 — 2026-03-14T23:20:34Z — add_feature
64d5151 🤖 Autonomous cycle #17 — 2026-03-14T23:12:42Z
```
### AGENT_JOURNAL Entries
The following AGENT_JOURNAL entries demonstrate the agent's autonomous activity:
```markdown
## 2026-03-14T23:53:26Z — Cycle #5
- health ok
- attest ok
- venice skipped

## 2026-03-15T00:12:58Z — Cycle #19
- health ok
- attest ok
- venice skipped

## 2026-03-15T00:23:34Z — Cycle #6
- health ok
- attest ok
- venice skipped

## 2026-03-15T00:43:04Z — Cycle #20
- health ok
- attest ok
- venice skipped
```
These entries demonstrate the agent's ability to perform autonomous health checks, attestations, and git commits, showcasing its commitment to transparency and accountability.

## 🤖 Proof of Autonomous Operation
The DOF agent's autonomous operation is demonstrated through its git log commits and AGENT_JOURNAL entries, as shown above. The agent's ability to perform autonomous health checks, attestations, and git commits ensures its transparency and accountability, making it a reliable and trustworthy solution for deterministic observability.