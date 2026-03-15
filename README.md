# DOF Synthesis 2026 Hackathon
[![Server Status](https://img.shields.io/website?down_message=Offline&label=Server%20Status&up_message=Online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract Address](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-orange)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686-blue)](https://erc8004.org/agents/1686)

## Overview
The DOF Synthesis 2026 hackathon project is a cutting-edge, autonomous system utilizing A2A, MCP, x402, and OASF protocols. Our system operates on multiple blockchain networks, including Base, Status Network, and Arbitrum.

### Key Statistics
| Metric | Value |
| --- | --- |
| Autonomous Cycles Completed | 34 |
| Features Auto-Generated | 1 |
| Attestations On-Chain | 1+ |
| Multi-Chain Networks | 3 (Base, Status Network, Arbitrum) |
| Days until Deadline | 7 |

### Architecture
```mermaid
graph LR;
    A2A -->| MCP |--> x402;
    x402 -->| OASF |--> Contract;
    Contract -->| ERC-8004 |--> Agent;
    Agent -->| Autonomous |--> Cycles;
```

### Live API Examples
You can test our API using the following `curl` commands:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/status
curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/metrics
```

### Proof of Autonomy
Our system has demonstrated autonomy by completing 34 cycles, generating 1 feature, and obtaining 1+ on-chain attestations.

### Human-Agent Collaboration
Our team collaborates with the autonomous agent through a live [conversation log](docs/journal.md). This allows us to track the agent's decisions and provide input when necessary.

### Task Tracking and Milestones
We use [GitHub Issues](https://github.com/your-repo/issues) for task tracking and [GitHub Releases](https://github.com/your-repo/releases) for milestones.

### Latest Commits
* `c10c99b` - DOF v4 cycle #33 — 2026-03-15T20:01:49Z — improve_readme
* `ae02538` - DOF v4 cycle #32 — 2026-03-15T19:37:14Z — improve_readme: Mejorando documentación y demos para maximizar sco
* `53f2813` - DOF v4 cycle #31 — 2026-03-15T19:32:43Z — improve_readme: Mejorando documentación y demos para maximizar sco

We welcome your feedback and look forward to continuing to push the boundaries of autonomous systems.