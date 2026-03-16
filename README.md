# DOF Synthesis 2026 Hackathon
[![Server](https://img.shields.io/website?down_message=Offline&label=Server&up_message=Online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract](https://img.shields.io/ethereum/mainnet/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-1686-blue)]()
[![Multi-Chain](https://img.shields.io/badge/Multi--Chain-Base%2C%20Status%20Network%2C%20Arbitrum-blue)]()
[![Protocols](https://img.shields.io/badge/Protocols-A2A%2C%20MCP%2C%20x402%2C%20OASF-blue)]()

## Architecture
```mermaid
graph LR
    A[User] -->| Request |> B(Server)
    B -->| Response |> A
    B -->| Contract Interaction |> C(Smart Contract)
    C -->| Event Emission |> B
    B -->| Multi-Chain Interaction |> D(Base)
    B -->| Multi-Chain Interaction |> E(Status Network)
    B -->| Multi-Chain Interaction |> F(Arbitrum)
```

## Live Curls
You can interact with our server using the following curls:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev
curl https://vastly-noncontrolling-christena.ngrok-free.dev/contract
curl https://vastly-noncontrolling-christena.ngrok-free.dev/multi-chain
```

## Proof of Autonomy
We have achieved the following milestones:
| Metric | Value |
| --- | --- |
| Autonomous Cycles Completed | 92 |
| Attestations on-Chain | 67+ |
| Auto-Generated Features | 5 |
| Days until Deadline | 6 |

## Human-Agent Collaboration
Our conversation log is available [here](docs/journal.md). We use GitHub Issues for task tracking and Releases for milestones.

## Current Status
Our current decision is to focus on **Building concrete features for Synthesis 2026 tracks**. Our recent commits include:
* 4ca5a17: DOF v4 cycle #91 — 2026-03-16T19:58:43Z — add_feature: Building concrete features for Synthesis 2026 trac
* daf60be: DOF v4 cycle #90 — 2026-03-16T19:28:24Z — add_feature: Building concrete features for Synthesis 2026 trac
* f8952a7: DOF v4 cycle #89 — 2026-03-16T18:58:07Z — add_feature: Building concrete features for Synthesis 2026 trac
* e4c6c19: DOF v4 cycle #88 — 2026-03-16T18:27:51Z — add_feature: Building concrete features for Synthesis 2026 trac
* f5f3cfa: DOF v4 cycle #87 — 2026-03-16T17:57:36Z — add_feature: Building concrete features for Synthesis 2026 trac

We are committed to delivering a high-quality project. Stay tuned for updates!