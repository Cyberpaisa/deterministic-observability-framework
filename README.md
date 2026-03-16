# DOF Synthesis 2026 Hackathon
[![Server Status](https://img.shields.io/website?down_color=red&down_message=Offline&up_color=green&up_message=Online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract Address](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-blue)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004_Agent-%231686-9cf)](#)

## Introduction
The DOF Synthesis 2026 hackathon project is a decentralized, autonomous system utilizing the ERC-8004 protocol, with a contract address of 0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6 on the Base Mainnet. Our agent, #1686, operates on multiple chains, including Base, Status Network, and Arbitrum, and supports various protocols such as A2A, MCP, x402, and OASF.

## Architecture
```mermaid
graph LR;
    A2[Server: https://vastly-noncontrolling-christena.ngrok-free.dev] -->|API|> B2[Contract: 0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6];
    B2 -->|ERC-8004|> C2[Agent #1686];
    C2 -->|Multi-chain|> D2[Base, Status Network, Arbitrum];
    D2 -->|Protocols|> E2[A2A, MCP, x402, OASF];
```

## Live Stats
| Metric | Value |
| --- | --- |
| Attestations on-chain | 44+ |
| Autonomous cycles completed | 69 |
| Features auto-generated | 5 |
| Days until deadline | 6 |

## Live Curls
You can test our API using the following cURL commands:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/
curl https://vastly-noncontrolling-christena.ngrok-free.dev/attestations
```

## Proof of Autonomy
Our system has demonstrated autonomy by completing 69 cycles, with the following Git log:
```markdown
13a2036 🤖 DOF v4 cycle #68 — 2026-03-16T08:22:11Z — deploy_contract:
440541a 🤖 DOF v4 cycle #67 — 2026-03-16T07:51:47Z — add_feature: Building concrete features for Synthesis 2026 trac
69a6dbf 🤖 DOF v4 cycle #66 — 2026-03-16T07:21:28Z — add_feature: Building concrete features for Synthesis 2026 trac
bb7073b 🤖 DOF v4 cycle #65 — 2026-03-16T06:51:11Z — add_feature: Building concrete features for Synthesis 2026 trac
9d210a3 🤖 DOF v4 cycle #76 — 2026-03-16T06:32:50Z — add Markee integration for  bounty
```

## Human-Agent Collaboration
For a live log of our human-agent collaboration, please see [docs/journal.md](docs/journal.md). This document is updated in real-time as we work towards our deadline.

## Task Tracking and Milestones
We use GitHub Issues for task tracking and Releases for milestones. Please see our [Issues](https://github.com/your-username/your-repo-name/issues) and [Releases](https://github.com/your-username/your-repo-name/releases) pages for more information.

## Current Decision
Our current decision is to focus on building concrete features for the Synthesis 2026 tracks. We will continue to monitor our progress and adjust our strategy as needed to meet our deadline.