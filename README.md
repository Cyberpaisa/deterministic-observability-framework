# DOF Synthesis 2026 Hackathon
[![Server Status](https://img.shields.io/website?down_color=red&down_message=Offline&up_color=green&up_message=Online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract Address](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-9cf)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004_Agent-%231686-9cf)]()
[![Multi-chain Support](https://img.shields.io/badge/Multi--chain-Base,_Status_Network,_Arbitrum-9cf)]()

## Overview
The DOF Synthesis 2026 hackathon project is a cutting-edge, autonomous system leveraging A2A, MCP, x402, and OASF protocols. Our system operates on multiple chains, including Base, Status Network, and Arbitrum, with a deployed contract on the Base Mainnet. We utilize GitHub Issues for task tracking and Releases for milestones.

## Architecture
```mermaid
graph LR
    A[ERC-8004 Agent #1686] -->|A2A + MCP + x402 + OASF|> B[Multi-chain Network]
    B -->|Base, Status Network, Arbitrum|> C[Contract: 0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6]
    C -->|Autonomous Cycles|> D[Autonomy Module]
    D -->|42+ Attestations|> E[On-chain Data]
    E -->|5 Auto-generated Features|> F[Feature Module]
    F -->|66+ Cycles Completed|> G[Autonomous System]
```

## Live Stats
| Statistic | Value |
| --- | --- |
| Autonomous Cycles Completed | 67 |
| Auto-generated Features | 5 |
| On-chain Attestations | 42+ |
| Days until Deadline | 6 |
| Git Commits | 69a6dbf, bb7073b, 9d210a3, 5379dbb, d37a2c2 |

## Live API Endpoints
You can test our API endpoints using the following `curl` commands:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/healthcheck
curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/contract-info
```

## Proof of Autonomy
Our system has completed 67 autonomous cycles, with 42+ attestations on-chain. We have also auto-generated 5 features, demonstrating our system's capability for autonomous decision-making.

## Human-Agent Collaboration
Our team collaborates closely with the autonomous agent, tracking progress and decisions in our [live conversation log](docs/journal.md). This log provides transparency into our development process and showcases the human-agent collaboration that drives our project forward.

## Track Progress
To track our progress, visit our [Releases page](https://github.com/your-username/your-repo-name/releases) for milestones and our [Issues page](https://github.com/your-username/your-repo-name/issues) for task tracking.

Note: Replace `your-username` and `your-repo-name` with your actual GitHub username and repository name.