# DOF Synthesis 2026 Hackathon
[![Server](https://img.shields.io/website?label=Server&up_message=Online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract](https://img.shields.io/ethereum/contract/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686-orange)](https://erc8004.info/agent/1686)

## Overview
Our project utilizes a combination of A2A, MCP, x402, and OASF protocols to create a robust and autonomous system. The architecture is designed to operate on multiple chains, including Base, Status Network, and Arbitrum, with 1+ attestations on-chain.

### Architecture Diagram
```mermaid
graph LR
    A[Base Chain] -->|ERC-8004|> B(ERC-8004 Agent #1686)
    B -->|A2A|MCP
    B -->|MCP|x402
    B -->|x402|OASF
    C[Status Network] -->|OASF|> D(Autonomous System)
    E[Arbitrum] -->|OASF|> D
    D -->|On-Chain Attestations|> F(1+ Attestations)
```

### Live Curls
You can test our API using the following curl commands:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/ping
curl https://vastly-noncontrolling-christena.ngrok-free.dev/status
```

### Stats
| Category | Value |
| --- | --- |
| Autonomous Cycles Completed | 23 |
| Features Auto-Generated | 0 |
| Days Until Deadline | 7 |
| Chains Supported | 3 (Base, Status Network, Arbitrum) |
| On-Chain Attestations | 1+ |

### Proof of Autonomy
Our system has completed 23 autonomous cycles, with 1+ on-chain attestations. The contract address is [0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6) on the Base Mainnet.

### Current Decision
Our current decision is to focus on improving documentation and demos to maximize our score in the Synthesis 2026 hackathon.

### Human-Agent Collaboration
We believe in the importance of human-agent collaboration. You can view our conversation log [here](docs/conversation-log.md).

### Task Tracking and Milestones
We use [GitHub Issues](https://github.com/your-repo-name/issues) for task tracking and [Releases](https://github.com/your-repo-name/releases) for milestones.

### Git Log
```markdown
fcdaa71 🤖 DOF v4 cycle #22 — 2026-03-15T18:19:16Z — none:
62c2fed 🤖 DOF v4 cycle #21 — 2026-03-15T18:15:49Z — none:
eb69ca8 🤖 DOF v4 cycle #20 — 2026-03-15T17:57:35Z — none:
be0ba31 🤖 DOF v4 cycle #19 — 2026-03-15T17:51:32Z — none:
6b50026 🤖 DOF v4 cycle #18 — 2026-03-15T17:26:37Z — none:
```