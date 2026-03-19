# DOF Synthesis 2026 Hackathon
[![Server Status](https://img.shields.io/website?down_message=Offline&up_message=Online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract Address](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-blue)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686-blue)]()
[![Multi-Chain](https://img.shields.io/badge/Multi--Chain-Base%2C%20Status%20Network%2C%20Arbitrum-blue)]()

## Overview
DOF Synthesis is a cutting-edge project that leverages A2A, MCP, x402, and OASF protocols to create a decentralized, autonomous system. Our project features a unique architecture, with a server hosted at [https://vastly-noncontrolling-christena.ngrok-free.dev](https://vastly-noncontrolling-christena.ngrok-free.dev) and a contract address of `0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6` on the Base Mainnet.

### Architecture
```mermaid
graph LR
    A[Server] -->|API|> B[Contract]
    B -->|Events|> C[Agent]
    C -->|Decisions|> D[Autonomous Cycles]
    D -->|Actions|> E[Multi-Chain]
    E -->|Attestations|> F[On-Chain Storage]
```

### Live Curls
You can interact with our server using the following curls:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/status
curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/decision
```

### Statistics
| Metric | Value |
| --- | --- |
| Autonomous Cycles Completed | 188 |
| Attestations On-Chain | 38+ |
| Features Auto-Generated | 10 |
| Days Until Deadline | 3 |

### Proof of Autonomy
Our system has demonstrated autonomy through the completion of 188 cycles, with 38+ attestations on-chain. The following git log entries demonstrate the autonomous nature of our system:
```markdown
4789c9d 🤖 DOF v4 cycle #187 — 2026-03-19T07:06:04Z — add_feature:
32b1420 🤖 DOF v4 cycle #186 — 2026-03-19T06:35:34Z — add_feature:
2271109 Vault Sync: Enigma Soul Backup 2026-03-19 01:20:32
81ff032 Vault Sync: Enigma Soul Backup 2026-03-19 01:17:36
5054d64 Vault Sync: Enigma Soul Backup 2026-03-19 01:06:37
```

### Human-Agent Collaboration
Our project features a unique collaboration between human developers and autonomous agents. You can view our conversation log, which is updated live, at [docs/journal.md](docs/journal.md).

### Task Tracking and Milestones
We use GitHub Issues for task tracking and Releases for milestones. You can view our current issues and releases on the [GitHub Issues](https://github.com/your-repo/issues) and [Releases](https://github.com/your-repo/releases) pages.

### Current Decision
Our current decision is to continue developing and refining our autonomous system, with a focus on improving its performance and reliability.