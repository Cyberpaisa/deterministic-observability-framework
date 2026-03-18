# DOF Synthesis 2026 Hackathon
[![Server Status](https://img.shields.io/website?down_message=Offline&up_message=Online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract Address](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-blue)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686-blue)]()
[![Multi-Chain](https://img.shields.io/badge/Multi--Chain-Base%2C%20Status%20Network%2C%20Arbitrum-blue)]()

## Overview
DOF Synthesis 2026 is a cutting-edge hackathon project that leverages the power of A2A, MCP, x402, and OASF protocols to create a decentralized, autonomous system. Our project features a multi-chain architecture, with deployments on Base, Status Network, and Arbitrum.

## Architecture
```mermaid
graph LR
    A[Client] -->| HTTPS |> B(Server)
    B -->| Web3 |> C(Contract)
    C -->| ERC-8004 |> D(Agent)
    D -->| A2A + MCP + x402 + OASF |> E(Multi-Chain)
    E -->| Autonomous Cycles |> F(On-Chain Attestations)
```

## Live Curls
You can interact with our server using the following curls:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/
curl https://vastly-noncontrolling-christena.ngrok-free.dev/contract
```

## Statistics
| Metric | Value |
| --- | --- |
| Autonomous Cycles Completed | 150 |
| On-Chain Attestations | 33+ |
| Auto-Generated Features | 4 |
| Days until Deadline | 4 |

## Proof of Autonomy
Our system has demonstrated autonomy by completing 150 cycles, with 33+ on-chain attestations. The following commits showcase our autonomous feature generation:
* `dcef628`: DOF v4 cycle #149 — 2026-03-18T02:25:34Z — deploy_contract
* `8f126b8`: DOF v4 cycle #149 — 2026-03-18T01:58:28Z — add_feature: Building concrete features for Synthesis 2026 track
* `80a04d8`: DOF v4 cycle #148 — 2026-03-18T01:55:11Z — add_feature
* `3b2aa72`: DOF v4 cycle #148 — 2026-03-18T01:27:18Z — add_feature
* `4b8f014`: DOF v4 cycle #147 — 2026-03-18T01:24:39Z — add_feature: Building concrete features for Synthesis 2026 track

## Human-Agent Collaboration
Our project features a live [Conversation Log](docs/journal.md), where you can track the decision-making process and collaboration between humans and agents. The current decision is: **Building concrete features for Synthesis 2026 tracks**.

## Task Tracking and Milestones
We use [GitHub Issues](https://github.com/your-repo/issues) for task tracking and [Releases](https://github.com/your-repo/releases) for milestones.

## Contract Details
* Contract Address: `0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6` (Base Mainnet)
* ERC-8004 Agent: `#1686` (Global)

Note: Replace `your-repo` with your actual GitHub repository name.