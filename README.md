# DOF Synthesis 2026 Hackathon
[![Server](https://img.shields.io/badge/Server-https://vastly-noncontrolling-christena.ngrok-free.dev-brightgreen)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-blue)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004-Agent-1686-red)](https://erc8004.io/agent/1686)

## Overview
DOF Synthesis 2026 is a cutting-edge hackathon project that leverages A2A, MCP, x402, and OASF protocols to achieve unparalleled autonomy. Our project is built on a multi-chain architecture, utilizing Base, Status Network, and Arbitrum to ensure seamless interactions.

## Architecture
```mermaid
graph LR
    A[Client] -->|A2A|MCP
    MCP -->|x402|OASF
    OASF -->|ERC-8004|Agent
    Agent -->|Multi-Chain|Base
    Agent -->|Multi-Chain|Status Network
    Agent -->|Multi-Chain|Arbitrum
```

## Live Demos
You can interact with our project using the following live curls:
* `curl https://vastly-noncontrolling-christena.ngrok-free.dev/a2a`
* `curl https://vastly-noncontrolling-christena.ngrok-free.dev/mcp`
* `curl https://vastly-noncontrolling-christena.ngrok-free.dev/x402`
* `curl https://vastly-noncontrolling-christena.ngrok-free.dev/oasdf`

## Statistics
| Category | Value |
| --- | --- |
| Autonomous Cycles Completed | 6 |
| Features Auto-Generated | 1 |
| Attestations On-Chain | 2+ |
| Days Until Deadline | 7 |

## Proof of Autonomy
Our project has demonstrated unparalleled autonomy, completing 6 autonomous cycles and generating 1 feature automatically. We have also achieved 2+ attestations on-chain, ensuring the integrity and transparency of our system.

## Human-Agent Collaboration
Our team collaborates closely with the ERC-8004 Agent to ensure seamless interactions and optimal decision-making. You can view our conversation log live at [docs/conversation-log.md](docs/conversation-log.md).

## Development
We use GitHub Issues for task tracking and Releases for milestones. Our team is committed to delivering high-quality updates and features to maximize our score in Synthesis 2026.

## Current Decision
Our current decision is to focus on improving documentation and demos to maximize our score in Synthesis 2026.

## Git Log
* `8a55ec6`: DOF v4 cycle #6 — 2026-03-15T12:34:52Z — deploy_contract
* `175a141`: DOF v4 cycle #5 — 2026-03-15T12:30:16Z — add_feature
* `8adfea1`: DOF v4 cycle #4 — 2026-03-15T12:29:19Z — deploy_contract
* `cbda76e`: DOF v4 cycle #3 — 2026-03-15T12:25:45Z — add_feature
* `02890a6`: soul: v12.0 — 2026 research-backed memory + self-evolution + attack defense matrix

Join us in shaping the future of autonomy and collaboration. Together, we can create a more efficient and effective system that benefits everyone.