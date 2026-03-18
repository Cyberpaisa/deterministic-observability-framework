# DOF Synthesis 2026 Hackathon
[![Server Status](https://img.shields.io/website?down_message=Offline&up_message=Online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract Address](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-blue)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686-blue)]()
[![Multi-Chain](https://img.shields.io/badge/Multi--Chain-Base%2C%20Status%20Network%2C%20Arbitrum-blue)]()

## Overview
The DOF Synthesis 2026 hackathon project is a cutting-edge, autonomous system utilizing A2A, MCP, x402, and OASF protocols. Our ERC-8004 Agent #1686 operates on the Base Mainnet, with a presence on multiple chains, including Status Network and Arbitrum.

## Architecture
```mermaid
graph LR
    A[Server] -->|https|> B[Contract]
    B -->|ERC-8004|> C[Agent #1686]
    C -->|A2A + MCP + x402 + OASF|> D[Multi-Chain]
    D -->|Base, Status Network, Arbitrum|> E[Autonomous Cycles]
```

## Statistics
| Metric | Value |
| --- | --- |
| Attestations on-chain | 34+ |
| Autonomous cycles completed | 151 |
| Features auto-generated | 4 |
| Days until deadline | 4 |

## Live Curls
You can interact with our server using the following curls:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev
```

## Proof of Autonomy
Our system has demonstrated autonomy through the completion of 151 cycles, with 4 features auto-generated. The contract address is [0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6).

## Human-Agent Collaboration
Our team collaborates with the agent through a live [Conversation Log](docs/journal.md). This log tracks our decision-making process and interactions with the agent.

## Task Tracking and Milestones
We use [GitHub Issues](https://github.com/your-repo/issues) for task tracking and [Releases](https://github.com/your-repo/releases) for milestones.

## Git Log
Recent commits:
* `4bae2f2`: DOF v4 cycle #150 — 2026-03-18T02:56:08Z — deploy_contract
* `b33cf97`: DOF v4 cycle #150 — 2026-03-18T02:29:06Z — add_feature: Building concrete features for Synthesis 2026 tracks
* `dcef628`: DOF v4 cycle #149 — 2026-03-18T02:25:34Z — deploy_contract
* `8f126b8`: DOF v4 cycle #149 — 2026-03-18T01:58:28Z — add_feature: Building concrete features for Synthesis 2026 tracks
* `80a04d8`: DOF v4 cycle #148 — 2026-03-18T01:55:11Z — add_feature

Current decision: Building concrete features for Synthesis 2026 tracks.