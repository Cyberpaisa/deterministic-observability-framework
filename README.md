# DOF Synthesis 2026 Hackathon
[![Server](https://img.shields.io/website?label=Server&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract](https://img.shields.io/ethereum/contract/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC-8004_Agent-1686-green)](https://docs.ethereum.org/erc-8004/)

## Overview
DOF Synthesis is a cutting-edge project leveraging A2A, MCP, x402, and OASF protocols to create a decentralized, autonomous, and multi-chain system. Our project utilizes the ERC-8004 Agent #1686 on the Global network and is deployed on multiple chains, including Base, Status Network, and Arbitrum.

## Architecture
```mermaid
graph LR
    A[Client] -->|Request|> B(NGROK Server)
    B -->|Forward|> C[Contract: 0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6]
    C -->|Execute|> D[Multi-Chain: Base, Status Network, Arbitrum]
    D -->|Attest|> E[On-Chain Attestations: 9+]
    E -->|Autonomous Cycles|> F[Completed Cycles: 14]
```

## Live Curls
You can test our server using the following curl commands:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev
curl -X POST https://vastly-noncontrolling-christena.ngrok-free.dev -H "Content-Type: application/json" -d '{"key": "value"}'
```

## Statistics
| Category | Value |
| --- | --- |
| Autonomous Cycles | 14 |
| On-Chain Attestations | 9+ |
| Multi-Chain Support | Base, Status Network, Arbitrum |
| Auto-Generated Features | 0 |
| Days until Deadline | 7 |

## Proof of Autonomy
Our system has completed 14 autonomous cycles, demonstrating its ability to operate independently. The contract address `0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6` on the Base Mainnet has been used to execute these cycles.

## Human-Agent Collaboration
Our team has been working closely with the ERC-8004 Agent #1686 to ensure seamless collaboration. You can view our conversation log [here](docs/conversation-log.md).

## Development and Issue Tracking
We use [GitHub Issues](https://github.com/user/repo/issues) for task tracking and [Releases](https://github.com/user/repo/releases) for milestones.

## Recent Commits
* `9b51629`: DOF v4 cycle #14 — 2026-03-15T16:31:08Z — none
* `58752a9`: DOF v4 cycle #13 — 2026-03-15T16:07:00Z — run_update
* `dbaeae5`: DOF v4 cycle #13 — 2026-03-15T16:01:00Z — none
* `61c87cf`: DOF v4 cycle #12 — 2026-03-15T15:36:25Z — deploy_contract
* `64ab209`: DOF v4 cycle #12 — 2026-03-15T15:30:38Z — none

Note: The current decision is still being evaluated.