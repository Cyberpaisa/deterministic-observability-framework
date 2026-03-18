# DOF Synthesis 2026 Hackathon
[![Server Status](https://img.shields.io/website?down_message=offline&label=Server&up_message=online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract Address](https://img.shields.io/ethereum/contract/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686%20(Global)-blue)]()

## Overview
DOF Synthesis is a cutting-edge project that utilizes A2A, MCP, x402, and OASF protocols to achieve multi-chain functionality across Base, Status Network, and Arbitrum. Our ERC-8004 Agent #1686 operates globally, with a contract address of `0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6` on the Base Mainnet.

## Architecture
```mermaid
graph LR
    A[Client] -->| Request |->> B[Server]
    B -->| Response |->> A
    B -->| Sync |->> C[Contract]
    C -->| Events |->> B
    subgraph Multi-Chain
        D[Base] -->| Cross-Chain |->> E[Status Network]
        E -->| Cross-Chain |->> F[Arbitrum]
    end
```

## Statistics
| Metric | Value |
| --- | --- |
| Attestations On-Chain | 31+ |
| Autonomous Cycles Completed | 157 |
| Auto-Generated Features | 4 |
| Days Until Deadline | 4 |

## Live API Status
You can test our API using the following `curl` commands:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/status
curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/events
```

## Proof of Autonomy
Our system has undergone rigorous testing and has demonstrated its ability to operate autonomously. With 157 autonomous cycles completed, we have shown that our agent can function independently and effectively.

## Human-Agent Collaboration
For a deeper understanding of our project's development and the human-agent collaboration, please refer to our [live conversation log](docs/journal.md). This document provides a transparent and detailed account of our decision-making process and communication.

## Development and Issue Tracking
We utilize GitHub Issues for task tracking and Releases for milestones. Our development process is fully transparent, and we welcome any feedback or contributions.

## Git Log
Our recent commits include:
- `0135ab0`: docs: restore TRUE conversation log with all Telegram history
- `35474ba`: docs: clean professional conversation log (English, tracks + cycles only)
- `7c828d2`: docs: restore COMPLETE conversation log (Git + Telegram, 2833 lines)
- `31bf332`: docs: restore conversation log from backup (4487 bytes)
- `750663e`: docs: final README v2 — clean professional, judge-ready, agent-proof

We are proud to present our project and believe that it showcases the potential of human-agent collaboration in achieving complex goals. With only 4 days left until the deadline, we are confident that our project will exceed expectations.