# DOF Synthesis 2026 Hackathon
[![Server Status](https://img.shields.io/website?label=Server%20Status&up_message=online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract Address](https://img.shields.io/badge/Contract%20Address-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-orange)](https://snowtrace.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-1686-blue)]()

## Overview
DOF Synthesis is a cutting-edge project that leverages A2A, MCP, x402, and OASF protocols to create a robust and autonomous system. Our project utilizes a contract address on the Avalanche network and is powered by an ERC-8004 agent.

## Architecture
```mermaid
graph LR
    A[Client] -->|API Request|> B(Server)
    B -->|Contract Interaction|> C(Smart Contract)
    C -->|Autonomous Cycles|> D(ERC-8004 Agent)
    D -->|Attestations|> E(On-Chain Data)
```
Our system consists of a client, server, smart contract, ERC-8004 agent, and on-chain data storage. The client sends API requests to the server, which interacts with the smart contract to initiate autonomous cycles. The ERC-8004 agent generates attestations, which are stored on-chain.

## Live Demos
You can test our system using the following live curl commands:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/demo
```
Replace the URL with the actual server address.

## Statistics
| Metric | Value |
| --- | --- |
| Autonomous Cycles Completed | 1 |
| On-Chain Attestations | 1+ |
| Features Auto-Generated | 0 |
| Days until Deadline | 7 |

## Proof of Autonomy
Our system has demonstrated autonomy by completing 1 cycle without human intervention. We have also stored 1+ attestations on-chain, showcasing the system's ability to generate and store data autonomously.

## Human-Agent Collaboration
Our team collaborates with the ERC-8004 agent through a conversation log, which can be found [here](docs/conversation-log.md). This log provides insights into the decision-making process and ensures transparency in our collaboration.

## Task Tracking and Milestones
We use [GitHub Issues](https://github.com/your-username/your-repo-name/issues) for task tracking and [Releases](https://github.com/your-username/your-repo-name/releases) for milestones. This allows us to stay organized and focused on our goals.

## Git Log
Our recent git log is as follows:
```
bedf4b9 🤖 DOF v4 cycle #4 — 2026-03-15T02:47:28Z — improve_demo: Mejorar la demo para aumentar la confiabilidad y e
4995baf 🤖 DOF v4 cycle #1 — 2026-03-15T02:41:57Z — add_feature:
0398729 🤖 DOF v4 cycle #3 — 2026-03-15T02:17:11Z — improve_demo: Mejorar la demo para aumentar la confiabilidad y l
cf40df3 🤖 DOF v4 cycle #1 — 2026-03-15T02:11:54Z — fix_bug: Mejorar la estabilidad del servidor para poder ava
a4f3d2a 🤖 DOF v4 cycle #2 — 2026-03-15T01:49:04Z — add_feature: Crear el archivo trust_score.py para empezar a gen
```
Note: Replace `your-username` and `your-repo-name` with your actual GitHub username and repository name.