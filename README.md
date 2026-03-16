# DOF Synthesis 2026 Hackathon
[![Server Status](https://img.shields.io/website?down_color=red&down_message=Offline&up_color=green&up_message=Online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract Address](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-orange)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686-blue)](https://erc8004.org/)
[![Multi-Chain](https://img.shields.io/badge/Multi--Chain-Base%2C%20Status%20Network%2C%20Arbitrum-yellow)](https://docs.base.org/)
[![Protocols](https://img.shields.io/badge/Protocols-A2A%2C%20MCP%2C%20x402%2C%20OASF-green)](https://docs.oASF.org/)

## Overview
DOF Synthesis 2026 is a cutting-edge project that leverages the power of AI and blockchain technology to create a decentralized, autonomous, and adaptive system. Our project utilizes the A2A, MCP, x402, and OASF protocols to facilitate seamless interactions across multiple chains, including Base, Status Network, and Arbitrum.

## Architecture
```mermaid
graph LR;
    A[Client] -->|HTTPS|> B(NGROK Server);
    B -->|Web3|> C[Contract: 0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6];
    C -->|ERC-8004|> D[Agent #1686];
    D -->|A2A|> E[Autonomous Cycle];
    E -->|MCP|> F[Multi-Chain Protocol];
    F -->|x402|> G[Cross-Chain Interactions];
    G -->|OASF|> H[On-Chain Attestations];
```

## Live Curls
To interact with our server, use the following curl commands:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/
curl -X POST -H "Content-Type: application/json" -d '{"key":"value"}' https://vastly-noncontrolling-christena.ngrok-free.dev/
```

## Statistics
| Metric | Value |
| --- | --- |
| Autonomous Cycles Completed | 59 |
| On-Chain Attestations | 34+ |
| Auto-Generated Features | 3 |
| Days until Deadline | 6 |

## Proof of Autonomy
Our system has demonstrated autonomy through the completion of 59 cycles, with 34+ on-chain attestations. The system has also auto-generated 3 features, further demonstrating its ability to adapt and improve over time.

## Human-Agent Collaboration
For a live view of our collaboration process, please refer to our [Conversation Log](docs/journal.md). This log provides a transparent and detailed account of our decision-making process and the evolution of our project.

## Task Tracking and Milestones
We use [GitHub Issues](https://github.com/DOF-Synthesis-2026/DOF-Synthesis-2026/issues) for task tracking and [Releases](https://github.com/DOF-Synthesis-2026/DOF-Synthesis-2026/releases) for milestones. This allows us to maintain a clear and organized record of our progress and achievements.

## Recent Commits
```markdown
* 24cbcac 🤖 DOF v4 cycle #59 — 2026-03-16T03:49:01Z — add v15.0: autonomous curriculum & meta-cognition
* 98fb4ed 🤖 DOF v4 cycle #58 — 2026-03-16T03:19:24Z — update SOUL v14.2: strategic Moltbook interaction protocol
* 079588f 🤖 DOF v4 cycle #58 — 2026-03-16T03:19:25Z — add_feature: Building concrete features for Synthesis 2026 trac
* ebfc113 🤖 DOF v4 cycle #57 — 2026-03-16T02:49:10Z — add_feature: Building concrete features for Synthesis 2026 trac
* 2e5b048 🧹 archive old conversation log to docs/ backup
```
Current decision: Building concrete features for Synthesis 2026 tracks.