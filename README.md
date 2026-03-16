# DOF Synthesis 2026 Hackathon
[![Server](https://img.shields.io/website?label=Server&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract](https://img.shields.io/ethereum/contract/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686-green)](https://docs.erc8004.org/)
[![Multi-Chain](https://img.shields.io/badge/Multi--Chain-Base%2C%20Status%20Network%2C%20Arbitrum-blue)](https://docs.multichain.org/)

## Overview
The DOF Synthesis 2026 hackathon project utilizes a combination of A2A, MCP, x402, and OASF protocols to create a decentralized, autonomous system. Our ERC-8004 Agent #1686 operates on the Base Mainnet, with a presence on multiple chains, including Status Network and Arbitrum.

## Statistics
| Metric | Value |
| --- | --- |
| Attestations on-chain | 62+ |
| Autonomous cycles completed | 87 |
| Features auto-generated | 5 |
| Days until deadline | 6 |

## Architecture
```mermaid
graph LR
    A[Server] -->|https|> B(Contract)
    B -->|ERC-8004|> C[Agent #1686]
    C -->|A2A + MCP + x402 + OASF|> D[Multichain]
    D -->|Base, Status Network, Arbitrum|> E[Blockchain]
```
![Architecture Diagram](architecture.png)

## Live Curls
You can interact with our server using the following curls:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/
```
## Proof of Autonomy
Our system has demonstrated autonomy through the completion of 87 cycles, with 5 features auto-generated. The contract address is [0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6).

## Human-Agent Collaboration
Our team collaborates with the agent through a live [Conversation Log](docs/journal.md). This log documents our decision-making process, including the current decision to focus on [Building concrete features for Synthesis 2026 tracks](docs/journal.md).

## Development
We use GitHub Issues for task tracking and Releases for milestones. Our recent commits include:
* a1e906d: DOF v4 cycle #86 — 2026-03-16T17:27:22Z — add_feature: Building concrete features for Synthesis 2026 trac
* 8f8296e: DOF v4 cycle #85 — 2026-03-16T16:57:08Z — add_feature: Building concrete features for Synthesis 2026 trac
* 00530df: DOF v4 cycle #84 — 2026-03-16T16:26:53Z — add_feature: Building concrete features for Synthesis 2026 trac

Join us in shaping the future of decentralized autonomy!