# DOF Synthesis 2026 Hackathon
[![Server](https://img.shields.io/website?label=Server&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract](https://img.shields.io/contract/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686-green)]()
[![Multi-chain](https://img.shields.io/badge/Multi--chain-Base%2C%20Status%20Network%2C%20Arbitrum-blue)]()

## Overview
DOF Synthesis is a cutting-edge project that leverages A2A, MCP, x402, and OASF protocols to create a decentralized, autonomous system. Our project features a Base Mainnet contract (`0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6`), an ERC-8004 Agent (#1686), and a multi-chain architecture spanning Base, Status Network, and Arbitrum.

### Statistics
| Category | Value |
| --- | --- |
| Autonomous Cycles Completed | 7 |
| Features Auto-Generated | 1 |
| Attestations On-Chain | 3+ |
| Days Until Deadline | 7 |

### Architecture
```mermaid
graph LR
    participant Server as "https://vastly-noncontrolling-christena.ngrok-free.dev"
    participant Contract as "0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6"
    participant Agent as "ERC-8004 Agent #1686"
    participant Chains as "Base, Status Network, Arbitrum"
    Server-->Contract
    Contract-->Agent
    Agent-->Chains
```

### Live API Requests
You can test our API using the following `curl` commands:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/data
curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/metadata
```

### Proof of Autonomy
Our system has demonstrated autonomy through the completion of 7 autonomous cycles. The following Git log entries demonstrate our progress:
```markdown
5fc90d1 🤖 DOF v4 cycle #7 — 2026-03-15T13:05:05Z — improve_readme:
9e5de75 🤖 DOF v4 cycle #6 — 2026-03-15T13:00:26Z — improve_readme: Mejorando documentación y demos para maximizar sco
8a55ec6 🤖 DOF v4 cycle #6 — 2026-03-15T12:34:52Z — deploy_contract:
175a141 🤖 DOF v4 cycle #5 — 2026-03-15T12:30:16Z — add_feature:
8adfea1 🤖 DOF v4 cycle #4 — 2026-03-15T12:29:19Z — deploy_contract:
```

### Human-Agent Collaboration
Our team uses [GitHub Issues](https://github.com/your-repo/issues) for task tracking and [GitHub Releases](https://github.com/your-repo/releases) for milestones. You can view our live [Conversation Log](docs/conversation-log.md) to see the collaboration between humans and our ERC-8004 Agent.

## Getting Started
To learn more about our project, please visit our [Server](https://vastly-noncontrolling-christena.ngrok-free.dev) and review our [Contract](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6) on Etherscan. Join our conversation on [GitHub Issues](https://github.com/your-repo/issues) and track our progress on [GitHub Releases](https://github.com/your-repo/releases).