# DOF Synthesis 2026 Hackathon
[![Server Status](https://img.shields.io/website?down_message=Offline&up_message=Online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686-blue)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![Contract Address](https://img.shields.io/badge/Contract%20Address-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-orange)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)

## Overview
DOF Synthesis is a cutting-edge project that leverages A2A, MCP, x402, and OASF protocols to create a decentralized, autonomous system. Our project utilizes a multi-chain approach, currently supporting Base, Status Network, and Arbitrum.

### Key Statistics
| Metric | Value |
| --- | --- |
| Attestations on-chain | 31+ |
| Autonomous Cycles Completed | 158 |
| Auto-generated Features | 3 |
| Days until Deadline | 4 |

## Architecture
Our system's architecture is designed to facilitate seamless interaction between various components. The following diagram illustrates the high-level architecture of our system:
```mermaid
graph LR
    A[ERC-8004 Agent #1686] -->|Interacts with|> B[Contract: 0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6]
    B -->|Utilizes|> C[A2A + MCP + x402 + OASF protocols]
    C -->|Enables|> D[Multi-chain support: Base, Status Network, Arbitrum]
    D -->|Facilitates|> E[Autonomous decision-making and execution]
```

## Live Data
You can view live data from our system using the following curls:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/status
curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/cycles
```

## Proof of Autonomy
Our system has demonstrated autonomy by completing 158 cycles, with 31+ attestations on-chain. This showcases the system's ability to operate independently and make decisions without human intervention.

## Human-Agent Collaboration
Our team collaborates closely with the ERC-8004 Agent #1686 to ensure seamless operation and continuous improvement. You can view our live conversation log, which tracks our interactions and decision-making process, at [docs/journal.md](docs/journal.md).

## Development and Tracking
We use GitHub Issues for task tracking and Releases for milestones. Our project's progress can be tracked through our [Git log](https://github.com/your-repo-name/commits/main).

### Recent Commits:
* 79a5f2e: Auto-commit: Interacción con Cyber Paisa
* b482fa6: Auto-commit: Interacción con Cyber Paisa
* 4df8ec2: 🤖 DOF v4 cycle #157 — 2026-03-18T21:51:07Z — add_feature:
* 0135ab0: docs: restore TRUE conversation log with all Telegram history
* 35474ba: docs: clean professional conversation log (English, tracks + cycles only)

Join us in pushing the boundaries of autonomous systems!