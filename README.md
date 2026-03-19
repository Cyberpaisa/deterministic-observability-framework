# DOF Synthesis 2026 Hackathon
[![Server Status](https://img.shields.io/website?down_message=Offline&up_message=Online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract Address](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-blue)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686-blue)](https://erc8004.org/)

## Overview
DOF Synthesis is a cutting-edge project that leverages A2A, MCP, x402, and OASF protocols to create a decentralized, autonomous system. Our project features a multi-chain architecture, currently deployed on Base, Status Network, and Arbitrum.

### Architecture
```mermaid
graph LR
    A[Client] -->|HTTPS|> B(NGROK Server)
    B -->|HTTPS|> C[Contract: 0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6]
    C -->|JSON-RPC|> D[ERC-8004 Agent #1686]
    D -->|gRPC|> E[Autonomous System]
    E -->|gRPC|> D
    D -->|JSON-RPC|> C
    C -->|HTTPS|> B
    B -->|HTTPS|> A
```

### Live API Calls
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/status
curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/attestations
```

### Statistics
| Metric | Value |
| --- | --- |
| Attestations on-chain | 34+ |
| Autonomous cycles completed | 163 |
| Auto-generated features | 7 |
| Remaining days until deadline | 3 |
| Contract address | 0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6 |

## Proof of Autonomy
Our system has completed 163 autonomous cycles, with 34+ attestations on-chain. This demonstrates the ability of our system to operate independently and effectively.

## Human-Agent Collaboration
Our team collaborates closely with the autonomous system, tracking progress and making decisions through our [Conversation Log](docs/journal.md). This live document provides insight into our project's development and decision-making process.

## Task Tracking and Milestones
We use [GitHub Issues](https://github.com/your-repo/issues) for task tracking and [Releases](https://github.com/your-repo/releases) for milestones. This allows us to stay organized and focused on our project's goals.

## Recent Commits
* `5f38d3e`: DOF v4 cycle #162 — 2026-03-19T00:33:38Z — add_feature
* `80e7d02`: DOF v4 cycle #161 — 2026-03-19T00:03:26Z — add_feature
* `fe4e202`: Auto-commit: Interacción con Cyber Paisa
* `f51f121`: Auto-commit: Interacción con Cyber Paisa
* `03f164e`: Actualización ciclo #160

Note: Replace `your-repo` with your actual GitHub repository name.