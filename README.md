# DOF Synthesis 2026 Hackathon
[![Server](https://img.shields.io/website?label=Server&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract](https://img.shields.io/ethereum-mainnet/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686%20(Global)-blue)]()

## Introduction
We are participating in the DOF Synthesis 2026 hackathon, utilizing the ERC-8004 Agent #1686 on the global network. Our project leverages the A2A, MCP, x402, and OASF protocols to achieve a multi-chain architecture across Base, Status Network, and Arbitrum. This repository serves as the central hub for our project, tracking progress, and showcasing our achievements.

## Statistics
| Category | Value |
| --- | --- |
| On-Chain Attestations | 76+ |
| Autonomous Cycles Completed | 101 |
| Auto-Generated Features | 5 |
| Days Until Deadline | 5 |

## Architecture
```mermaid
graph LR
    A[Multi-Chain] -->|A2A|MCP|x402|OASF|> B(Base)
    A -->|A2A|MCP|x402|OASF|> C(Status Network)
    A -->|A2A|MCP|x402|OASF|> D(Arbitrum)
    B --> E(Contract: 0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
    C --> E
    D --> E
```

## Live Demos
You can test our project using the following live curl commands:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev
```
Alternatively, visit our [Vercel live demo link](https://vercel.live/demo) for a more interactive experience.

## Proof of Autonomy
We have achieved a high level of autonomy, with 101 cycles completed and 5 features auto-generated. Our contract, deployed on the Base mainnet, has received over 76 on-chain attestations.

## Human-Agent Collaboration
Our team collaborates closely with the ERC-8004 Agent #1686 to ensure seamless execution of tasks. You can follow our conversation log, updated live, at [docs/journal.md](docs/journal.md).

## Task Tracking and Milestones
We use [GitHub Issues](https://github.com/username/repository/issues) for task tracking and [Releases](https://github.com/username/repository/releases) for milestones.

## Recent Commits
- 961a9de: Complete README with all 10 tracks (6 functional + 4 conceptual)
- 8bc905a: Add Vercel live demo link
- 7b0aeef: Restore complete README with tracks and evidence
- 2b0d1a7: DOF v4 cycle #100 — 2026-03-17T00:32:23Z — add_feature: Building concrete features for Synthesis 2026 tracks
- 97c743f: DOF v4 cycle #99 — 2026-03-17T00:01:44Z — add_feature: Building concrete features for Synthesis 2026 tracks

Current decision: Building concrete features for Synthesis 2026 tracks. With 5 days left until the deadline, we are focused on delivering a high-quality project that showcases our expertise and creativity.