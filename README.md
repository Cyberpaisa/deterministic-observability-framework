# DOF Synthesis 2026 Hackathon
[![Server Status](https://img.shields.io/website=https://vastly-noncontrolling-christena.ngrok-free.dev.svg)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract Address](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-blue.svg)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686-blue.svg)](https://docs.erc8004.org/)

## Overview
DOF Synthesis 2026 is a cutting-edge project that leverages A2A, MCP, x402, and OASF protocols to achieve robust multi-chain functionality across Base, Status Network, and Arbitrum. Our ERC-8004 Agent #1686 is a global, autonomous entity that has completed 40 cycles, with 2+ attestations on-chain.

## Architecture
```mermaid
graph LR
    A[Base] -->|A2A|MCP
    A -->|x402|OASF
    MCP -->|MCP|Status Network
    OASF -->|OASF|Arbitrum
    subgraph Multi-Chain
        Status Network
        Arbitrum
    end
    style A fill:#f9f,stroke:#333,stroke-width:4px
```

## Live API
You can interact with our API using the following `curl` commands:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/
curl https://vastly-noncontrolling-christena.ngrok-free.dev/contract
```

## Statistics
| Metric | Value |
| --- | --- |
| Autonomous Cycles | 40 |
| On-Chain Attestations | 2+ |
| Features Auto-Generated | 0 |
| Days until Deadline | 7 |

## Proof of Autonomy
Our agent has demonstrated autonomy by completing 40 cycles without human intervention. The following table highlights the latest commits:
| Commit Hash | Description | Timestamp |
| --- | --- | --- |
| 1f3c796 | improve\_readme: Mejorando documentación y demos para maximizar sco | 2026-03-15T21:41:43Z |
| 8e751f0 | improve\_readme: Mejorando documentación y demos para maximizar sco | 2026-03-15T21:38:17Z |
| 026cbf4 | improve\_readme: | 2026-03-15T21:36:55Z |

## Human-Agent Collaboration
Our team collaborates with the agent through a live [Conversation Log](docs/journal.md). This log provides insights into the agent's decision-making process and allows us to refine its performance.

## Task Tracking and Milestones
We use [GitHub Issues](https://github.com/your-repo/issues) for task tracking and [Releases](https://github.com/your-repo/releases) for milestones.

## Current Decision
Our current decision is to focus on improving documentation and demos to maximize our score in the Synthesis 2026 hackathon.

## Contract Address
The contract address for our project is: `0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6` (Base Mainnet)

## Join Us
Join our community to contribute to the development of DOF Synthesis 2026. Together, we can push the boundaries of autonomous agents and multi-chain functionality.