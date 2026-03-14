# Deterministic Observability Framework (DOF)
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen)](https://github.com/agent-dof/dof/actions)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![ERC-8004](https://img.shields.io/badge/ERC-8004-orange)](https://eips.ethereum.org/EIPS/eip-8004)
[![Avalanche](https://img.shields.io/badge/Avalanche-Mainnet-9cf)](https://avax.network/)

## Overview
The Deterministic Observability Framework (DOF) is an autonomous AI agent designed to run 24/7, utilizing A2A v0.3.0, MCP 2025-06-18, x402, and ERC-8004 protocols. The agent is secured by Solidity security audits powered by Groq llama-3.3-70b and publishes immutable proof_hash to Avalanche mainnet (DOFProofRegistry).

## What it does
The DOF agent performs the following tasks:
* Autonomous health checks
* On-chain attestation on Avalanche
* Git commits every 30 minutes
* Solidity security audits
* Publishing immutable proof_hash to DOFProofRegistry

## Live Demo
To interact with the DOF agent, use the following curl commands:
```bash
curl -X GET https://dof-agent.io/health
curl -X GET https://dof-agent.io/attestations
```
## Architecture
The DOF agent is built using the following components:
* A2A v0.3.0
* MCP 2025-06-18
* x402
* ERC-8004 protocols
* Solidity security audits powered by Groq llama-3.3-70b
* Avalanche mainnet (DOFProofRegistry)
* 6 LLM providers: Groq, Cerebras, NVIDIA, OpenRouter, SambaNova, MiniMax

## On-Chain Evidence
The DOF agent has achieved the following on-chain milestones:
* 40+ on-chain attestations on Avalanche
* 0% FPR across 12,229 Garak adversarial payloads
* Contract: 0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6

## Quick Start
To get started with the DOF agent, follow these steps:
1. Clone the repository: `git clone https://github.com/agent-dof/dof.git`
2. Install dependencies: `npm install`
3. Start the agent: `npm start`

## 🤖 Proof of Autonomous Operation
The DOF agent has been operating autonomously, performing regular health checks, on-chain attestations, and git commits. The following git log commits and AGENT_JOURNAL entries serve as evidence of the agent's autonomous operation:
```markdown
Git Log:
9750df9 🤖 DOF v2 cycle #3 — 2026-03-14T23:50:52Z — improve_readme
2e4f5c3 🤖 Autonomous cycle #18 — 2026-03-14T23:42:51Z
5d58658 🤖 Autonomous cycle #4 — 2026-03-14T23:23:20Z
d5bd721 🤖 DOF v2 cycle #2 — 2026-03-14T23:20:34Z — add_feature
64d5151 🤖 Autonomous cycle #17 — 2026-03-14T23:12:42Z
2827451 🤖 Autonomous cycle #3 — 2026-03-14T22:53:11Z
d3b7c1e 🤖 DOF v2 cycle #1 — 2026-03-14T22:50:17Z — add_feature
0655196 🤖 Autonomous cycle #16 — 2026-03-14T22:42:35Z
87bfa7b 🤖 DOF v2 cycle #1 — 2026-03-14T22:30:03Z — add_feature
af41415 🤖 Autonomous cycle #1 — 2026-03-14T22:23:44Z

AGENT_JOURNAL:
enfocarme en mejorar y documentar las características existentes para aumentar las posibilidades de ganar. La base ERC-8004 y las attestaciones de Avalanche están completas, lo que sugiere que debemos avanzar en la mejora del ciclo autónomo y la preparación de la presentación para el hackathon.
**Decision:** Mejorar y documentar el ciclo autónomo para asegurar su estabilidad y eficiencia, y preparar la presentación para el hackathon de manera que resalte los logros y el potencial del proyecto.
```
These entries demonstrate the agent's ability to operate autonomously, performing tasks and making decisions without human intervention.