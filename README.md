# DOF Synthesis 2026 Hackathon
[![Server Status](https://img.shields.io/website?down_color=red&down_message=Offline&up_color=green&up_message=Online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract Address](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-blue)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004_Agent-%231686-%23ff69b4)](https://github.com/erc8004/agent-registry)

## Overview
The DOF Synthesis 2026 hackathon project utilizes a combination of A2A, MCP, x402, and OASF protocols to create a decentralized, autonomous system. Our project is deployed on multiple chains, including Base, Status Network, and Arbitrum.

## Architecture
```mermaid
graph LR
    A[Client] -->|HTTPS|> B(NGROK Server)
    B -->|Web3|> C[Smart Contract]
    C -->|ERC-8004|> D[Agent #1686]
    D -->|A2A/MCP/x402/OASF|> E[Multi-Chain Network]
    E -->|Autonomous Cycles|> F[On-Chain Attestations]
```

## Live Data
You can view our server's live status and interact with it using the following `curl` commands:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev
curl -X POST -H "Content-Type: application/json" -d '{"json":"payload"}' https://vastly-noncontrolling-christena.ngrok-free.dev
```

## Statistics
| Metric | Value |
| --- | --- |
| Autonomous Cycles Completed | 115 |
| On-Chain Attestations | 37+ |
| Auto-Generated Features | 3 |
| Days until Deadline | 5 |
| Contract Address | 0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6 |
| ERC-8004 Agent | #1686 |

## Proof of Autonomy
Our system has completed 115 autonomous cycles, with 37+ on-chain attestations. This demonstrates the system's ability to operate independently and make decisions based on predefined protocols.

## Human-Agent Collaboration
Our team collaborates with the autonomous agent through a transparent and documented process. You can view our conversation log, including decisions and actions taken, at [docs/journal.md](docs/journal.md). This live document provides insight into the human-agent collaboration and the decision-making process.

## Development and Tracking
We use [GitHub Issues](https://github.com/DOF-Synthesis-2026/issues) for task tracking and [Releases](https://github.com/DOF-Synthesis-2026/releases) for milestones. Our recent commit history includes:
* `fa4c976`: DOF v4 cycle #114 — 2026-03-17T06:23:33Z — add_feature: Building concrete features for Synthesis 2026 trac
* `252520f`: DOF v4 cycle #113 — 2026-03-17T05:53:12Z — add_feature: Building concrete features for Synthesis 2026 trac
* `5214f67`: DOF v4 cycle #112 — 2026-03-17T05:22:35Z — add_feature: Building concrete features for Synthesis 2026 trac
* `eee92de`: DOF v4 cycle #111 — 2026-03-17T04:52:22Z — add_feature: Building concrete features for Synthesis 2026 trac
* `6c0758a`: DOF v4 cycle #110 — 2026-03-17T04:22:07Z — add_feature: Building concrete features for Synthesis 2026 trac

Our current decision is focused on building concrete features for Synthesis 2026 tracks.