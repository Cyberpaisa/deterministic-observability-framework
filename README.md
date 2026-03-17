# DOF Synthesis 2026 Hackathon
[![Server](https://img.shields.io/website?down_color=red&down_message=Offline&up_color=green&up_message=Online&url=https://vastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-blue)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-1686-yellow)](https://erc8004.io/agent/1686)

## Overview
DOF Synthesis 2026 is a cutting-edge hackathon project that leverages the power of A2A, MCP, x402, and OASF protocols to create a decentralized, multi-chain system. Our project features:

* Multi-chain support: Base, Status Network, Arbitrum
* 77+ on-chain attestations
* 102 autonomous cycles completed
* 5 auto-generated features

### Statistics
| Category | Value |
| --- | --- |
| On-chain Attestations | 77+ |
| Autonomous Cycles | 102 |
| Auto-generated Features | 5 |
| Days until Deadline | 5 |

### Architecture
```mermaid
graph LR
    A[Server] -->|HTTPS|> B[Contract]
    B -->|ERC-8004|> C[Agent #1686]
    C -->|A2A + MCP + x402 + OASF|> D[Multi-chain]
    D -->|Base|> E[Base Network]
    D -->|Status Network|> F[Status Network]
    D -->|Arbitrum|> G[Arbitrum Network]
```

### Live Demos
You can test our server using the following `curl` commands:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev
```
### Proof of Autonomy
Our project has completed 102 autonomous cycles, demonstrating its ability to operate independently. We have also auto-generated 5 features, showcasing the power of our system.

### Human-Agent Collaboration
Our project features a live [Conversation Log](docs/journal.md), which details our human-agent collaboration throughout the hackathon. This log provides valuable insights into our design decisions and problem-solving processes.

## Development
We use [GitHub Issues](https://github.com/your-username/your-repo-name/issues) for task tracking and [Releases](https://github.com/your-username/your-repo-name/releases) for milestones. Our project is constantly evolving, and we invite you to explore our [Git Log](https://github.com/your-username/your-repo-name/commits/main) to see our latest updates.

### Recent Commits
* `73d9acd`: docs: DOF Agent #1686 — professional README with 10 tracks, verified evidence, judge-ready
* `5beb0a1`: docs: professional README — clean, verified, judge-ready
* `3fa136e`: DOF v4 cycle #101 — 2026-03-17T01:03:09Z — add_feature: Building concrete features for Synthesis 2026 tracks
* `961a9de`: docs: complete README with all 10 tracks (6 functional + 4 conceptual)
* `8bc905a`: docs: add Vercel live demo link

## Current Decision
Our current focus is on building concrete features for the Synthesis 2026 tracks. We are committed to delivering a high-quality project that showcases the potential of decentralized, multi-chain systems.