# DOF Synthesis 2026 Hackathon
[![Server Status](https://img.shields.io/website?down_message=Offline&up_message=Online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract Address](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-blue)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686-green)]()

## Overview
DOF Synthesis 2026 is a cutting-edge project that leverages the power of A2A, MCP, x402, and OASF protocols to create a decentralized, multi-chain system. Our project is built on top of the Base Mainnet, with additional support for Status Network and Arbitrum.

## Architecture
```mermaid
graph LR
    A[Client] -->| HTTPS |> B(NGROK Server)
    B -->| Web3 |> C[Contract: 0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6]
    C -->| ERC-8004 |> D[Agent #1686]
    D -->| A2A + MCP + x402 + OASF |> E[Multi-Chain Network]
    E -->| Base, Status Network, Arbitrum |> F[On-Chain Attestations]
```

## Statistics
| Metric | Value |
| --- | --- |
| Autonomous Cycles Completed | 140 |
| On-Chain Attestations | 31+ |
| Auto-Generated Features | 5 |
| Days until Deadline | 5 |

## Live API Endpoints
You can test our API endpoints using the following `curl` commands:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/status
curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/attestations
```

## Proof of Autonomy
Our system has demonstrated autonomy by completing 140 cycles without human intervention. The contract address `0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6` has been verified on the Base Mainnet, and our ERC-8004 Agent #1686 has been successfully integrated.

## Human-Agent Collaboration
Our team has been working closely with the AI agent to develop and refine the system. You can view our conversation log, which is updated in real-time, at [docs/journal.md](docs/journal.md).

## Development and Tracking
We use [GitHub Issues](https://github.com/your-repo/issues) for task tracking and [GitHub Releases](https://github.com/your-repo/releases) for milestones. Our commit history is available for review, with notable commits including:
* `85ade2e`: DOF v4 cycle #139 — 2026-03-17T20:57:48Z — add_feature
* `d8822cc`: DOF v4 cycle #138 — 2026-03-17T20:27:22Z — add_feature
* `86985ca`: docs: final README v2 — clean professional, judge-ready, agent-proof

Note: Replace `your-repo` with your actual GitHub repository name.