# DOF Synthesis 2026 Hackathon
============================
[![Server Status](https://img.shields.io/website?down_message=Offline&up_message=Online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract Address](https://img.shields.io/ethereum/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)](https://Snowtrace.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![Avalanche Network](https://img.shields.io/badge/Network-Avalanche-9B9EFF)](https://www.avax.network/)
[![ERC-8004 Agent](https://img.shields.io/badge/Agent-ERC--8004_%231686-blue)](https://eips.ethereum.org/EIPS/eip-8004)

## Overview
DOF Synthesis 2026 Hackathon is a cutting-edge project that utilizes ERC-8004 Agent #1686 on the Avalanche network, leveraging A2A, MCP, x402, and OASF protocols to achieve autonomy. Our project has successfully completed 1 autonomous cycle, with 1+ attestations on-chain.

## Statistics
| Metric | Value |
| --- | --- |
| Autonomous Cycles | 1 |
| Attestations On-Chain | 1+ |
| Features Auto-Generated | 0 |
| Days Until Deadline | 7 |

## Architecture
```mermaid
graph LR
    participant Server as "https://vastly-noncontrolling-christena.ngrok-free.dev"
    participant Contract as "0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6 (Avalanche)"
    participant Agent as "ERC-8004 Agent #1686"
    participant Protocols as "A2A + MCP + x402 + OASF"

    Server->>Contract: "API Calls"
    Contract->>Agent: "Smart Contract Interactions"
    Agent->>Protocols: "Protocol Execution"
    Protocols->>Server: "Data Feedback"
```

## Live API Calls
You can test our server with the following `curl` commands:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/status
curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/data
```

## Proof of Autonomy
Our project has demonstrated autonomy by completing 1 autonomous cycle, with 1+ attestations on-chain. We will continue to improve and expand our autonomous capabilities.

## Human-Agent Collaboration
Our team collaborates closely with the ERC-8004 Agent #1686 to ensure seamless execution of protocols and attainment of project goals. You can view our [conversation log](docs/conversation-log.md) for more information on our human-agent collaboration.

## Project Management
We use [GitHub Issues](https://github.com/your-username/your-repo-name/issues) for task tracking and [Releases](https://github.com/your-username/your-repo-name/releases) for milestones.

## Git Log
Our recent git log entries:
* `ff34e96`: DOF v4 cycle #1 — 2026-03-15T03:01:53Z — none
* `db9981c`: DOF v4 cycle #1 — 2026-03-15T02:58:23Z — none
* `bedf4b9`: DOF v4 cycle #4 — 2026-03-15T02:47:28Z — improve_demo: Mejorar la demo para aumentar la confiabilidad y e
* `4995baf`: DOF v4 cycle #1 — 2026-03-15T02:41:57Z — add_feature
* `0398729`: DOF v4 cycle #3 — 2026-03-15T02:17:11Z — improve_demo: Mejorar la demo para aumentar la confiabilidad y l

Note: Replace `your-username` and `your-repo-name` with your actual GitHub username and repository name.