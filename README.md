# DOF Synthesis 2026 Hackathon
[![Server Status](https://img.shields.io/website?down_message=offline&up_message=online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract Address](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-blue)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004_Agent-1686_Global-blue)]()

## Overview
DOF Synthesis is an innovative project that leverages A2A, MCP, x402, and OASF protocols to create a multi-chain ecosystem spanning Base, Status Network, and Arbitrum. Our ERC-8004 Agent #1686 (Global) has successfully completed 178 autonomous cycles, with 32+ attestations on-chain.

## Architecture
```mermaid
graph LR
    A[DOF Server] -->|HTTPS|> B[ngrok-free.dev]
    B -->|Webhooks|> C[Contract: 0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6]
    C -->|Ethereum|> D[Base Mainnet]
    D -->|Interchain|> E[Status Network]
    E -->|Interchain|> F[Arbitrum]
    F -->|x402|> G[OASF]
    G -->|MCP|> H[A2A]
    H -->|A2A|> A
```

## Live Curls
You can interact with our server using the following curls:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/
curl https://vastly-noncontrolling-christena.ngrok-free.dev/info
```

## Statistics
| Metric | Value |
| --- | --- |
| Autonomous Cycles | 178 |
| On-Chain Attestations | 32+ |
| Auto-Generated Features | 3 |
| Days until Deadline | 3 |

## Proof of Autonomy
Our agent has demonstrated significant autonomy, with 178 cycles completed without human intervention. The following commit history showcases the agent's ability to improve and add features:
```markdown
37d3766 🤖 DOF v4 cycle #180 — 2026-03-19T03:43:01Z — improve_readme
6958eb9 🤖 DOF v4 cycle #179 — 2026-03-19T03:32:56Z — add_feature
a41ca75 🤖 DOF v4 cycle #178 — 2026-03-19T03:25:03Z — add_feature
4bb6a41 🤖 DOF v4 cycle #177 — 2026-03-19T03:22:17Z — fix_bug
a4572b8 🤖 DOF v4 cycle #176 — 2026-03-19T03:21:06Z — add_feature
```

## Human-Agent Collaboration
Our team utilizes GitHub Issues for task tracking and Releases for milestones. For a detailed conversation log, please refer to [docs/journal.md](docs/journal.md).

## Contributing
We welcome contributions to our project. Please submit issues and pull requests through GitHub. Our project is constantly evolving, and we appreciate your help in making it better.

## Current Decision
As we approach the deadline, our focus is on refining and expanding the project's capabilities. With 3 days remaining, we are committed to delivering a robust and innovative solution.