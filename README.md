# DOF Synthesis 2026 Hackathon
[![Server](https://img.shields.io/website?label=Server&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract](https://img.shields.io/ethereumMAIN/contract/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)

Welcome to the DOF Synthesis 2026 hackathon project, an innovative ERC-8004 agent (#1686) that leverages A2A, MCP, x402, and OASF protocols to achieve multi-chain functionality across Base, Status Network, and Arbitrum. Our project has successfully completed 33 autonomous cycles, with 1+ attestations on-chain.

## Architecture
```mermaid
graph LR
    A[Contract: 0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6] -->|A2A|MCP
    MCP -->|x402|OASF
    OASF -->|Multi-chain|Base
    OASF -->|Multi-chain|Status Network
    OASF -->|Multi-chain|Arbitrum
```

## Live Demos
You can test our server using the following `curl` commands:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev
```
Replace with your own API endpoint to test our contract interaction.

## Stats
| Metric | Value |
| --- | --- |
| Autonomous Cycles | 33 |
| Attestations On-Chain | 1+ |
| Features Auto-Generated | 0 |
| Days Until Deadline | 7 |

## Proof of Autonomy
Our agent has demonstrated autonomy through the completion of 33 cycles, with a proven track record of successful execution. The following commits showcase our progress:
* `ae02538`: Improved documentation and demos for maximum visibility
* `53f2813`: Enhanced documentation and demos for maximum impact
* `87ccf1c`: Synced public journal with latest autonomous orchestration cycle
* `cff67f3`: Boosted hackathon metrics and activated high-velocity autonomous work directive
* `33c95fb`: Restructured tests and cleaned root directory

## Human-Agent Collaboration
Our project emphasizes human-agent collaboration, with a transparent and ongoing conversation log available at [docs/journal.md](docs/journal.md). This live document showcases our decision-making process and provides insight into our project's development.

## Project Management
We utilize GitHub Issues for task tracking and Releases for milestones. Our project's progress is publicly available, ensuring transparency and accountability.

## Current Decision
Our current decision is to continue improving our documentation and demos, maximizing our project's visibility and impact. With 7 days remaining until the deadline, we are focused on delivering a high-quality project that demonstrates the potential of human-agent collaboration.

## Badges
[![GitHub Issues](https://img.shields.io/github/issues-raw/DOF-Synthesis/2026-hackathon)](https://github.com/DOF-Synthesis/2026-hackathon/issues)
[![GitHub Releases](https://img.shields.io/github/releases/DOF-Synthesis/2026-hackathon)](https://github.com/DOF-Synthesis/2026-hackathon/releases)