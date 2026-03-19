# DOF Synthesis 2026 Hackathon
[![Server Status](https://img.shields.io/website?down_message=Offline&up_message=Online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract Address](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-blue)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686-green)]()
[![Multi-Chain](https://img.shields.io/badge/Multi--Chain-Base%2C%20Status%20Network%2C%20Arbitrum-yellow)]()

## Overview
DOF Synthesis 2026 is a cutting-edge hackathon project that leverages A2A, MCP, x402, and OASF protocols to create a decentralized, autonomous system. Our project features a multi-chain architecture, with deployments on Base, Status Network, and Arbitrum.

## Architecture
```mermaid
graph LR
    A[Client] -->| HTTPS |> B(NGROK Server)
    B -->| Web3 |> C[Contract: 0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6]
    C -->| ERC-8004 |> D[Agent #1686]
    D -->| A2A + MCP + x402 + OASF |> E[Autonomous System]
    E -->| Multi-Chain |> F[Base]
    E -->| Multi-Chain |> G[Status Network]
    E -->| Multi-Chain |> H[Arbitrum]
```

## Live Demo
You can interact with our system using the following `curl` commands:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/
curl -X POST -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"eth_call","params":[{"to":"0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6","data":"0x..."}],"id":1}' https://vastly-noncontrolling-christena.ngrok-free.dev/
```

## Statistics
| Metric | Value |
| --- | --- |
| Attestations on-chain | 46+ |
| Autonomous cycles completed | 196 |
| Auto-generated features | 13 |
| Days until deadline | 3 |

## Proof of Autonomy
Our system has demonstrated autonomy by completing 196 cycles without human intervention. The following Git log entries showcase the autonomous updates:
```markdown
f9f3f04 🤖 DOF v4 cycle #195 — 2026-03-19T11:08:26Z — deploy_contract:
0a4c68e 🤖 DOF v4 cycle #194 — 2026-03-19T10:38:08Z — add_feature:
9bc2d95 🤖 DOF v4 cycle #193 — 2026-03-19T10:07:51Z — improve_readme:
79d424e 🤖 DOF v4 cycle #192 — 2026-03-19T09:37:36Z — add_feature: Building concrete features for Synthesis 2026 trac
bf8966e 🤖 DOF v4 cycle #191 — 2026-03-19T09:07:24Z — deploy_contract:
```

## Human-Agent Collaboration
Our project features a unique collaboration between humans and agents. You can view the live conversation log at [docs/journal.md](docs/journal.md).

## Task Tracking and Milestones
We use [GitHub Issues](https://github.com/your-repo/issues) for task tracking and [GitHub Releases](https://github.com/your-repo/releases) for milestones.

## Current Decision
Our current decision is to continue improving the autonomy of our system, with a focus on increasing the number of auto-generated features and attestations on-chain.

Note: Replace `your-repo` with your actual GitHub repository name.