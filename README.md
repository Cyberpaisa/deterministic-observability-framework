# DOF Synthesis 2026 Hackathon
================================

[![Server Status](https://img.shields.io/website?down_color=red&down_message=Offline&up_color=green&up_message=Online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract Address](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-blue)](https://snowtrace.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6#balances)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004-Agent-%231686-blue)]()

## Overview
--------

DOF Synthesis is a cutting-edge project that leverages the power of A2A, MCP, x402, and OASF protocols to create a decentralized, autonomous system. Our project features a unique architecture that enables seamless interaction between humans and agents, ensuring a secure and efficient experience.

## Architecture
------------

The following diagram illustrates the high-level architecture of our system:
```mermaid
graph LR
    A[Human] -->|Interact|> B[Agent]
    B -->|A2A/MCP/x402/OASF|> C[Blockchain]
    C -->|Smart Contract|> D[Autonomous Cycle]
    D -->|AI Decision|> E[Action]
    E -->|Feedback|> A
```
## Live Curls
-------------

You can test our API using the following live curls:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/agents
curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/contracts
```
## Proof of Autonomy
-------------------

Our system has successfully completed 2 autonomous cycles, with 1+ attestations on-chain. The following table summarizes our progress:

| Metric | Value |
| --- | --- |
| Autonomous Cycles | 2 |
| On-Chain Attestations | 1+ |
| Auto-Generated Features | 0 |
| Days until Deadline | 7 |

## Human-Agent Collaboration
---------------------------

Our project emphasizes the importance of human-agent collaboration. You can view our live conversation log [here](docs/conversation-log.md).

## Task Tracking and Milestones
-----------------------------

We use [GitHub Issues](https://github.com/your-username/your-repo/issues) for task tracking and [Releases](https://github.com/your-username/your-repo/releases) for milestones.

## Recent Updates
----------------

Our recent updates include:

* `4a50f43`: feat: bond.credit creditworthy trading agent for Agents that Pay bounty
* `212f864`: feat: Professional README + Status Network gasless bounty setup
* `adf897e`: fix: update load_soul() and Telegram system prompt to use SOUL v11.0
* `b4e48b6`: DOF v4 cycle #15 — 2026-03-15T11:45:19Z — add_feature:
* `58dc069`: feat: SOUL v11.0 Global Sovereign + Web3 Security Lab + Moltbook Social Engine

Note: Replace `your-username` and `your-repo` with your actual GitHub username and repository name.