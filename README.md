# DOF Synthesis 2026 Hackathon
=====================================

[![Server](https://img.shields.io/website?label=Server&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-blue)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686-green)]()
[![Multi-chain](https://img.shields.io/badge/Multi--chain-Base%2C%20Status%20Network%2C%20Arbitrum-yellow)]()

## Overview
This is the official repository for the DOF Synthesis 2026 hackathon. Our project utilizes the A2A, MCP, x402, and OASF protocols to achieve a high level of autonomy and decentralization. We are currently operating on three blockchain networks: Base, Status Network, and Arbitrum.

## Architecture
```mermaid
graph LR
    A[DOF Server] -->|https|> B[Ngrok Tunnel]
    B -->|https|> C[Client]
    C -->|JSON-RPC|> D[Ethereum Node]
    D -->|Smart Contract|> E[ERC-8004 Agent]
    E -->|On-chain Data|> F[Attestations]
    F -->|Off-chain Data|> G[Autonomous Cycles]
```

## Live Curls
To interact with our server, you can use the following cURL commands:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/healthcheck
curl https://vastly-noncontrolling-christena.ngrok-free.dev/stats
```

## Statistics
| Metric | Value |
| --- | --- |
| Autonomous Cycles | 79 |
| Attestations | 54+ |
| Auto-generated Features | 5 |
| Days until Deadline | 6 |
| Decision Cycles | 78 |
| Blockchain Networks | 3 |

## Proof of Autonomy
Our system has been operating autonomously for an extended period, with 79 cycles completed and 54+ attestations on-chain. This demonstrates the reliability and self-sufficiency of our architecture.

## Human-Agent Collaboration
Our team has been collaborating with the ERC-8004 agent to develop and refine our project. You can view our [conversation log](docs/journal.md) to see the progress we've made.

## Task Tracking and Milestones
We use [GitHub Issues](https://github.com/your-username/your-repo-name/issues) for task tracking and [Releases](https://github.com/your-username/your-repo-name/releases) for milestones.

## Git Log
Here are the recent commit messages:
* ae851c1 🤖 DOF v4 cycle #78 — 2026-03-16T13:25:05Z — add_feature: Building concrete features for Synthesis 2026 trac
* af02edd 🤖 DOF v4 cycle #77 — 2026-03-16T12:54:52Z — add_feature: Building concrete features for Synthesis 2026 trac
* aee5eac 🤖 DOF v4 cycle #76 — 2026-03-16T12:24:36Z — add_feature: Building concrete features for Synthesis 2026 trac
* 60722dd 🤖 DOF v4 cycle #75 — 2026-03-16T11:54:21Z — add_feature: Building concrete features for Synthesis 2026 trac
* bbf4078 🤖 DOF v4 cycle #74 — 2026-03-16T11:24:07Z — add_feature: Building concrete features for Synthesis 2026 trac

Current decision: Building concrete features for Synthesis 2026 tracks

Note: Please replace `your-username` and `your-repo-name` with your actual GitHub username and repository name.