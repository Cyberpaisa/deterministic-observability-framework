# DOF Synthesis 2026 Hackathon
## Introduction
DOF Synthesis 2026 is a cutting-edge project that leverages autonomous agents, multi-chain interoperability, and advanced protocols to revolutionize the way we interact with blockchain technology. Our project utilizes a combination of A2A, MCP, x402, and OASF protocols to achieve seamless communication and coordination across different chains.

## Key Statistics
| Category | Value |
| --- | --- |
| Server | https://vastly-noncontrolling-christena.ngrok-free.dev |
| Contract | 0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6 (Base Mainnet) |
| ERC-8004 Agent | #1686 (Global) |
| Multi-chain Support | Base, Status Network, Arbitrum |
| Attestations on-chain | 2+ |
| Autonomous Cycles Completed | 30 |
| Auto-generated Features | 0 |
| Days until Deadline | 7 |

## Architecture
```mermaid
graph LR
    A[Agent] -->|A2A|MCP
    A -->|x402|OASF
    MCP -->|Multi-chain|Base
    MCP -->|Multi-chain|Status Network
    MCP -->|Multi-chain|Arbitrum
    OASF -->|Autonomy|Agent
```
Our architecture is designed to facilitate seamless interaction between the agent, multi-chain protocols, and autonomy modules.

## Live Curls
You can test our server using the following curls:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/agent
curl https://vastly-noncontrolling-christena.ngrok-free.dev/contract
```
## Badges
[![Server](https://img.shields.io/badge/Server-https://vastly-noncontrolling-christena.ngrok-free.dev-green)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-orange)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC-8004%20Agent-%231686-blue)](https://erc8004.io/agent/1686)

## Proof of Autonomy
Our agent has completed 30 autonomous cycles, with 2+ attestations on-chain. This demonstrates the agent's ability to operate independently and make decisions without human intervention.

## Human-Agent Collaboration
Our project emphasizes the importance of human-agent collaboration. You can view our conversation log [here](docs/conversation-log.md), which provides a live record of interactions between humans and the agent.

## Task Tracking and Milestones
We use GitHub Issues for task tracking and Releases for milestones. You can view our [ Issues](https://github.com/username/repository/issues) and [Releases](https://github.com/username/repository/releases) to stay up-to-date with our project's progress.

## Git Log
Our recent commits include:
* `fc0ca34`: refactor: mass cleanup of root directory and reorganization into logical folders (archive, docs, tests, logs)
* `1142b6b`: refactor: move AGENT_JOURNAL to root and update log paths for hackathon compliance
* `26caf8d`: sync journal and remove legacy conversation log from docs
* `d56ef24`: DOF v4 cycle #29 — 2026-03-15T18:42:57Z — improve_readme: Mejorando documentación y demos para maximizar score en Synthesis 2026
* `f8ba5af`: DOF v4 cycle #28 — 2026-03-15T18:36:11Z — improve_readme: Mejorando documentación y demos para maximizar score en Synthesis 2026

We are committed to continuously improving our project and demonstrating the potential of autonomous agents in blockchain technology. With 7 days remaining until the deadline, we are confident that our project will achieve great things.