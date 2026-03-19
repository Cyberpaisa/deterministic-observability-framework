# DOF Synthesis 2026 Hackathon
==========================

[![Server](https://img.shields.io/website?label=Server&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract](https://img.shields.io/ethereum/contract/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![Agent](https://img.shields.io/badge/ERC--8004%20Agent-1686-blue)](https://erc8004.info/agents/1686)

## Overview
DOF Synthesis 2026 is a cutting-edge project leveraging AI and blockchain technology to achieve autonomy and decentralization. Our project utilizes a combination of A2A, MCP, x402, and OASF protocols to facilitate seamless interactions across multiple chains, including Base, Status Network, and Arbitrum.

## Architecture
```mermaid
graph LR
    A[Server] -->|HTTPS|> B[Contract]
    B -->|Web3|> C[Blockchain]
    C -->|Multi-Chain|> D[Base]
    C -->|Multi-Chain|> E[Status Network]
    C -->|Multi-Chain|> F[Arbitrum]
    D -->|A2A|> E
    E -->|MCP|> F
    F -->|x402|> D
    D -->|OASF|> C
```

## Live Curls
You can interact with our server using the following curls:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/
curl -X POST -H "Content-Type: application/json" -d '{"json":"data"}' https://vastly-noncontrolling-christena.ngrok-free.dev/
```

## Statistics
| Metric | Value |
| --- | --- |
| Attestations on-chain | 31+ |
| Autonomous cycles completed | 165 |
| Features auto-generated | 3 |
| Days until deadline | 3 |

## Proof of Autonomy
Our project has demonstrated autonomy through the completion of 165 cycles, with 31+ attestations on-chain. Our agent, ERC-8004 Agent #1686, has been interacting with the blockchain seamlessly, ensuring the integrity and decentralization of our system.

## Human-Agent Collaboration
Our team has been working closely with the AI agent, tracking progress and making decisions through our [Conversation Log](docs/journal.md). This live document provides insight into the development process and decision-making behind the project.

## Task Tracking and Milestones
We use [GitHub Issues](https://github.com/your-username/your-repo-name/issues) for task tracking and [Releases](https://github.com/your-username/your-repo-name/releases) for milestones. This allows us to stay organized and focused on our goals.

## Git Log
Recent commits:
* 80934c4 🤖 DOF v4 cycle #164 — 2026-03-19T01:24:04Z — add_feature: Building concrete features for Synthesis 2026 track
* 28ba28f 🤖 DOF v4 cycle #163 — 2026-03-19T01:03:53Z — add_feature:
* 5f38d3e 🤖 DOF v4 cycle #162 — 2026-03-19T00:33:38Z — add_feature:
* 80e7d02 🤖 DOF v4 cycle #161 — 2026-03-19T00:03:26Z — add_feature:
* fe4e202 Auto-commit: Interacción con Cyber Paisa

Note: Replace `your-username` and `your-repo-name` with your actual GitHub username and repository name.