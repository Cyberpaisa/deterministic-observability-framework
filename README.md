# DOF Synthesis 2026 Hackathon
[![Server Status](https://img.shields.io/website?down_message=Offline&label=Server%20Status&up_message=Online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract Address](https://img.shields.io/ethereum/mainnet/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686-orange)](https://erc8004.org/)
[![Multi-Chain](https://img.shields.io/badge/Multi--Chain-Base%2C%20Status%20Network%2C%20Arbitrum-blue)](https://docs.google.com/document/d/1pT1Hc...)
[![Protocols](https://img.shields.io/badge/Protocols-A2A%20%2B%20MCP%20%2B%20x402%20%2B%20OASF-green)](https://docs.google.com/document/d/1pT1Hc...)

## Overview
DOF Synthesis 2026 is a cutting-edge hackathon project that leverages the power of blockchain and artificial intelligence to create a decentralized, autonomous, and multi-chain system. Our project utilizes the ERC-8004 Agent #1686 (Global) and supports A2A + MCP + x402 + OASF protocols, ensuring seamless communication and interaction across various blockchain networks.

## Architecture
The architecture of our system can be visualized as follows:
```mermaid
graph LR
    participant Blockchain as "Base, Status Network, Arbitrum"
    participant Contract as "0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6"
    participant Agent as "ERC-8004 Agent #1686"
    participant Server as "https://vastly-noncontrolling-christena.ngrok-free.dev"
    participant Client as "Users"

    note "A2A + MCP + x402 + OASF protocols"
    Client->>Server: Request
    Server->>Contract: Transaction
    Contract->>Blockchain: Smart Contract Execution
    Blockchain->>Agent: Event Notification
    Agent->>Server: Update
    Server->>Client: Response
```

## Live Curls
To interact with our server, you can use the following `curl` commands:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev
curl -X POST -H "Content-Type: application/json" -d '{"key":"value"}' https://vastly-noncontrolling-christena.ngrok-free.dev/api/endpoint
```

## Statistics
Our project has achieved the following milestones:
| Metric | Value |
| --- | --- |
| Autonomous Cycles Completed | 93 |
| Attestations on-chain | 68+ |
| Auto-Generated Features | 5 |
| Days until Deadline | 6 |

## Proof of Autonomy
Our system has demonstrated autonomy by completing 93 cycles without human intervention. The decision-making process is currently focused on **Building concrete features for Synthesis 2026 tracks**.

## Git Log
Our recent commit history is as follows:
```markdown
* 09ca2a8 🤖 DOF v4 cycle #92 — 2026-03-16T20:29:02Z — add_feature: Building concrete features for Synthesis 2026 trac
* 4ca5a17 🤖 DOF v4 cycle #91 — 2026-03-16T19:58:43Z — add_feature: Building concrete features for Synthesis 2026 trac
* daf60be 🤖 DOF v4 cycle #90 — 2026-03-16T19:28:24Z — add_feature: Building concrete features for Synthesis 2026 trac
* f8952a7 🤖 DOF v4 cycle #89 — 2026-03-16T18:58:07Z — add_feature: Building concrete features for Synthesis 2026 trac
* e4c6c19 🤖 DOF v4 cycle #88 — 2026-03-16T18:27:51Z — add_feature: Building concrete features for Synthesis 2026 trac
```

## Human-Agent Collaboration
Our project utilizes a human-agent collaboration approach, where humans and AI agents work together to achieve common goals. The conversation log can be found [here](docs/journal.md).

## Task Tracking and Milestones
We use [GitHub Issues](https://github.com/username/repository/issues) for task tracking and [Releases](https://github.com/username/repository/releases) for milestones.

## Join the Conversation
Join our conversation on [docs/journal.md](docs/journal.md) to learn more about our project and contribute to the development of DOF Synthesis 2026.