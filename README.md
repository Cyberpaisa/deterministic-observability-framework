# DOF Synthesis 2026 Hackathon
[![Server Status](https://img.shields.io/website?label=Server&up_message=Online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract Address](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-orange)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686-blue)](https://erc8004.io/agent/1686)

## Overview
DOF Synthesis 2026 is a cutting-edge project that utilizes A2A, MCP, x402, and OASF protocols to achieve seamless multi-chain functionality across Base, Status Network, and Arbitrum. Our ERC-8004 Agent #1686 is a key component in this ecosystem, enabling autonomous decision-making and execution.

## Architecture
```mermaid
graph LR
    A[Server] -->|HTTPS|> B[Contract]
    B -->|ERC-8004|> C[Agent #1686]
    C -->|A2A + MCP + x402 + OASF|> D[Multi-Chain Network]
    D -->|Base|> E[Base Chain]
    D -->|Status Network|> F[Status Network Chain]
    D -->|Arbitrum|> G[Arbitrum Chain]
```

## Live Curls
To interact with our server, use the following curls:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev
```
For more information, please refer to our [API documentation](#api-documentation).

## Statistics
| Metric | Value |
| --- | --- |
| Autonomous Cycles Completed | 120 |
| Attestations on-Chain | 42+ |
| Features Auto-Generated | 4 |
| Days until Deadline | 5 |

## Proof of Autonomy
Our project demonstrates autonomy through the following features:
* Autonomous decision-making using ERC-8004 Agent #1686
* Execution of A2A, MCP, x402, and OASF protocols
* Seamless multi-chain functionality across Base, Status Network, and Arbitrum

## Human-Agent Collaboration
Our team collaborates closely with our autonomous agent to ensure seamless execution and decision-making. For more information, please refer to our [Conversation Log](docs/journal.md).

## Task Tracking and Milestones
We use [GitHub Issues](https://github.com/your-repo/issues) for task tracking and [GitHub Releases](https://github.com/your-repo/releases) for milestones.

## Git Log
Recent commits:
* `5013763`: DOF v4 cycle #119 — 2026-03-17T08:55:28Z — add_feature: Building concrete features for Synthesis 2026 tracks
* `f0329d1`: DOF v4 cycle #118 — 2026-03-17T08:25:07Z — add_feature
* `453f2c0`: DOF v4 cycle #117 — 2026-03-17T07:54:43Z — improve_readme
* `9c185c0`: DOF v4 cycle #116 — 2026-03-17T07:24:07Z — add_feature: Building concrete features for Synthesis 2026 tracks
* `e90dff3`: DOF v4 cycle #115 — 2026-03-17T06:53:51Z — add_feature: Building concrete features for Synthesis 2026 tracks

Current decision: Building concrete features for Synthesis 2026 tracks.