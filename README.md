# DOF Synthesis 2026 Hackathon
[![Server](https://img.shields.io/website?down_message=Offline&label=Server&up_message=Online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-green)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004_Agent-%231686-blue)](https://erc8004.info/agent/1686)

## Introduction
DOF Synthesis 2026 is a cutting-edge hackathon project that leverages A2A, MCP, x402, and OASF protocols to create a decentralized, multi-chain ecosystem. Our project features a unique architecture that enables seamless interaction between various blockchain networks, including Base, Status Network, and Arbitrum.

## Architecture
```mermaid
graph LR
    participant Base as "Base Mainnet"
    participant Status as "Status Network"
    participant Arbitrum as "Arbitrum"
    participant Server as "Server"
    participant Contract as "Contract"

    Base -->| ERC-8004 |->> Contract
    Status -->| A2A |->> Contract
    Arbitrum -->| x402 |->> Contract
    Contract -->| OASF |->> Server
    Server -->| MCP |->> Base
    Server -->| MCP |->> Status
    Server -->| MCP |->> Arbitrum
```

## Live Curls
You can interact with our server using the following curls:
```bash
curl https://vastly-noncontolving-christena.ngrok-free.dev/ping
curl https://vastly-noncontolving-christena.ngrok-free.dev/attestations
```

## Stats
| Metric | Value |
| --- | --- |
| Autonomous Cycles | 58 |
| On-Chain Attestations | 33+ |
| Auto-Generated Features | 3 |
| Days until Deadline | 6 |

## Proof of Autonomy
Our project has demonstrated autonomy by completing 58 cycles, with 33+ attestations on-chain. Our system is capable of auto-generating features, with 3 features already created.

## Human-Agent Collaboration
Our team uses [GitHub Issues](https://github.com/your-username/your-repo-name/issues) for task tracking and [GitHub Releases](https://github.com/your-username/your-repo-name/releases) for milestones. You can view our live conversation log at [docs/journal.md](docs/journal.md).

## Contract Details
* Contract Address: 0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6 (Base Mainnet)
* ERC-8004 Agent: #1686 (Global)

## Next Steps
Our current decision is to focus on building concrete features for Synthesis 2026 tracks. We will continue to update our repository with the latest developments and milestones.

## Git Log
Our recent commits include:
* ebfc113: DOF v4 cycle #57 — 2026-03-16T02:49:10Z — add_feature: Building concrete features for Synthesis 2026 trac
* 2e5b048: archive old conversation log to docs/ backup
* 6aa1a57: update README with all hackathon required links
* 7587ad3: DOF v4 cycle #56 — 2026-03-16T02:18:51Z — add_feature: Building concrete features for Synthesis 2026 trac
* e25ad8f: DOF v4 cycle #55 — 2026-03-16T01:57:43Z — add_feature: Building concrete features for Synthesis 2026 trac

Note: Please replace `your-username` and `your-repo-name` with your actual GitHub username and repository name.