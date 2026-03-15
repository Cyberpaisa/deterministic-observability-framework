# DOF Synthesis 2026 Hackathon
[![Server Status](https://img.shields.io/website?down_message=offline&up_message=online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract Address](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-orange)](https://snowtrace.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686-blue)]()

## Overview
The DOF Synthesis 2026 hackathon project utilizes a combination of A2A, MCP, x402, and OASF protocols to achieve autonomy. Our ERC-8004 Agent #1686 is deployed on the Avalanche network, with a contract address of 0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6.

## Architecture
The architecture of our project is as follows:
```mermaid
graph LR
    participant Server as "https://vastly-noncontrolling-christena.ngrok-free.dev"
    participant Contract as "0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6"
    participant Agent as "ERC-8004 Agent #1686"
    Server-->|HTTPS|>Contract
    Contract-->|Smart Contract|>Agent
    Agent-->|Autonomous Decisions|>Server
```

## Live Curls
You can interact with our server using the following curls:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev
```

## Statistics
| Metric | Value |
| --- | --- |
| Autonomous Cycles Completed | 1 |
| Attestations on-chain | 1+ |
| Features Auto-Generated | 0 |
| Days until Deadline | 7 |

## Proof of Autonomy
Our project has completed 1 autonomous cycle, with 1+ attestations on-chain. This demonstrates the ability of our ERC-8004 Agent #1686 to make decisions autonomously.

## Human-Agent Collaboration
Our team uses [GitHub Issues](https://github.com/your-repo/issues) for task tracking and [Releases](https://github.com/your-repo/releases) for milestones. You can view our [Conversation Log](docs/conversation-log.md) to see the collaboration between humans and our autonomous agent.

## Latest Git Log
```markdown
* 0376a2e 🤖 DOF v4 cycle #1 — 2026-03-15T03:14:59Z — none:
* 2fe249c 🤖 DOF v4 cycle #1 — 2026-03-15T03:13:01Z — none:
* 67d4074 🤖 DOF v4 cycle #1 — 2026-03-15T03:10:34Z — none:
* 99d2179 🤖 DOF v4 cycle #1 — 2026-03-15T03:06:01Z — none:
* ff34e96 🤖 DOF v4 cycle #1 — 2026-03-15T03:01:53Z — none:
```
Current decision: 

Note: Please replace `your-repo` with your actual GitHub repository name.