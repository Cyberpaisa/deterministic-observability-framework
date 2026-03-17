# DOF Synthesis 2026 Hackathon
[![Server](https://img.shields.io/website?label=Server&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract](https://img.shields.io/ethereum/mainnet/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686%20(Global)-blue)]()

## Overview
DOF Synthesis 2026 is a cutting-edge project that leverages the power of blockchain and artificial intelligence to create a decentralized, autonomous, and scalable system. Our project utilizes the following protocols:
* A2A
* MCP
* x402
* OASF

We are built on a multi-chain architecture, supporting:
* Base
* Status Network
* Arbitrum

Our system is powered by ERC-8004 Agent #1686 (Global), and has achieved significant milestones:
| Statistic | Value |
| --- | --- |
| Attestations on-chain | 30+ |
| Autonomous cycles completed | 132 |
| Auto-generated features | 3 |
| Days until deadline | 5 |

## Architecture
```mermaid
graph LR
    participant Server as "https://vastly-noncontrolling-christena.ngrok-free.dev"
    participant Contract as "0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6 (Base Mainnet)"
    participant ERC-8004_Agent as "ERC-8004 Agent #1686 (Global)"
    participant Multi-chain as "Base, Status Network, Arbitrum"

    note "A2A, MCP, x402, OASF protocols"
    Server -- > Contract
    Contract -- > ERC-8004_Agent
    ERC-8004_Agent -- > Multi-chain
```

## Live Curls
To interact with our system, you can use the following curl commands:
```bash
# Example curl command to interact with our server
curl https://vastly-noncontrolling-christena.ngrok-free.dev
```

## Proof of Autonomy
Our system has completed 132 autonomous cycles, with a significant number of attestations on-chain (30+). This demonstrates the autonomous nature of our system, which can operate without human intervention.

## Git Log
Our recent git log is as follows:
```markdown
* 067bb3f 🤖 DOF v4 cycle #131 — 2026-03-17T16:16:48Z — add_feature: Building concrete features for Synthesis 2026 trac
* 93f982a 🤖 DOF v4 cycle #130 — 2026-03-17T16:09:28Z — add_feature: Building concrete features for Synthesis 2026 trac
* b184a39 🤖 DOF v4 cycle #129 — 2026-03-17T15:38:53Z — improve_readme:
* 3676215 🤖 DOF v4 cycle #128 — 2026-03-17T15:07:32Z — add_feature: Building concrete features for Synthesis 2026 trac
* 8abd201 🤖 DOF v4 cycle #127 — 2026-03-17T14:37:05Z — add_feature: Building concrete features for Synthesis 2026 trac
```

## Human-Agent Collaboration
For more information on our human-agent collaboration, please refer to our [Conversation Log](docs/journal.md). This log is updated in real-time and provides insights into our decision-making process.

## Task Tracking and Milestones
We use [GitHub Issues](https://github.com/your-repo/issues) for task tracking and [Releases](https://github.com/your-repo/releases) for milestones. You can track our progress and stay up-to-date with the latest developments.

## Contributing
We welcome contributions from the community. If you're interested in contributing, please refer to our [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines.

## Current Decision
Our current decision is focused on continuing to build and improve our system, with a focus on autonomous decision-making and human-agent collaboration. We are committed to delivering a high-quality project that showcases the potential of blockchain and artificial intelligence.