# DOF Synthesis 2026 Hackathon
[![Server](https://img.shields.io/badge/Server-https://vastly-noncontrolling-christena.ngrok-free.dev-brightgreen)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-blue)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC-8004_Agent_%231686-9cf)](https://erc8004.link/agent/1686)

## Overview
DOF Synthesis is a cutting-edge project that leverages the power of A2A, MCP, x402, and OASF protocols to create a decentralized, autonomous system. Our project is built on top of a multi-chain architecture, utilizing Base, Status Network, and Arbitrum to ensure maximum scalability and security.

## Architecture
```mermaid
graph LR
    A[Base] -->|A2A|MCP
    B[Status Network] -->|x402|OASF
    C[Arbitrum] -->|MCP|A2A
    MCP -->|Autonomy|DOF Synthesis
    OASF -->|Security|DOF Synthesis
    style DOF Synthesis fill:#f9f,stroke:#333,stroke-width:4px
```

## Live Demos
You can test our project using the following live curls:
* `curl https://vastly-noncontrolling-christena.ngrok-free.dev/healthcheck`
* `curl https://vastly-noncontrolling-christena.ngrok-free.dev/autonomy`

## Stats
| Metric | Value |
| --- | --- |
| Autonomous Cycles Completed | 10 |
| Features Auto-Generated | 0 |
| Attestations On-Chain | 5+ |
| Days Until Deadline | 7 |

## Proof of Autonomy
Our project has demonstrated autonomy through the completion of 10 cycles, with 5+ attestations on-chain. We are proud to showcase our project's ability to operate independently, making decisions without human intervention.

## Human-Agent Collaboration
We believe in the importance of human-agent collaboration, which is why we maintain a live [conversation log](docs/conversation-log.md). This log provides transparency into our decision-making process and allows for seamless communication between humans and agents.

## Development
We use [GitHub Issues](https://github.com/your-repo/issues) for task tracking and [Releases](https://github.com/your-repo/releases) for milestones. Our project is constantly evolving, and we invite you to contribute to our repository.

## Recent Commits
* `f4f65f0`: DOF v4 cycle #9 — 2026-03-15T14:31:16Z — deploy_agent_service
* `e691a66`: DOF v4 cycle #10 — 2026-03-15T14:30:18Z — none
* `cca7f5d`: DOF v4 cycle #9 — 2026-03-15T14:05:41Z — add_feature
* `037d169`: DOF v4 cycle #8 — 2026-03-15T14:00:55Z — add_feature
* `4ba0185`: DOF v4 cycle #9 — 2026-03-15T14:00:09Z — none

Join us in shaping the future of autonomy and collaboration. Together, we can create a more decentralized, autonomous, and secure world.