# DOF Synthesis 2026 Hackathon
[![Server Status](https://img.shields.io/website?label=Server%20Status&up_message=online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev&style=flat)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract Address](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-orange)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686-green)]()
[![Multi-Chain](https://img.shields.io/badge/Multi--Chain-Base%2C%20Status%20Network%2C%20Arbitrum-blue)]()

## Overview
The DOF Synthesis 2026 hackathon project is a cutting-edge, autonomous system leveraging A2A, MCP, x402, and OASF protocols. Our project utilizes a multi-chain approach, deployed on Base, Status Network, and Arbitrum, with a contract address of 0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6.

## Statistics
| Category | Value |
| --- | --- |
| Attestations on-chain | 36+ |
| Autonomous Cycles Completed | 114 |
| Auto-Generated Features | 3 |
| Days until Deadline | 5 |

## Architecture
```mermaid
graph LR;
    A2A -->|Interface|> MCP;
    MCP -->|Interface|> x402;
    x402 -->|Interface|> OASF;
    OASF -->|Interface|> Contract;
    Contract -->|Interface|> Multi-Chain;
    Multi-Chain -->|Interface|> Base;
    Multi-Chain -->|Interface|> Status Network;
    Multi-Chain -->|Interface|> Arbitrum;
```

## Live API Calls
You can test our API using the following `curl` commands:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/attestations
curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/autonomous-cycles
```

## Proof of Autonomy
Our system has completed 114 autonomous cycles, demonstrating its ability to operate independently. We have also achieved 36+ attestations on-chain, further solidifying our project's autonomous capabilities.

## Human-Agent Collaboration
Our team collaborates closely with our autonomous agent, tracking progress and making decisions through our [Conversation Log](docs/journal.md). This live document provides insight into our project's development and decision-making process.

## Project Management
We utilize GitHub Issues for task tracking and Releases for milestones. Our recent commits include:
* `252520f`: DOF v4 cycle #113 — 2026-03-17T05:53:12Z — add_feature: Building concrete features for Synthesis 2026 track
* `5214f67`: DOF v4 cycle #112 — 2026-03-17T05:22:35Z — add_feature: Building concrete features for Synthesis 2026 track
* `eee92de`: DOF v4 cycle #111 — 2026-03-17T04:52:22Z — add_feature: Building concrete features for Synthesis 2026 track
* `6c0758a`: DOF v4 cycle #110 — 2026-03-17T04:22:07Z — add_feature: Building concrete features for Synthesis 2026 track
* `a74da77`: DOF v4 cycle #109 — 2026-03-17T03:51:46Z — add_feature: Building concrete features for Synthesis 2026 track

Our current decision is focused on building concrete features for Synthesis 2026 tracks. With 5 days remaining until the deadline, our team is committed to delivering a high-quality project.