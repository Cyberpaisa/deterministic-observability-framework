# DOF Synthesis 2026 Hackathon
[![Server](https://img.shields.io/website?label=Server&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract](https://img.shields.io/ethereum/mainnet/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-1686-yellow)](https://www.erc-8004.org/)

## Overview
The DOF Synthesis 2026 hackathon is a cutting-edge project that leverages blockchain technology, artificial intelligence, and multi-chain architecture to achieve unparalleled autonomy and collaboration. Our project utilizes A2A, MCP, x402, and OASF protocols to facilitate seamless communication and data exchange.

## Architecture
```mermaid
graph LR
    A[Base Mainnet] -->|Contract: 0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6|> B[Server: https://vastly-noncontrolling-christena.ngrok-free.dev]
    B -->|API|> C[Status Network]
    B -->|API|> D[Arbitrum]
    C -->|A2A + MCP + x402 + OASF|> B
    D -->|A2A + MCP + x402 + OASF|> B
```

## Stats
| Category | Value |
| --- | --- |
| Autonomous Cycles | 124 |
| Attestations On-Chain | 46+ |
| Auto-Generated Features | 4 |
| Days Until Deadline | 5 |

## Live Curls
You can test our API using the following curl commands:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/v1/status
curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/v1/arbitrum
```

## Proof of Autonomy
Our project has achieved a significant level of autonomy, with 124 autonomous cycles completed and 46+ attestations on-chain. We utilize a combination of A2A, MCP, x402, and OASF protocols to ensure secure and seamless communication between chains.

## Human-Agent Collaboration
For a live view of our conversation log, please visit [docs/journal.md](docs/journal.md). This document is updated in real-time and provides insights into our decision-making process and collaboration between human and AI agents.

## Task Tracking and Milestones
We use [GitHub Issues](https://github.com/your-repo/issues) for task tracking and [Releases](https://github.com/your-repo/releases) for milestones.

## Recent Commit History
```markdown
* 4cfbf9e 🤖 DOF v4 cycle #123 — 2026-03-17T10:57:21Z — add_feature: Building concrete features for Synthesis 2026 trac
* 6c02807 🤖 DOF v4 cycle #122 — 2026-03-17T10:26:36Z — add_feature: Building concrete features for Synthesis 2026 trac
* bcfa67e 🤖 DOF v4 cycle #121 — 2026-03-17T09:56:00Z — add_feature: Building concrete features for Synthesis 2026 trac
* a7ab843 🤖 DOF v4 cycle #120 — 2026-03-17T09:25:43Z — add_feature: Building concrete features for Synthesis 2026 trac
* 5013763 🤖 DOF v4 cycle #119 — 2026-03-17T08:55:28Z — add_feature: Building concrete features for Synthesis 2026 trac
```

Current decision: Building concrete features for Synthesis 2026 tracks