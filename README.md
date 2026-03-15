# DOF Synthesis 2026 Hackathon
=====================================

[![Server Status](https://img.shields.io/website?down_color=red&down_message=Offline&up_color=green&up_message=Online&url=https://vastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract Address](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-9cf)](https://snowtrace.io/token/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004_Agent-%231686-9cf)](https://erc8004-agent-docs.io/)
[![Days Left](https://img.shields.io/badge/Days_until_deadline-7-yellow)]()

## Overview
DOF Synthesis is a cutting-edge project that utilizes A2A, MCP, x402, and OASF protocols to create a decentralized and autonomous system. Our project features:

* 1+ attestations on-chain
* 1 autonomous cycle completed
* 0 features auto-generated
* ERC-8004 Agent #1686 on the Avalanche network

## Statistics
| Category | Value |
| --- | --- |
| Attestations on-chain | 1+ |
| Autonomous cycles completed | 1 |
| Features auto-generated | 0 |
| Days until deadline | 7 |

## Architecture
```mermaid
graph LR
    A[Server] -->| REST API |/> B[Contract]
    B -->| Event Emission |/> C[ERC-8004 Agent]
    C -->| A2A + MCP + x402 + OASF |/> D[Autonomous System]
    D -->| On-chain Attestations |/> E[Blockchain]
```

## Live CURLs
You can interact with our server using the following CURL commands:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/
curl https://vastly-noncontrolling-christena.ngrok-free.dev/attestations
```

## Proof of Autonomy
Our system has completed 1 autonomous cycle, demonstrating its ability to operate independently.

## Human-Agent Collaboration
Our team collaborates with the ERC-8004 Agent through a conversational interface. You can view the live conversation log at [docs/conversation-log.md](docs/conversation-log.md).

## Project Management
We use [GitHub Issues](https://github.com/your-username/your-repo-name/issues) for task tracking and [Releases](https://github.com/your-username/your-repo-name/releases) for milestones.

## Git Log
```markdown
2fe249c 🤖 DOF v4 cycle #1 — 2026-03-15T03:13:01Z — none:
67d4074 🤖 DOF v4 cycle #1 — 2026-03-15T03:10:34Z — none:
99d2179 🤖 DOF v4 cycle #1 — 2026-03-15T03:06:01Z — none:
ff34e96 🤖 DOF v4 cycle #1 — 2026-03-15T03:01:53Z — none:
db9981c 🤖 DOF v4 cycle #1 — 2026-03-15T02:58:23Z — none:
```

Note: Replace `your-username` and `your-repo-name` with your actual GitHub username and repository name.