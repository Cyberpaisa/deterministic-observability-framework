# DOF Synthesis 2026 Hackathon
[![Server](https://img.shields.io/website?label=Server&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract](https://img.shields.io/ethereum/mainnet-contracts-verified/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686%20(Global)-blue)]()
[![Multi-chain](https://img.shields.io/badge/Multi--chain-Base%2C%20Status%20Network%2C%20Arbitrum-blue)]()

## Overview
The DOF Synthesis 2026 hackathon project is built on top of the ERC-8004 protocol, utilizing the A2A, MCP, x402, and OASF protocols to achieve multi-chain functionality across Base, Status Network, and Arbitrum. Our project features a smart contract deployed on the Base Mainnet with the address `0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6`.

### Project Statistics
| Metric | Value |
| --- | --- |
| Autonomous Cycles Completed | 112 |
| Attestations On-chain | 34+ |
| Features Auto-generated | 3 |
| Days until Deadline | 5 |

### Architecture
```mermaid
graph LR
    A[Client] -->|HTTPS|> B(NGROK Server)
    B -->|Web3|> C[ERC-8004 Agent #1686]
    C -->|A2A + MCP + x402 + OASF|> D[Base Mainnet]
    D -->|Smart Contract|> E[Status Network]
    E -->|Smart Contract|> F[Arbitrum]
```

### Live CURLs
You can interact with our server using the following CURL commands:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev
```
### Current Decision
Our current decision is to focus on building concrete features for Synthesis 2026 tracks.

### Proof of Autonomy
Our project has completed 112 autonomous cycles, with 34+ attestations on-chain. We have also auto-generated 3 features.

### Human-Agent Collaboration
For more information on our human-agent collaboration, please refer to our [Conversation Log](docs/journal.md).

### Task Tracking and Milestones
We use [GitHub Issues](https://github.com/username/repository/issues) for task tracking and [Releases](https://github.com/username/repository/releases) for milestones.

### Git Log
Our recent git log entries are:
* `eee92de 🤖 DOF v4 cycle #111 — 2026-03-17T04:52:22Z — add_feature: Building concrete features for Synthesis 2026 trac`
* `6c0758a 🤖 DOF v4 cycle #110 — 2026-03-17T04:22:07Z — add_feature: Building concrete features for Synthesis 2026 trac`
* `a74da77 🤖 DOF v4 cycle #109 — 2026-03-17T03:51:46Z — add_feature: Building concrete features for Synthesis 2026 trac`
* `6268fe7 🤖 DOF v4 cycle #108 — 2026-03-17T03:48:53Z — deploy_contract:`
* `f9db85d 🤖 DOF v4 cycle #107 — 2026-03-17T03:37:52Z — add_feature: Building concrete features for Synthesis 2026 trac`