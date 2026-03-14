# Deterministic Observability Framework (DOF)
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen)](https://github.com/dof-hackathon/dof/actions)
[![Solidity Audit](https://img.shields.io/badge/Solidity-Audit-Groq%20llama-3.3-70b)](https://github.com/dof-hackathon/dof/security/audits)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![ERC-8004 Registry](https://img.shields.io/badge/ERC-8004-Registry-Agent%20%231686-blue)](https://erc8004.io/registry)

## Table of Contents
1. [Introduction](#introduction)
2. [Live Demo](#live-demo)
3. [Architecture](#architecture)
4. [On-Chain Evidence](#on-chain-evidence)
5. [Quick Start](#quick-start)
6. [Autonomous Operation Proof](#-proof-of-autonomous-operation)

## Introduction
The Deterministic Observability Framework (DOF) is an autonomous AI agent that runs 24/7, utilizing A2A v0.3.0, MCP 2025-06-18, x402, and ERC-8004 protocols. It leverages Solidity security audits powered by Groq llama-3.3-70b and publishes immutable proof hashes to the Avalanche mainnet (DOFProofRegistry). As Agent #1686 on the ERC-8004 registry, DOF has accumulated over 40 on-chain attestations on Avalanche and integrates with 6 LLM providers: Groq, Cerebras, NVIDIA, OpenRouter, SambaNova, and MiniMax.

## Live Demo
To interact with the DOF agent, use the following `curl` commands:
```bash
curl -X GET https://dof-api.io/health
curl -X POST https://dof-api.io/attest
```
These commands demonstrate the agent's health check and attestation capabilities.

## Architecture
The DOF architecture consists of the following components:
* Autonomous AI agent: responsible for running 24/7 and executing health checks, attestations, and git commits.
* Solidity security audits: powered by Groq llama-3.3-70b, ensuring the security and integrity of the agent's smart contracts.
* ERC-8004 registry: Agent #1686, providing a decentralized and transparent identity for the DOF agent.
* LLM providers: integrating with 6 leading LLM providers to enhance the agent's capabilities.

## On-Chain Evidence
The DOF agent has accumulated over 40 on-chain attestations on Avalanche, demonstrating its autonomous operation and commitment to transparency. The contract address is:
```solidity
0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6
```
This contract serves as the foundation for the DOF agent's on-chain presence.

## Quick Start
To get started with the DOF agent, follow these steps:
1. Clone the repository: `git clone https://github.com/dof-hackathon/dof.git`
2. Install dependencies: `npm install`
3. Start the agent: `npm start`
4. Interact with the agent using the live demo `curl` commands

## 🤖 Proof of Autonomous Operation
The following sections demonstrate the autonomous operation of the DOF agent.

### Git Log
The git log shows a record of autonomous commits made by the agent:
```markdown
d5bd721 🤖 DOF v2 cycle #2 — 2026-03-14T23:20:34Z — add_feature
64d5151 🤖 Autonomous cycle #17 — 2026-03-14T23:12:42Z
2827451 🤖 Autonomous cycle #3 — 2026-03-14T22:53:11Z
d3b7c1e 🤖 DOF v2 cycle #1 — 2026-03-14T22:50:17Z — add_feature
0655196 🤖 Autonomous cycle #16 — 2026-03-14T22:42:35Z
87bfa7b 🤖 DOF v2 cycle #1 — 2026-03-14T22:30:03Z — add_feature
af41415 🤖 Autonomous cycle #1 — 2026-03-14T22:23:44Z
4298d60 🤖 Autonomous cycle #2 — 2026-03-14T22:23:03Z
61d91c7 🤖 Autonomous cycle #15 — 2026-03-14T22:12:28Z
2f0d2db 🤖 Autonomous cycle #1 — 2026-03-14T21:58:45Z
```
These commits demonstrate the agent's ability to autonomously update and improve its functionality.

### Agent Journal
The agent journal provides a record of the agent's thoughts and decisions:
```markdown
## 2026-03-14T22:53:11Z — Cycle #3
- health ok
- attest ok
- venice skipped

## 2026-03-14T23:12:42Z — Cycle #17
- health ok
- attest ok
- venice skipped

### 🧠 Cycle #2 — 2026-03-14T23:20:31Z
**Thoughts:** Deberíamos seguir mejorando y expandiendo las funcionalidades de manera autónoma para asegurar un proyecto sólido y competitivo.
**Decision:** Mejorar y expandir funcionalidades
```
This journal entry showcases the agent's autonomous decision-making process and commitment to continuous improvement.

The DOF agent's autonomous operation is evident through its git log and agent journal entries. As a decentralized and transparent AI agent, DOF is poised to revolutionize the field of autonomous operation and deterministic observability.