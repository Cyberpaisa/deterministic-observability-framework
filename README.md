# DOF Synthesis 2026 Hackathon
[![Server Status](https://img.shields.io/website?down_color=red&down_message=Offline&up_color=green&up_message=Online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract Address](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-blue)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-1686%20%28Global%29-blue)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)

## Overview
DOF Synthesis 2026 is a cutting-edge project that utilizes A2A, MCP, x402, and OASF protocols to achieve multi-chain compatibility across Base, Status Network, and Arbitrum. Our project features a robust ERC-8004 agent, with 69+ attestations on-chain and 94 autonomous cycles completed.

## Architecture
```mermaid
graph LR
    A[Server] -->|https|> B[Contract]
    B -->|ERC-8004|> C[Agent]
    C -->|A2A + MCP + x402 + OASF|> D[Multichain]
    D -->|Base|> E[Status Network]
    D -->|Arbitrum|> F[Autonomous Cycles]
    F -->|69+ Attestations|> G[On-Chain]
```

## Live Demos
You can interact with our server using the following live `curl` commands:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev
curl -X POST https://vastly-noncontrolling-christena.ngrok-free.dev/features
```

## Proof of Autonomy
Our project has achieved significant autonomous milestones, including:
| Metric | Value |
| --- | --- |
| Autonomous Cycles | 94 |
| Attestations On-Chain | 69+ |
| Auto-Generated Features | 5 |

## Human-Agent Collaboration
Our team collaborates closely with the DOF agent to ensure seamless development and deployment. You can follow our conversation log in real-time at [docs/journal.md](docs/journal.md).

## Project Management
We use [GitHub Issues](https://github.com/username/repository/issues) for task tracking and [Releases](https://github.com/username/repository/releases) for milestones.

## Statistics
| Category | Value |
| --- | --- |
| Days until Deadline | 6 |
| Contract Address | 0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6 |
| ERC-8004 Agent | #1686 (Global) |
| Chains | Base, Status Network, Arbitrum |
| Protocols | A2A, MCP, x402, OASF |

## Recent Commits
* 0d050b2 🤖 DOF v4 cycle #93 — 2026-03-16T20:59:28Z — add_feature: Building concrete features for Synthesis 2026 track
* 09ca2a8 🤖 DOF v4 cycle #92 — 2026-03-16T20:29:02Z — add_feature: Building concrete features for Synthesis 2026 track
* 4ca5a17 🤖 DOF v4 cycle #91 — 2026-03-16T19:58:43Z — add_feature: Building concrete features for Synthesis 2026 track
* daf60be 🤖 DOF v4 cycle #90 — 2026-03-16T19:28:24Z — add_feature: Building concrete features for Synthesis 2026 track
* f8952a7 🤖 DOF v4 cycle #89 — 2026-03-16T18:58:07Z — add_feature: Building concrete features for Synthesis 2026 track

Current decision: Building concrete features for Synthesis 2026 tracks