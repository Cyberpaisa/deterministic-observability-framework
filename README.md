# DOF Synthesis 2026 Hackathon
[![Server Status](https://img.shields.io/website?down_message=offline&label=Server%20Status&up_message=online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract Address](https://img.shields.io/badge/Contract%20Address-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-orange)](https://explorer.base.org/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686-blue)](https://erc8004.org/agents/1686)

## Overview
DOF Synthesis 2026 is a cutting-edge hackathon project that leverages the power of A2A, MCP, x402, and OASF protocols to create a decentralized, multi-chain framework. Our solution utilizes the Base Mainnet, Status Network, and Arbitrum, with a total of 46+ on-chain attestations and 127 autonomous cycles completed.

### Statistics
| Category | Value |
| --- | --- |
| Attestations | 46+ |
| Autonomous Cycles | 127 |
| Auto-Generated Features | 4 |
| Days until Deadline | 5 |

## Architecture
```mermaid
graph LR
    participant Base Mainnet as "Base Mainnet"
    participant Status Network as "Status Network"
    participant Arbitrum as "Arbitrum"
    participant Server as "Server"
    participant Contract as "Contract (0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)"

    Base Mainnet--->>Server
    Status Network--->>Server
    Arbitrum--->>Server
    Server--->>Contract
```

## Live Curls
You can interact with our server using the following curled commands:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/healthcheck
curl https://vastly-noncontrolling-christena.ngrok-free.dev/metrics
```

## Proof of Autonomy
Our project has completed 127 autonomous cycles, with 4 features auto-generated. We utilize the ERC-8004 Agent #1686 to ensure the autonomy of our system.

## Human-Agent Collaboration
Our team collaborates closely with the AI agent to ensure seamless integration and decision-making. You can view our live conversation log at [docs/journal.md](docs/journal.md).

## Task Tracking and Milestones
We use GitHub Issues for task tracking and Releases for milestones. You can view our issues and releases at:
* [Issues](https://github.com/your-repository/issues)
* [Releases](https://github.com/your-repository/releases)

## Git Log
Our recent commits include:
* `c8ee168`: DOF v4 cycle #126 — 2026-03-17T14:06:33Z — deploy_contract
* `9aea1fa`: DOF v4 cycle #125 — 2026-03-17T13:05:58Z — none
* `f6bab73`: DOF v4 cycle #124 — 2026-03-17T12:31:00Z — add_feature: Building concrete features for Synthesis 2026 track
* `4cfbf9e`: DOF v4 cycle #123 — 2026-03-17T10:57:21Z — add_feature: Building concrete features for Synthesis 2026 track
* `6c02807`: DOF v4 cycle #122 — 2026-03-17T10:26:36Z — add_feature: Building concrete features for Synthesis 2026 track

Current decision: Building concrete features for Synthesis 2026 tracks.

We are excited to showcase our project and demonstrate the potential of human-agent collaboration in the development of decentralized, autonomous systems.