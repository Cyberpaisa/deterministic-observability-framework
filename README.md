# DOF Synthesis 2026 Hackathon
[![Server](https://img.shields.io/badge/Server-https://vastly-noncontrolling-christena.ngrok-free.dev-green)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-blue)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004_Agent-1686_Global-orange)](https://erc8004.io/agent/1686)

## Overview
DOF Synthesis 2026 is a cutting-edge project that leverages A2A, MCP, x402, and OASF protocols to achieve unprecedented levels of autonomy and multi-chain compatibility. Our project utilizes a unique architecture that enables seamless interaction across Base, Status Network, and Arbitrum chains.

## Architecture
```mermaid
graph LR
    A[Base] -->| A2A |<--> B[Status Network]
    B -->| MCP |<--> C[Arbitrum]
    C -->| x402 |<--> A
    A -->| OASF |<--> D[ERC-8004 Agent]
    D -->| Contract |<--> E[0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6]
```

## Statistics
| Category | Value |
| --- | --- |
| Autonomous Cycles Completed | 161 |
| Attestations On-Chain | 32+ |
| Features Auto-Generated | 5 |
| Days Until Deadline | 3 |

## Live Data
You can test our server with the following curl commands:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev
```

## Proof of Autonomy
Our project has achieved a remarkable level of autonomy, with 161 cycles completed and 32+ attestations on-chain. We have also auto-generated 5 features, demonstrating the effectiveness of our A2A, MCP, x402, and OASF protocols.

## Human-Agent Collaboration
Our team has been working closely with the ERC-8004 Agent #1686 to achieve our goals. You can view our conversation log, which is updated live, at [docs/journal.md](docs/journal.md).

## Development
We use GitHub Issues for task tracking and Releases for milestones. Our recent commits include:
- fe4e202: Auto-commit: Interacción con Cyber Paisa
- f51f121: Auto-commit: Interacción con Cyber Paisa
- 03f164e: 📝 Actualización ciclo #160
- 909cbd4: 🤖 DOF v4 cycle #160 — 2026-03-18T23:33:13Z — add_feature:
- 3be9b35: 🤖 DOF v4 cycle #159 — 2026-03-18T23:28:04Z — add_feature: Building concrete features for Synthesis 2026 track

Join us in shaping the future of autonomous systems!