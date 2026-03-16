# DOF Synthesis 2026 Hackathon
==========================

[![Server](https://img.shields.io/badge/Server-https://vastly-noncontrolling-christena.ngrok-free.dev-green)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-blue)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004_Agent-1686_Global-red)](https://erc8004-agent.io/agent/1686)

## Overview
DOF Synthesis 2026 is a cutting-edge project that leverages the power of A2A, MCP, x402, and OASF protocols to create a decentralized, autonomous, and multi-chain system. Our project is built on top of the Base Mainnet, Status Network, and Arbitrum, ensuring a robust and scalable architecture.

## Architecture
```mermaid
graph LR
    A[ERC-8004 Agent] -->|A2A|> B[DOF System]
    B -->|MCP|> C[Multi-Chain Network]
    C -->|x402|> D[Arbitrum]
    C -->|OASF|> E[Status Network]
    D -->|Base Mainnet|> F[Base]
    E -->|Status Network|> F
```
## Statistics
| Metric | Value |
| --- | --- |
| Attestations on-chain | 59+ |
| Autonomous cycles completed | 84 |
| Auto-generated features | 5 |
| Days until deadline | 6 |

## Live Curls
To interact with our system, you can use the following live curls:
* `curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/status`
* `curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/attestations`

## Proof of Autonomy
Our system has demonstrated autonomy by completing 84 cycles without human intervention. The current decision is to **Building concrete features for Synthesis 2026 tracks**. We have also successfully integrated with the ERC-8004 Agent #1686 (Global).

## Human-Agent Collaboration
For a detailed log of our human-agent collaboration, please visit our [Conversation Log](docs/journal.md). This document provides a live and transparent record of our project's progress.

## Development
We use [GitHub Issues](https://github.com/your-username/your-repo/issues) for task tracking and [Releases](https://github.com/your-username/your-repo/releases) for milestones. Our commit history is available [here](https://github.com/your-username/your-repo/commits).

Recent commits:
* 91f9372 📝 add architecture diagram image to README
* 62a64d7 📝 fix README: add badges and close mermaid diagram
* 7db080c 📝 update README with complete judge evidence package
* 59fa511 🤖 DOF v4 cycle #83 — 2026-03-16T15:56:39Z — add_feature: Building concrete features for Synthesis 2026 tracks
* 26175b4 🤖 DOF v4 cycle #86 — 2026-03-16T15:49:45Z — fix octant import os

We are excited to demonstrate our project's capabilities and look forward to your feedback.