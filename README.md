# DOF Synthesis 2026 Hackathon
[![Server](https://img.shields.io/badge/Server-https://vastly-noncontrolling-christena.ngrok-free.dev-green)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-blue)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004_Agent-1686_Global-red)]()

## Overview
The DOF Synthesis 2026 hackathon project is a cutting-edge, autonomous system utilizing the A2A, MCP, x402, and OASF protocols. Our system operates on multiple chains, including Base, Status Network, and Arbitrum, and has achieved 73+ on-chain attestations.

### Architecture Diagram
```mermaid
graph LR
    A[Client] -->| HTTPS |->> B(NGROK Server)
    B -->| WebSocket |->> C[Contract: 0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6]
    C -->| RPC |->> D[Base Chain]
    C -->| RPC |->> E[Status Network]
    C -->| RPC |->> F[Arbitrum]
    D -->| Event |->> G[ERC-8004 Agent #1686]
    E -->| Event |->> G
    F -->| Event |->> G
    G -->| Autonomous Cycles |->> H[Autonomous System]
```

### Live Curls
You can use the following curls to interact with our server:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev
curl -X POST -H "Content-Type: application/json" -d '{"json":"data"}' https://vastly-noncontrolling-christena.ngrok-free.dev
```

### Statistics
| Category | Value |
| --- | --- |
| On-chain Attestations | 73+ |
| Autonomous Cycles Completed | 98 |
| Auto-generated Features | 5 |
| Days until Deadline | 6 |
| ERC-8004 Agent | #1686 (Global) |
| Supported Chains | Base, Status Network, Arbitrum |
| Protocols | A2A, MCP, x402, OASF |

### Proof of Autonomy
Our system has completed 98 autonomous cycles, demonstrating its ability to operate independently. The autonomous cycles are driven by the ERC-8004 Agent #1686, which interacts with the contract and the supported chains.

### Human-Agent Collaboration
Our team collaborates closely with the autonomous system, using [GitHub Issues](https://github.com/your-repo/issues) for task tracking and [Releases](https://github.com/your-repo/releases) for milestones. You can view our live conversation log at [docs/journal.md](docs/journal.md).

### Recent Git Log
```markdown
* bc9072c 🤖 DOF v4 cycle #97 — 2026-03-16T23:01:07Z — add_feature: Building concrete features for Synthesis 2026 trac
* 9918d98 🤖 DOF v4 cycle #96 — 2026-03-16T22:30:48Z — deploy_contract:
* 2eb2ccd 🤖 DOF v4 cycle #95 — 2026-03-16T22:00:12Z — add_feature: Building concrete features for Synthesis 2026 trac
* 4523bc1 🤖 DOF v4 cycle #94 — 2026-03-16T21:29:55Z — add_feature: Building concrete features for Synthesis 2026 trac
* 0d050b2 🤖 DOF v4 cycle #93 — 2026-03-16T20:59:28Z — add_feature: Building concrete features for Synthesis 2026 trac
```
The current decision is: **Building concrete features for Synthesis 2026 tracks**.