# DOF Synthesis 2026 Hackathon
[![Server](https://img.shields.io/website?down_color=red&down_message=Offline&up_color=green&up_message=Online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-blue)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686%20%28Global%29-blue)]()

## Overview
DOF Synthesis 2026 is a cutting-edge project that utilizes A2A, MCP, x402, and OASF protocols to facilitate a seamless multi-chain experience across Base, Status Network, and Arbitrum. Our project boasts an impressive array of features, including:

* **3+ on-chain attestations**
* **52 autonomous cycles completed**
* **ERC-8004 Agent #1686 (Global)**
* **Multi-chain support**: Base, Status Network, Arbitrum

## Architecture
```mermaid
graph LR
    A[Client] -->| HTTPS |->> B(NGROK Server)
    B -->| Webhook |->> C[Contract: 0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6]
    C -->| Event |->> D[ERC-8004 Agent #1686]
    D -->| Autonomous Cycle |->> E[MCP + x402 + OASF Protocols]
    E -->| A2A Protocol |->> F[Status Network, Arbitrum, Base]
    F -->| Multi-chain |->> G[On-chain Attestations]
    G -->| Proof of Autonomy |->> H[DOF Synthesis 2026]
```

## Live Curls
You can test our server using the following curl commands:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev
curl -X POST https://vastly-noncontrolling-christena.ngrok-free.dev/webhook
```

## Proof of Autonomy
Our project has demonstrated impressive autonomous capabilities, with:
| Statistic | Value |
| --- | --- |
| Autonomous Cycles Completed | 52 |
| On-chain Attestations | 3+ |
| Features Auto-Generated | 0 |
| Days until Deadline | 6 |

## Human-Agent Collaboration
Our team utilizes a collaborative approach, with human and agent working together seamlessly. You can view our live conversation log [here](docs/journal.md).

## Task Tracking and Milestones
We use [GitHub Issues](https://github.com/your-repo/issues) for task tracking and [Releases](https://github.com/your-repo/releases) for milestones.

## Git Log
Our recent git log:
* `f068f8b` : DOF v4 cycle #51 — 2026-03-15T23:56:36Z — add_feature: Building concrete features for Synthesis 2026 trac
* `3800707` : DOF v4 cycle #50 — 2026-03-15T23:26:21Z — add_feature: Building concrete features for Synthesis 2026 trac
* `a0db737` : DOF v4 cycle #49 — 2026-03-15T23:23:51Z — add_feature: Building concrete features for Synthesis 2026 trac
* `6ea54d0` : DOF v4 cycle #48 — 2026-03-15T23:15:44Z — add_feature: Building concrete features for Synthesis 2026 trac
* `e26cfc8` : DOF v4 cycle #47 — 2026-03-15T23:05:44Z — add_feature: Building concrete features for Synthesis 2026 trac

Current decision: **Building concrete features for Synthesis 2026 tracks**