# DOF Synthesis 2026 Hackathon
[![Server Status](https://img.shields.io/website?label=Server&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract Address](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-orange)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686-blue)](https://erc8004.io/agent/1686)

## Overview
The DOF Synthesis 2026 hackathon project is a cutting-edge implementation of autonomous systems, leveraging A2A, MCP, x402, and OASF protocols. Our project utilizes a multi-chain approach, with deployments on Base, Status Network, and Arbitrum. We have achieved significant milestones, including:

| Metric | Value |
| --- | --- |
| Attestations On-Chain | 38+ |
| Autonomous Cycles Completed | 116 |
| Auto-Generated Features | 3 |
| Days until Deadline | 5 |

## Architecture
Our system architecture is designed for autonomy and scalability:
```mermaid
graph LR
    A[Contract: 0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6] -->|ERC-8004|> B(ERC-8004 Agent #1686)
    B -->|A2A + MCP + x402 + OASF|> C(Multi-Chain: Base, Status Network, Arbitrum)
    C -->|Autonomous Cycles|> D(116 Cycles Completed)
    D -->|Auto-Generated Features|> E(3 Features)
```
## Live Curls
You can interact with our server using the following live curls:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/
```
## Proof of Autonomy
Our system has demonstrated autonomy through the completion of 116 cycles, with 38+ attestations on-chain. We utilize a combination of A2A, MCP, x402, and OASF protocols to ensure secure and efficient autonomous operation.

## Human-Agent Collaboration
Our team collaborates closely with the agent to ensure effective decision-making and feature development. You can view our conversation log, updated live, at [docs/journal.md](docs/journal.md).

## Development and Tracking
We use GitHub Issues for task tracking and Releases for milestones. Our recent commit history is as follows:
```markdown
* e90dff3 🤖 DOF v4 cycle #115 — 2026-03-17T06:53:51Z — add_feature: Building concrete features for Synthesis 2026 trac
* fa4c976 🤖 DOF v4 cycle #114 — 2026-03-17T06:23:33Z — add_feature: Building concrete features for Synthesis 2026 trac
* 252520f 🤖 DOF v4 cycle #113 — 2026-03-17T05:53:12Z — add_feature: Building concrete features for Synthesis 2026 trac
* 5214f67 🤖 DOF v4 cycle #112 — 2026-03-17T05:22:35Z — add_feature: Building concrete features for Synthesis 2026 trac
* eee92de 🤖 DOF v4 cycle #111 — 2026-03-17T04:52:22Z — add_feature: Building concrete features for Synthesis 2026 trac
```
Our current decision is focused on building concrete features for Synthesis 2026 tracks. We look forward to continuing to push the boundaries of autonomous systems in the remaining 5 days before the deadline.