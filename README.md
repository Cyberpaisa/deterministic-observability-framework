# DOF Synthesis 2026 Hackathon
=========================
[![Server](https://img.shields.io/website?down_message=offline&up_message=online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-yellow)](https://snowtrace.io/token/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686-blue)]()

## Overview
DOF Synthesis is a cutting-edge project that utilizes A2A, MCP, x402, and OASF protocols to achieve autonomy. Our project features a server hosted at [https://vastly-noncontrolling-christena.ngrok-free.dev](https://vastly-noncontrolling-christena.ngrok-free.dev) and a contract deployed on the Avalanche network at `0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6`.

## Architecture
```mermaid
graph LR
    A[Server] -->|API|> B[Contract]
    B -->|Events|> C[Agent]
    C -->|Actions|> D[Protocols]
    D -->|Data|> E[On-Chain Storage]
    E -->|Attestations|> F[Autonomous Cycles]
```

## Statistics
| Metric | Value |
| --- | --- |
| Attestations on-chain | 1+ |
| Autonomous cycles completed | 1 |
| Features auto-generated | 0 |
| Days until deadline | 7 |

## Live Curls
You can interact with our server using the following curls:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/status
curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/data
```

## Proof of Autonomy
Our project has achieved autonomy through the completion of 1 autonomous cycle. We use a combination of A2A, MCP, x402, and OASF protocols to enable autonomous decision-making.

## Human-Agent Collaboration
Our team collaborates with the agent through a conversation log, which can be found at [docs/conversation-log.md](docs/conversation-log.md). This log provides a transparent and live record of our interactions with the agent.

## Task Tracking and Milestones
We use [GitHub Issues](https://github.com/your-repo/issues) for task tracking and [Releases](https://github.com/your-repo/releases) for milestones.

## Git Log
Our recent commits include:
* `c09edf9`: Sync Track Trust/Pay contracts, append Slither audits & setup LLM telegram fallback
* `45aa2d5`: DOF v4 cycle #2 — 2026-03-15T04:15:56Z — improve_readme
* `ba8aad3`: DOF v4 cycle #1 — 2026-03-15T03:44:22Z — improve_readme: Mejorando documentación y demos para maximizar sco
* `735cbf7`: soul: v11.0 — Web3 Security Lab + Juan context + concrete objectives
* `b530425`: feat: Web3 Security Lab — Kali for Web3 + AI agent integration

Note: Replace `your-repo` with your actual repository name.