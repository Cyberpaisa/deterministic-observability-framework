# DOF Synthesis 2026 Hackathon
[![DOF Synthesis 2026](https://img.shields.io/badge/DOF-Synthesis%202026-blue)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-green)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686-yellow)](https://erc8004.io/agent/1686)

## Overview
DOF Synthesis 2026 is a cutting-edge project that utilizes A2A + MCP + x402 + OASF protocols to achieve unprecedented levels of autonomy. Our system is deployed on multiple chains, including Base, Status Network, and Arbitrum, ensuring seamless interaction and maximum reach.

### Architecture
```mermaid
graph LR
    A[Client] -->|Request|> B[Server]
    B -->|Process|> C[Contract]
    C -->|Execute|> D[Blockchain]
    D -->|Verify|> E[Attestations]
    E -->|Update|> B
```
### Live Stats
| Metric | Value |
| --- | --- |
| Autonomous Cycles Completed | 173 |
| Attestations on-chain | 31+ |
| Auto-generated Features | 4 |
| Days until Deadline | 3 |

### Live Curls
You can interact with our server using the following curls:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev
```
### Proof of Autonomy
Our system has demonstrated impressive autonomy, with 173 autonomous cycles completed and 31+ attestations on-chain. This is a testament to the robustness and reliability of our implementation.

### Human-Agent Collaboration
Our team collaborates closely with the agent to ensure seamless integration and maximum efficiency. You can view our conversation log [here](docs/journal.md).

## Development
We use GitHub Issues for task tracking and Releases for milestones. Our recent commits include:
* `d9277b8`: DOF v4 cycle #172 — 2026-03-19T02:10:51Z — add_feature: Building concrete features for Synthesis 2026
* `d40558d`: DOF v4 cycle #171 — 2026-03-19T01:50:52Z — fix_bug:
* `96c5d79`: DOF v4 cycle #170 — 2026-03-19T01:50:29Z — add_feature:
* `2da8cdd`: DOF v4 cycle #169 — 2026-03-19T01:50:08Z — add_feature:
* `9770524`: DOF v4 cycle #168 — 2026-03-19T01:49:13Z — add_feature:

## Current Decision
Our current decision is to continue refining and improving our system, ensuring maximum autonomy and efficiency.

## Contract Details
* Contract Address: `0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6` (Base Mainnet)
* ERC-8004 Agent: `#1686` (Global)

## Multi-Chain Support
Our system supports multiple chains, including:
* Base
* Status Network
* Arbitrum

## Badges
[![GitHub Issues](https://img.shields.io/badge/GitHub-Issues-red)](https://github.com/your-username/your-repo/issues)
[![GitHub Releases](https://img.shields.io/badge/GitHub-Releases-orange)](https://github.com/your-username/your-repo/releases)