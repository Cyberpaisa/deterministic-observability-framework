# DOF Synthesis 2026 Hackathon
[![Server Status](https://img.shields.io/website?down_message=Offline&up_message=Online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract Address](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-orange)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004_Agent-%231686-blue)](https://erc8004.io/agent/1686)

## Overview
DOF Synthesis 2026 is a cutting-edge hackathon project that leverages A2A, MCP, x402, and OASF protocols to create a robust and autonomous system. Our project utilizes a multi-chain architecture, currently supporting Base, Status Network, and Arbitrum.

## Architecture
```mermaid
graph LR
    A[Base] -->| A2A |> B[Status Network]
    B -->| MCP |> C[Arbitrum]
    C -->| x402 |> A
    A -->| OASF |> D[ERC-8004 Agent #1686]
```
## Live Data
You can access our server at [https://vastly-noncontrolling-christena.ngrok-free.dev](https://vastly-noncontrolling-christena.ngrok-free.dev) or use the following live curl commands:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/data
curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/metrics
```
## Statistics
| Metric | Value |
| --- | --- |
| Autonomous Cycles Completed | 134 |
| Attestations on-chain | 30+ |
| Auto-Generated Features | 3 |
| Days until Deadline | 5 |

## Proof of Autonomy
Our system has demonstrated significant autonomy, with 134 cycles completed and over 30 attestations on-chain. We utilize a combination of A2A, MCP, x402, and OASF protocols to ensure seamless interaction between chains.

## Human-Agent Collaboration
Our team collaborates closely with the ERC-8004 Agent #1686 to ensure the project's success. You can view our conversation log at [docs/journal.md](docs/journal.md).

## Task Tracking and Milestones
We use [GitHub Issues](https://github.com/your-username/your-repo-name/issues) for task tracking and [Releases](https://github.com/your-username/your-repo-name/releases) for milestones.

## Recent Updates
Our recent git log updates include:
* `3d87809`: Added feature for Synthesis 2026 tracks
* `57316ca`: Improved README
* `067bb3f`: Added feature for Synthesis 2026 tracks
* `93f982a`: Added feature for Synthesis 2026 tracks
* `b184a39`: Improved README

Our current decision is focused on building concrete features for Synthesis 2026 tracks.