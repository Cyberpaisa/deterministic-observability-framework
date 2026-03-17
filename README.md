# DOF Synthesis 2026 Hackathon
[![Server](https://img.shields.io/badge/Server-https://vastly-noncontrolling-christena.ngrok-free.dev-green)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-orange)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004_Agent-%231686-blue)](#)
[![Multi-chain](https://img.shields.io/badge/Multi--chain-Base,_Status_Network,_Arbitrum-purple)](#)

## Overview
DOF Synthesis 2026 is a cutting-edge hackathon project that leverages the power of A2A, MCP, x402, and OASF protocols to create a decentralized, autonomous, and multi-chain system. Our project features a unique architecture that enables seamless interaction between different blockchain networks.

## Architecture
```mermaid
graph LR
    A[Base Mainnet] -->| ERC-8004 |->> B(ERC-8004 Agent #1686)
    B -->| A2A + MCP + x402 + OASF |->> C[Status Network]
    C -->| OASF |->> D[Arbitrum]
    D -->| x402 |->> B
    style A fill:#f9f,stroke:#333,stroke-width:4px
    style B fill:#f9f,stroke:#333,stroke-width:4px
    style C fill:#f9f,stroke:#333,stroke-width:4px
    style D fill:#f9f,stroke:#333,stroke-width:4px
```

## Live Curls
* **Server:** `curl https://vastly-noncontrolling-christena.ngrok-free.dev`
* **Contract:** `curl https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6.json`

## Stats
| Category | Value |
| --- | --- |
| Autonomous Cycles | 126 |
| Attestations on-chain | 46+ |
| Features Auto-Generated | 4 |
| Days until Deadline | 5 |

## Proof of Autonomy
Our system has completed 126 autonomous cycles, with 46+ attestations on-chain. This demonstrates the effectiveness and reliability of our decentralized architecture.

## Human-Agent Collaboration
Our project utilizes a collaborative approach between humans and agents. For more information on our conversation log, please visit: [docs/journal.md](docs/journal.md)

## Task Tracking and Milestones
We use [GitHub Issues](https://github.com/your-repo/issues) for task tracking and [Releases](https://github.com/your-repo/releases) for milestones.

## Git Log
* `9aea1fa`: DOF v4 cycle #125 — 2026-03-17T13:05:58Z — none:
* `f6bab73`: DOF v4 cycle #124 — 2026-03-17T12:31:00Z — add_feature: Building concrete features for Synthesis 2026 trac
* `4cfbf9e`: DOF v4 cycle #123 — 2026-03-17T10:57:21Z — add_feature: Building concrete features for Synthesis 2026 trac
* `6c02807`: DOF v4 cycle #122 — 2026-03-17T10:26:36Z — add_feature: Building concrete features for Synthesis 2026 trac
* `bcfa67e`: DOF v4 cycle #121 — 2026-03-17T09:56:00Z — add_feature: Building concrete features for Synthesis 2026 trac

Note: Replace `your-repo` with your actual GitHub repository name.