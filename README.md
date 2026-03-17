# DOF Synthesis 2026 Hackathon
[![Server Status](https://img.shields.io/website?down_color=red&down_message=Offline&up_color=green&up_message=Online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract Address](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-blue)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686-orange)]()
[![Multi-Chain](https://img.shields.io/badge/Multi--Chain-Base%2C%20Status%20Network%2C%20Arbitrum-blue)]()

## Overview
The DOF Synthesis 2026 hackathon project is a cutting-edge, autonomous system leveraging A2A, MCP, x402, and OASF protocols. Our system operates on multiple chains, including Base, Status Network, and Arbitrum, with a deployed contract address of `0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6` on the Base Mainnet.

## Architecture
```mermaid
graph LR
    A[Client] -->| HTTPS |->> B(NGROK Server)
    B -->| Webhook |->> C[Contract]
    C -->| Event |->> D[ERC-8004 Agent #1686]
    D -->| Attestation |->> E[On-Chain Storage]
    E -->| Autonomy Cycle |->> F[Autonomous System]
    F -->| Decision |->> G[Feature Generation]
    G -->| Feature |->> H[Client]
```

## Live Curls
You can interact with our server using the following curl commands:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev
curl -X POST https://vastly-noncontrolling-christena.ngrok-free.dev/api/endpoint
```

## Proof of Autonomy
Our system has achieved the following milestones:
| Metric | Value |
| --- | --- |
| Autonomous Cycles Completed | 99 |
| Attestations On-Chain | 74+ |
| Features Auto-Generated | 5 |
| Days Until Deadline | 5 |

## Human-Agent Collaboration
Our system is designed to collaborate with humans through transparent decision-making processes. You can view our live conversation log at [docs/journal.md](docs/journal.md).

## Task Tracking and Milestones
We use [GitHub Issues](https://github.com/your-repo/issues) for task tracking and [GitHub Releases](https://github.com/your-repo/releases) for milestones.

## Git Log
Our recent commits include:
* `6b9ef13`: DOF v4 cycle #98 — 2026-03-16T23:31:23Z — add_feature: Building concrete features for Synthesis 2026 track
* `bc9072c`: DOF v4 cycle #97 — 2026-03-16T23:01:07Z — add_feature: Building concrete features for Synthesis 2026 track
* `9918d98`: DOF v4 cycle #96 — 2026-03-16T22:30:48Z — deploy_contract
* `2eb2ccd`: DOF v4 cycle #95 — 2026-03-16T22:00:12Z — add_feature: Building concrete features for Synthesis 2026 track
* `4523bc1`: DOF v4 cycle #94 — 2026-03-16T21:29:55Z — add_feature: Building concrete features for Synthesis 2026 track

Current decision: Building concrete features for Synthesis 2026 tracks.