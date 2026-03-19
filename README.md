# DOF Synthesis 2026 Hackathon
[![Server Status](https://img.shields.io/website?down_message=Offline&label=Server%20Status&up_message=Online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract Address](https://img.shields.io/ethereum/mainnet/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6?label=Contract%20Address)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![Agent ID](https://img.shields.io/badge/Agent%20ID-%231686-blue)](https://erc8004.org/agent/1686)

## Overview
DOF Synthesis 2026 is an innovative hackathon project that leverages cutting-edge blockchain technology to create a decentralized, autonomous, and multi-chain system. Our project utilizes the A2A, MCP, x402, and OASF protocols to facilitate seamless interactions across three blockchain networks: Base, Status Network, and Arbitrum.

## Architecture
```mermaid
graph LR;
    A[Base Network] -->|Contract: 0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6|> B[DOF Synthesis];
    C[Status Network] -->|A2A Protocol|> B;
    D[Arbitrum] -->|x402 Protocol|> B;
    B -->|MCP Protocol|> E[Autonomous Cycles];
    B -->|OASF Protocol|> F[Attestations];
    E -->|Autonomous Decision-Making|> G[Human-Agent Collaboration];
    F -->|On-Chain Verification|> G;
```

## Key Statistics
| Category | Value |
| --- | --- |
| Autonomous Cycles | 169 |
| On-Chain Attestations | 31+ |
| Auto-Generated Features | 4 |
| Days until Deadline | 3 |

## Live System
To demonstrate the capabilities of our system, you can interact with our server using the following `curl` commands:
```bash
# Example: Get system status
curl https://vastly-noncontrolling-christena.ngrok-free.dev/status

# Example: Trigger autonomous cycle
curl -X POST https://vastly-noncontrolling-christena.ngrok-free.dev/cycle
```

## Proof of Autonomy
Our system has completed 169 autonomous cycles, with 31+ on-chain attestations. This demonstrates the ability of our system to operate independently and make decisions based on predefined protocols.

## Human-Agent Collaboration
Our project emphasizes the importance of human-agent collaboration. You can view our live conversation log at [docs/journal.md](docs/journal.md), which showcases the dynamic interaction between humans and our autonomous system.

## Development and Issue Tracking
We use [GitHub Issues](https://github.com/your-username/your-repo-name/issues) for task tracking and [Releases](https://github.com/your-username/your-repo-name/releases) for milestones. Our recent commit history is as follows:
* 9770524: DOF v4 cycle #168 — 2026-03-19T01:49:13Z — add_feature
* 07a92cd: DOF v4 cycle #167 — 2026-03-19T01:48:29Z — fix_bug
* 9569124: DOF v4 cycle #166 — 2026-03-19T01:47:13Z — deploy_contract
* 1b2602e: DOF v4 cycle #165 — 2026-03-19T01:46:15Z — deploy_contract
* 80934c4: DOF v4 cycle #164 — 2026-03-19T01:24:04Z — add_feature

Join us in shaping the future of autonomous systems!