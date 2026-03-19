# DOF Synthesis 2026 Hackathon
[![Server](https://img.shields.io/badge/Server-https://vastly-noncontrolling-christena.ngrok-free.dev-brightgreen)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-blue)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004_Agent-1686.Global-red)](https://erc8004.info/agent/1686)

## Overview
DOF Synthesis 2026 is a cutting-edge project that leverages A2A, MCP, x402, and OASF protocols to create a decentralized and autonomous system. Our project features a multi-chain architecture, currently supporting Base, Status Network, and Arbitrum.

## Architecture
```mermaid
graph LR
    A[Client] -->|Request|> B[Server]
    B -->|Processing|> C[Contract]
    C -->|Execution|> D[Blockchain]
    D -->|Response|> B
    B -->|Response|> A
    style B fill:#f9f,stroke:#333,stroke-width:4px
    style C fill:#ccc,stroke:#333,stroke-width:4px
```

## Live Curls
You can interact with our server using the following curls:
* `curl https://vastly-noncontrolling-christena.ngrok-free.dev`
* `curl -X POST https://vastly-noncontrolling-christena.ngrok-free.dev/data`

## Proof of Autonomy
Our system has demonstrated significant autonomy, with the following statistics:
| Metric | Value |
| --- | --- |
| Attestations on-chain | 31+ |
| Autonomous cycles completed | 164 |
| Features auto-generated | 3 |
| Days until deadline | 3 |

## Human-Agent Collaboration
Our team collaborates closely with the agent to ensure seamless integration and decision-making. You can view our conversation log [here](docs/journal.md).

## Task Tracking and Milestones
We use [GitHub Issues](https://github.com/your-repo/issues) for task tracking and [Releases](https://github.com/your-repo/releases) for milestone tracking.

## Current Decision
Our current decision is to build concrete features for Synthesis 2026 tracks.

## Recent Commits
* `28ba28f`: DOF v4 cycle #163 — 2026-03-19T01:03:53Z — add_feature
* `5f38d3e`: DOF v4 cycle #162 — 2026-03-19T00:33:38Z — add_feature
* `80e7d02`: DOF v4 cycle #161 — 2026-03-19T00:03:26Z — add_feature
* `fe4e202`: Auto-commit: Interacción con Cyber Paisa
* `f51f121`: Auto-commit: Interacción con Cyber Paisa

Note: Replace `your-repo` with your actual GitHub repository name.