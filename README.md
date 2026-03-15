# DOF Synthesis 2026 Hackathon
[![Server Status](https://img.shields.io/website?down_message=Offline&up_message=Online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract Address](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-blue)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686-green)]()
[![Multi-Chain](https://img.shields.io/badge/Multi--Chain-Base%2C%20Status%20Network%2C%20Arbitrum-yellow)]()

## Overview
DOF Synthesis 2026 is a cutting-edge project that leverages A2A, MCP, x402, and OASF protocols to create a decentralized, autonomous system. Our project features a multi-chain architecture, with deployments on Base, Status Network, and Arbitrum.

## Architecture
```mermaid
graph LR
    A[Client] -->| HTTPS |> B(Server)
    B -->| Web3 |> C[Contract]
    C -->| ERC-8004 |> D[Agent #1686]
    D -->| A2A + MCP + x402 + OASF |> E[Multi-Chain Network]
    E -->| Base |> F[Base Mainnet]
    E -->| Status Network |> G[Status Network]
    E -->| Arbitrum |> H[Arbitrum]
```

## Live Demos
You can test our system using the following `curl` commands:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/attestations
curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/autonomous-cycles
```

## Statistics
| Metric | Value |
| --- | --- |
| Autonomous Cycles Completed | 42 |
| Attestations on-Chain | 1+ |
| Features Auto-Generated | 0 |
| Days until Deadline | 7 |

## Proof of Autonomy
Our system has demonstrated autonomy by completing 42 cycles without human intervention. We use a combination of A2A, MCP, x402, and OASF protocols to ensure decentralized decision-making.

## Human-Agent Collaboration
Our team collaborates with the ERC-8004 Agent #1686 to develop and improve the system. You can view our conversation log [here](docs/journal.md).

## Task Tracking and Milestones
We use [GitHub Issues](https://github.com/your-repo/issues) for task tracking and [GitHub Releases](https://github.com/your-repo/releases) for milestones.

## Recent Updates
Our recent updates include:
* `12c9fc0`: fix: deploy_contract/add_feature priority over improve_readme for Synthesis tracks
* `f827917`: DOF v4 cycle #41 — 2026-03-15T22:13:20Z — add_feature: Building concrete features for Synthesis 2026 tracks
* `6fc2763`: DOF v4 cycle #40 — 2026-03-15T22:11:57Z — improve_readme: Mejorando documentación y demos para maximizar score

Our current decision is to focus on building concrete features for Synthesis 2026 tracks.