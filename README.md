# DOF Synthesis 2026 Hackathon
[![Server Status](https://img.shields.io/website?down_message=Offline&up_message=Online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract Address](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-blue)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686-%23FF69B4)](https://erc8004.org/agent/1686)

## Overview
The DOF Synthesis 2026 hackathon project is a cutting-edge, autonomous system leveraging A2A, MCP, x402, and OASF protocols to facilitate seamless multi-chain interactions across Base, Status Network, and Arbitrum. Our system boasts an impressive 47+ on-chain attestations, with 72 autonomous cycles completed to date.

## Statistics
| Category | Value |
| --- | --- |
| On-chain Attestations | 47+ |
| Autonomous Cycles | 72 |
| Auto-generated Features | 5 |
| Days until Deadline | 6 |
| Contract Address | 0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6 |
| ERC-8004 Agent | #1686 (Global) |

## Architecture
```mermaid
graph LR
    A[Client] -->|A2A, MCP, x402, OASF|> B[DOF Synthesis 2026]
    B -->|Multi-chain|> C[Base]
    B -->|Multi-chain|> D[Status Network]
    B -->|Multi-chain|> E[Arbitrum]
    C -->|On-chain Attestations|> F[Blockchain]
    D -->|On-chain Attestations|> F
    E -->|On-chain Attestations|> F
```

## Live API Examples
You can test our API using the following `curl` commands:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/status
curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/attestations
```

## Proof of Autonomy
Our system has completed 72 autonomous cycles, with 5 features auto-generated to date. The following Git log entries demonstrate our project's autonomous nature:
```markdown
a302333 🤖 DOF v4 cycle #71 — 2026-03-16T09:52:56Z — add_feature: Building concrete features for Synthesis 2026 trac
1d37c5a 🤖 DOF v4 cycle #70 — 2026-03-16T09:22:41Z — add_feature: Building concrete features for Synthesis 2026 trac
abbf404 🤖 DOF v4 cycle #69 — 2026-03-16T08:52:25Z — add_feature: Building concrete features for Synthesis 2026 trac
13a2036 🤖 DOF v4 cycle #68 — 2026-03-16T08:22:11Z — deploy_contract:
440541a 🤖 DOF v4 cycle #67 — 2026-03-16T07:51:47Z — add_feature: Building concrete features for Synthesis 2026 trac
```

## Human-Agent Collaboration
Our team utilizes GitHub Issues for task tracking and Releases for milestones. The [Conversation Log](docs/journal.md) provides a live, detailed account of our project's progress and decision-making process.

## Getting Started
To learn more about our project, explore the following resources:
* [Server](https://vastly-noncontrolling-christena.ngrok-free.dev)
* [Contract Address](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
* [Conversation Log](docs/journal.md)

We look forward to your feedback and contributions!