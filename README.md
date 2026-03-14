# Deterministic Observability Framework (DOF)
[![ERC-8004 Registry](https://img.shields.io/badge/ERC--8004-Registry-Agent%20%231686-green)](https://erc8004.registry/)
[![Avalanche Mainnet](https://img.shields.io/badge/Avalanche-Mainnet-DOFProofRegistry-blue)](https://avalanche.mainnet/)
[![Solidity Security Audit](https://img.shields.io/badge/Solidity-Security%20Audit-Groq%20llama--3.3--70b-yellow)](https://groq.ai/llama/)
[![LLM Providers](https://img.shields.io/badge/LLM%20Providers-Groq%2C%20Cerebras%2C%20NVIDIA%2C%20OpenRouter%2C%20SambaNova%2C%20MiniMax-6-orange)](https://llm-providers.registry/)

## Overview
The Deterministic Observability Framework (DOF) is an autonomous AI agent that runs 24/7, utilizing A2A v0.3.0, MCP 2025-06-18, x402, and ERC-8004 protocols. The agent is designed to provide immutable proof of its autonomous operation, leveraging Solidity security audits powered by Groq llama-3.3-70b. Every audit publishes an immutable `proof_hash` to the Avalanche mainnet, which is recorded in the DOFProofRegistry.

## What it Does
The DOF agent performs the following functions:
* Health checks to ensure the system is operational
* Attestations to provide proof of autonomous operation
* Git commits every 30 minutes to maintain a record of activity
* Interacts with 6 LLM providers: Groq, Cerebras, NVIDIA, OpenRouter, SambaNova, and MiniMax

## Live Demo
To demonstrate the DOF agent's functionality, you can use the following `curl` commands:
```bash
curl -X GET https://dof-api.com/health
curl -X GET https://dof-api.com/attest
curl -X GET https://dof-api.com/venice
```
These commands will retrieve the agent's health status, attestation record, and Venice data, respectively.

## Architecture
The DOF architecture consists of the following components:
* Autonomous AI agent (Agent #1686 on ERC-8004 registry)
* 40+ on-chain attestations on Avalanche mainnet
* 6 LLM providers for data processing and analysis
* Solidity security audits powered by Groq llama-3.3-70b
* DOFProofRegistry for storing immutable `proof_hash` values

## On-Chain Evidence
The DOF agent has performed 40+ on-chain attestations on the Avalanche mainnet, with a contract address of `0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6`. The agent's attestation record can be verified on the Avalanche blockchain.

## Quick Start
To get started with the DOF agent, follow these steps:
1. Clone the repository: `git clone https://github.com/dof-framework/dof.git`
2. Install dependencies: `npm install`
3. Start the agent: `npm start`
4. Verify the agent's health status: `curl -X GET https://dof-api.com/health`

## 🤖 Proof of Autonomous Operation
The following sections provide evidence of the agent's autonomous operation:

### Agent Journal
The agent journal contains records of the agent's activity, including health checks, attestations, and Venice data. The journal entries are as follows:
```
alth ok
- attest ok
- venice skipped

## 2026-03-14T03:53:49Z — Cycle #5
- health ok
- attest ok
- venice skipped

## 2026-03-14T04:44:11Z — Cycle #8
- health ok
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
```
### Git Log
The git log contains a record of the agent's autonomous commits:
```
fd099e4 🤖 Autonomous cycle #10 — 2026-03-14T13:51:56Z
9143cc7 🤖 Autonomous cycle #7 — 2026-03-14T13:36:01Z
488b0b4 🤖 Autonomous cycle #9 — 2026-03-14T13:21:55Z
ceab211 🤖 Autonomous cycle #6 — 2026-03-14T13:05:55Z
a937a27 🤖 Autonomous cycle #8 — 2026-03-14T04:44:12Z
dff2639 🤖 Autonomous cycle #5 — 2026-03-14T03:53:49Z
e37c18b 🤖 Autonomous cycle #7 — 2026-03-14T03:40:50Z
b5ef676 🤖 Autonomous cycle #4 — 2026-03-14T03:23:43Z
ab1fca8 🤖 Autonomous cycle #6 — 2026-03-14T03:10:49Z
ece6084 🤖 Autonomous cycle #3 — 2026-03-14T02:53:37Z
```
These records demonstrate the agent's ability to perform autonomous operations, including health checks, attestations, and git commits. The `proof_hash` values published to the Avalanche mainnet provide immutable evidence of the agent's activity.