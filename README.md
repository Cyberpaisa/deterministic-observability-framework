# DOF Synthesis 2026 Hackathon
==========================

[![Server](https://img.shields.io/badge/Server-https://vastly-noncontrolling-christena.ngrok-free.dev-brightgreen)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-orange)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC-8004_Agent_%231686-ff69b4)](https://erc8004.io/agent/1686)

## Overview
DOF Synthesis 2026 is a cutting-edge project that utilizes the power of A2A + MCP + x402 + OASF protocols to create a decentralized, multi-chain ecosystem. Our project is built on top of the Base Mainnet, Status Network, and Arbitrum, with a strong focus on autonomy and decentralization.

## Architecture
```mermaid
graph LR
    A[User] -->|Interact|> B[Client]
    B -->|Request|> C[Server]
    C -->|Process|> D[Contract]
    D -->|Execute|> E[Blockchain]
    E -->|Verify|> F[On-Chain Attestations]
    F -->|Update|> C
```

## Live Curls
You can test our API using the following curl commands:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/
curl https://vastly-noncontrolling-christena.ngrok-free.dev/attestations
```

## Statistics
| Metric | Value |
| --- | --- |
| Autonomous Cycles Completed | 46 |
| On-Chain Attestations | 1+ |
| Features Auto-Generated | 0 |
| Days until Deadline | 7 |

## Proof of Autonomy
Our project has demonstrated significant autonomy, with 46 autonomous cycles completed. We have implemented a robust ERC-8004 Agent (#1686) that interacts with the blockchain to execute tasks and verify results.

## Human-Agent Collaboration
Our team has been working closely with our AI agent to build concrete features for the Synthesis 2026 tracks. You can view our conversation log [here](docs/journal.md) to see how we're collaborating to build a robust and decentralized ecosystem.

## Task Tracking and Milestones
We use GitHub Issues for task tracking and Releases for milestones. You can view our [issues](https://github.com/your-repo/issues) and [releases](https://github.com/your-repo/releases) to see how we're managing our project.

## Recent Updates
Our recent updates include:
* `c9352d5`: Added active defense protocol
* `f9bf59c`: Completed DOF v4 cycle #45
* `3d20aa3`: Completed DOF v4 cycle #44
* `7bda1c3`: Added ERC-8004 demo and feature discovery
* `1db2651`: Completed DOF v4 cycle #43

Our current decision is to focus on building concrete features for the Synthesis 2026 tracks. We're excited to see how our project will evolve and improve over the next 7 days!