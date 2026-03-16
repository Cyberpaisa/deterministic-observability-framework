# DOF Synthesis 2026 Hackathon
[![Server](https://img.shields.io/website?label=Server&up_message=Online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-blue)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686-green)]()

## Overview
DOF Synthesis 2026 is a cutting-edge project that leverages A2A, MCP, x402, and OASF protocols to achieve autonomy and decentralization. Our project utilizes a multi-chain approach, currently deployed on Base, Status Network, and Arbitrum.

## Architecture
```mermaid
graph LR
    A[User] -->|Request|> B[Server]
    B -->|Contract|> C[Blockchain]
    C -->|Event|> D[Agent]
    D -->|Action|> E[Protocol]
    E -->|Response|> B
    B -->|Response|> A
```

## Live Curls
You can interact with our server using the following curls:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/
```

## Statistics
| Metric | Value |
| --- | --- |
| Autonomous Cycles | 57 |
| Attestations on-chain | 32+ |
| Auto-generated Features | 3 |
| Days until Deadline | 6 |

## Proof of Autonomy
Our project has demonstrated significant autonomy, with 57 autonomous cycles completed. We utilize a combination of A2A, MCP, x402, and OASF protocols to achieve decentralized decision-making.

## Human-Agent Collaboration
Our project emphasizes human-agent collaboration, with a live [conversation log](docs/journal.md) that documents our decision-making process. We encourage you to review our log to understand our thought process and decisions.

## Task Tracking and Milestones
We use [GitHub Issues](https://github.com/your-repo/issues) for task tracking and [Releases](https://github.com/your-repo/releases) for milestones. You can track our progress and contribute to our project by opening issues or pull requests.

## Contract and Agent Information
* Contract Address: 0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6 (Base Mainnet)
* ERC-8004 Agent #1686 (Global)

## Recent Git Log
```markdown
* 2e5b048 🧹 archive old conversation log to docs/ backup
* 6aa1a57 📝 update README with all hackathon required links
* 7587ad3 🤖 DOF v4 cycle #56 — 2026-03-16T02:18:51Z — add_feature: Building concrete features for Synthesis 2026 trac
* e25ad8f 🤖 DOF v4 cycle #55 — 2026-03-16T01:57:43Z — add_feature: Building concrete features for Synthesis 2026 trac
* 00d3506 🤖 DOF v4 cycle #54 — 2026-03-16T01:27:26Z — add_feature: Building concrete features for Synthesis 2026 trac
```
Current decision: Building concrete features for Synthesis 2026 tracks.