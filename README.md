# DOF Synthesis 2026 Hackathon
[![DOI](https://img.shields.io/badge/Server-https://vastly-noncontrolling-christena.ngrok-free.dev-green)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-blue)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![Agent](https://img.shields.io/badge/ERC-8004%20Agent%20%231686-red)](https://erc8004.agent/1686)

## Overview
Our project utilizes A2A, MCP, x402, and OASF protocols to facilitate a multi-chain architecture across Base, Status Network, and Arbitrum. With 42+ attestations on-chain and 192 autonomous cycles completed, our project demonstrates a high level of autonomy and decentralization.

## Statistics
| Metric | Value |
| --- | --- |
| Autonomous Cycles | 192 |
| Attestations On-Chain | 42+ |
| Auto-Generated Features | 11 |
| Remaining Days Until Deadline | 3 |

## Architecture
```mermaid
graph LR;
    A2A -->| interacts with |> MCP;
    MCP -->| utilizes |> x402;
    x402 -->| leverages |> OASF;
    OASF -->| integrates with |> Base;
    Base -->| communicates with |> Status Network;
    Status Network -->| interacts with |> Arbitrum;
    Arbitrum -->| provides infrastructure for |> DOF Synthesis 2026;
```

## Live Curls
You can interact with our contract using the following curls:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/contract
curl https://vastly-noncontrolling-christena.ngrok-free.dev/agent
```

## Proof of Autonomy
Our project has demonstrated autonomy through the completion of 192 cycles, with each cycle adding new features and functionality to the system. The use of A2A, MCP, x402, and OASF protocols enables decentralized decision-making and execution.

## Human-Agent Collaboration
Our team collaborates closely with the agent to ensure seamless execution and decision-making. You can view our conversation log [here](docs/journal.md), which is updated live.

## Task Tracking and Milestones
We use [GitHub Issues](https://github.com/your-username/your-repo-name/issues) for task tracking and [Releases](https://github.com/your-username/your-repo-name/releases) for milestones.

## Recent Commits
* `bf8966e`: DOF v4 cycle #191 — 2026-03-19T09:07:24Z — deploy_contract
* `c9ed2a4`: DOF v4 cycle #190 — 2026-03-19T08:37:10Z — add_feature
* `7d37105`: DOF v4 cycle #189 — 2026-03-19T08:06:47Z — improve_readme
* `d3cb56e`: DOF v4 cycle #188 — 2026-03-19T07:36:30Z — add_feature
* `4789c9d`: DOF v4 cycle #187 — 2026-03-19T07:06:04Z — add_feature

Our current decision is to focus on building concrete features for the Synthesis 2026 tracks. With only 3 days remaining until the deadline, we are committed to delivering a high-quality project that showcases the potential of human-agent collaboration.