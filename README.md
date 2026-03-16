# DOF Synthesis 2026 Hackathon
[![Server Status](https://img.shields.io/website?down_message=Offline&up_message=Online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-blue)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004_Agent-1686_(Global)-orange)]()

## Overview
DOF Synthesis 2026 is a cutting-edge hackathon project that leverages the power of A2A, MCP, x402, and OASF protocols to create a decentralized and autonomous system. Our project utilizes a multi-chain approach, with deployments on Base, Status Network, and Arbitrum.

## Architecture
```mermaid
graph LR;
    A[User] -->|Interact|> B[Server];
    B -->|API|> C[Contract];
    C -->|ERC-8004|> D[Agent];
    D -->|Autonomous Cycle|> E[Attestation];
    E -->|On-Chain|> F[Blockchain];
```
Our architecture is designed to provide a seamless and autonomous experience, with the user interacting with the server, which in turn communicates with the contract and agent.

## Live Curls
You can use the following curl commands to test our API:
```bash
curl -X GET https://vastly-noncontrolling-christena.ngrok-free.dev/api/attestations
curl -X POST https://vastly-noncontrolling-christena.ngrok-free.dev/api/attestations -H "Content-Type: application/json" -d '{"data": "Example data"}'
```
## Stats
| Metric | Value |
| --- | --- |
| Attestations on-chain | 39+ |
| Autonomous cycles completed | 64 |
| Features auto-generated | 5 |
| Days until deadline | 6 |

## Proof of Autonomy
Our system has demonstrated autonomy through the completion of 64 cycles, with 39+ attestations on-chain. This is a testament to the effectiveness of our ERC-8004 agent and the A2A, MCP, x402, and OASF protocols.

## Human-Agent Collaboration
Our project is built on the principles of human-agent collaboration. You can view our live conversation log at [docs/journal.md](docs/journal.md), which showcases the dynamic interaction between humans and our autonomous agent.

## Task Tracking and Milestones
We use [GitHub Issues](https://github.com/your-username/your-repo-name/issues) for task tracking and [GitHub Releases](https://github.com/your-username/your-repo-name/releases) for milestones.

## Recent Updates
Our recent updates include:
* **d37a2c2**: Added complete track traceability to conversation log
* **609ad18**: Fixed diagram syntax
* **4711c25**: Fixed README: Mermaid syntax and curl headers
* **da8b558**: Added Ampersend x402 integration concept for bounty
* **6174254**: Added feature: Building concrete features for Synthesis 2026 track

We look forward to showcasing our project to the AI judges and demonstrating the potential of human-agent collaboration in the context of A2A, MCP, x402, and OASF protocols.