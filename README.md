# DOF Synthesis 2026 Hackathon
[![Server Status](https://img.shields.io/website?down_message=Offline&up_message=Online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract Address](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-orange)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686-blue)]()
[![Multi-Chain](https://img.shields.io/badge/Multi--Chain-Base%2C%20Status%20Network%2C%20Arbitrum-green)]()

## Overview
DOF Synthesis is a cutting-edge project that leverages A2A, MCP, x402, and OASF protocols to create a decentralized, autonomous system. Our project features a multi-chain architecture, currently deployed on Base, Status Network, and Arbitrum.

## Architecture
```mermaid
graph LR
    A[Client] -->| HTTPS |> B(Server)
    B -->| Web3 |> C[Contract]
    C -->| ERC-8004 |> D[Agent #1686]
    D -->| A2A + MCP + x402 + OASF |> E[Multi-Chain Network]
    E -->| Base |> F[Base Network]
    E -->| Status Network |> G[Status Network]
    E -->| Arbitrum |> H[Arbitrum Network]
```

## Live Curls
You can interact with our server using the following curls:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev
curl -X POST -H "Content-Type: application/json" -d '{"json":"data"}' https://vastly-noncontrolling-christena.ngrok-free.dev
```

## Statistics
| Metric | Value |
| --- | --- |
| Autonomous Cycles Completed | 179 |
| Attestations On-Chain | 31+ |
| Features Auto-Generated | 4 |
| Days Until Deadline | 3 |

## Proof of Autonomy
Our system has demonstrated autonomy by completing 179 cycles without human intervention. The contract address `0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6` on the Base Mainnet has been verified to be functional and interacting with the ERC-8004 Agent #1686.

## Human-Agent Collaboration
Our team collaborates with the agent through a live [Conversation Log](docs/journal.md). This log documents all interactions, decisions, and outcomes, providing transparency and accountability.

## Development
We use [GitHub Issues](https://github.com/your-repo/issues) for task tracking and [Releases](https://github.com/your-repo/releases) for milestones. Our recent commits include:
* `6170721`: DOF v4 cycle #178 — 2026-03-19T03:52:31Z — deploy_contract
* `37d3766`: DOF v4 cycle #180 — 2026-03-19T03:43:01Z — improve_readme
* `6958eb9`: DOF v4 cycle #179 — 2026-03-19T03:32:56Z — add_feature
* `a41ca75`: DOF v4 cycle #178 — 2026-03-19T03:25:03Z — add_feature
* `4bb6a41`: DOF v4 cycle #177 — 2026-03-19T03:22:17Z — fix_bug

Note: Replace `your-repo` with your actual GitHub repository name.