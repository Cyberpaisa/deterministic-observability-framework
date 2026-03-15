# DOF Synthesis 2026 Hackathon
[![Server](https://img.shields.io/website?label=Server&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract](https://img.shields.io/ethereum/contract/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)](https://snowtrace.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686-blue)]()

## Overview
DOF Synthesis is a cutting-edge project that leverages A2A, MCP, x402, and OASF protocols to achieve autonomy and interoperability. Our ERC-8004 Agent #1686 is deployed on the Avalanche network, with a contract address of `0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6`.

## Architecture
```mermaid
graph LR
    A[Server] -->|HTTPS|> B[Contract]
    B -->|Web3|> C[ERC-8004 Agent]
    C -->|A2A|> D[Autonomous Cycle]
    D -->|MCP|> E[Data Processing]
    E -->|x402|> F[Data Storage]
    F -->|OASF|> G[Data Visualization]
```

## Live Curls
You can interact with our server using the following curls:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/
curl -X POST https://vastly-noncontrolling-christena.ngrok-free.dev/api/data
```

## Proof of Autonomy
We have achieved the following milestones:
| Metric | Value |
| --- | --- |
| Autonomous Cycles | 10 |
| Attestations on-chain | 10+ |
| Features Auto-Generated | 4 |
| Days until Deadline | 7 |

## Human-Agent Collaboration
Our human and agent collaborators work together to ensure the success of this project. You can view our live conversation log [here](docs/conversation-log.md).

## Task Tracking and Milestones
We use [GitHub Issues](https://github.com/your-repo/issues) for task tracking and [Releases](https://github.com/your-repo/releases) for milestones.

## Git Log
Our recent git log entries are:
* `f4dce6b`: DOF v4 cycle #9 — 2026-03-15T08:44:19Z — add_feature
* `42d2332`: DOF v4 cycle #8 — 2026-03-15T08:14:08Z — add_feature
* `3151de2`: DOF v4 cycle #7 — 2026-03-15T07:43:54Z — add_feature
* `139b62b`: DOF v4 cycle #6 — 2026-03-15T07:13:44Z — fix_bug
* `1d8905b`: DOF v4 cycle #5 — 2026-03-15T06:43:33Z — improve_readme

## Current Decision
Our current decision is to continue developing and refining our autonomous cycles, with a focus on improving the accuracy and efficiency of our data processing and visualization pipelines.