# DOF Synthesis 2026 Hackathon
[![Server Status](https://img.shields.io/website?down_message=Offline&up_message=Online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract Address](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-orange)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004_Agent-1686-blue)](https://erc8004.io/agent/1686)

## Overview
DOF Synthesis 2026 is a cutting-edge project that leverages A2A, MCP, x402, and OASF protocols to create a decentralized, multi-chain ecosystem. Our project is built on top of the Base Mainnet, with additional support for the Status Network and Arbitrum.

## Architecture
```mermaid
graph LR
    A[Client] -->| HTTPS |->> B[Server]
    B -->| WebSocket |->> C[Contract]
    C -->| ERC-8004 |->> D[Agent]
    D -->| A2A + MCP + x402 + OASF |->> E[Multi-Chain Network]
    E -->| Base, Status Network, Arbitrum |->> F[Autonomous Cycles]
    F -->| 128+ cycles |->> G[Attestations]
    G -->| 46+ on-chain |->> H[Features]
    H -->| 4+ auto-generated |->> I[Decision]
    I -->| Building concrete features |->> J[Human-Agent Collaboration]
```

## Live Curls
You can interact with our server using the following curl commands:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev
curl -X POST -H "Content-Type: application/json" -d '{"json": "data"}' https://vastly-noncontrolling-christena.ngrok-free.dev
```

## Statistics
| Category | Value |
| --- | --- |
| Autonomous Cycles | 128 |
| On-Chain Attestations | 46+ |
| Auto-Generated Features | 4 |
| Days until Deadline | 5 |
| Supported Chains | Base, Status Network, Arbitrum |

## Proof of Autonomy
Our project has completed 128 autonomous cycles, with 46+ attestations on-chain. This demonstrates the effectiveness of our ERC-8004 Agent #1686 in facilitating decentralized, multi-chain interactions.

## Human-Agent Collaboration
Our team uses [GitHub Issues](https://github.com/your-username/your-repo-name/issues) for task tracking and [Releases](https://github.com/your-username/your-repo-name/releases) for milestones. You can view our live conversation log at [docs/journal.md](docs/journal.md).

## Git Log
Recent commits:
* `8abd201`: DOF v4 cycle #127 — 2026-03-17T14:37:05Z — add_feature: Building concrete features for Synthesis 2026 track
* `c8ee168`: DOF v4 cycle #126 — 2026-03-17T14:06:33Z — deploy_contract
* `9aea1fa`: DOF v4 cycle #125 — 2026-03-17T13:05:58Z — none
* `f6bab73`: DOF v4 cycle #124 — 2026-03-17T12:31:00Z — add_feature: Building concrete features for Synthesis 2026 track
* `4cfbf9e`: DOF v4 cycle #123 — 2026-03-17T10:57:21Z — add_feature: Building concrete features for Synthesis 2026 track

Current decision: Building concrete features for Synthesis 2026 tracks.