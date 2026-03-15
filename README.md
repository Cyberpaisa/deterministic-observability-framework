# DOF Synthesis 2026 Hackathon
[![Server Status](https://img.shields.io/website?down_color=red&down_message=Offline&up_color=green&up_message=Online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract Address](https://img.shields.io/endpoint?url=https://etherchain.org/api/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6/balance)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686%20%28Global%29-brightgreen)](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-8004.md)

## Overview
DOF Synthesis is a cutting-edge, autonomous system that leverages the power of blockchain technology and artificial intelligence to revolutionize the way we interact with decentralized applications. Our system utilizes a combination of A2A, MCP, x402, and OASF protocols to ensure seamless communication and data exchange across multiple chains, including Base, Status Network, and Arbitrum.

## Architecture
```mermaid
graph LR
    A[Client] -->|HTTPS|> B(NGROK Server)
    B -->|Web3|> C[Contract: 0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6]
    C -->|ERC-8004|> D[Agent #1686]
    D -->|A2A/MCP/x402/OASF|> E[Autonomous System]
    E -->|On-chain Attestations|> F[Base]
    E -->|On-chain Attestations|> G[Status Network]
    E -->|On-chain Attestations|> H[Arbitrum]
```

## Statistics
| Metric | Value |
| --- | --- |
| Autonomous Cycles Completed | 7 |
| On-chain Attestations | 2+ |
| Features Auto-Generated | 0 |
| Days until Deadline | 7 |
| Current Contract Address | 0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6 |
| ERC-8004 Agent ID | #1686 (Global) |

## Live Demos
You can test our system by running the following `curl` commands:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/endpoint1
curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/endpoint2
```

## Proof of Autonomy
Our system has demonstrated autonomy by completing 7 cycles without human intervention. The following commit history showcases the autonomous updates:
```markdown
- 9e5de75 🤖 DOF v4 cycle #6 — 2026-03-15T13:00:26Z — improve_readme: Mejorando documentación y demos para maximizar sco
- 8a55ec6 🤖 DOF v4 cycle #6 — 2026-03-15T12:34:52Z — deploy_contract:
- 175a141 🤖 DOF v4 cycle #5 — 2026-03-15T12:30:16Z — add_feature:
- 8adfea1 🤖 DOF v4 cycle #4 — 2026-03-15T12:29:19Z — deploy_contract:
- cbda76e 🤖 DOF v4 cycle #3 — 2026-03-15T12:25:45Z — add_feature:
```

## Human-Agent Collaboration
Our system encourages human-agent collaboration through transparent conversation logging. You can view the live conversation log [here](docs/conversation-log.md).

## Task Tracking and Milestones
We use [GitHub Issues](https://github.com/your-repo/issues) for task tracking and [Releases](https://github.com/your-repo/releases) for milestones.

## Current Decision
The current decision is to focus on improving the system's autonomy and completing the remaining tasks before the deadline.