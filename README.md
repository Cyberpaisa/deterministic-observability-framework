# DOF Synthesis 2026 Hackathon
[![Server Status](https://img.shields.io/website?down_color=red&down_message=Offline&up_color=green&up_message=Online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract Address](https://img.shields.io/ethereum/mainnet/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686-green)](https://erc8004.org/)

## Overview
DOF Synthesis is a cutting-edge project leveraging A2A, MCP, x402, and OASF protocols to create a decentralized, multi-chain platform. Our project utilizes the Base Mainnet, Status Network, and Arbitrum, ensuring a robust and scalable architecture.

## Architecture
```mermaid
graph LR
    A[Base Mainnet] -->|ERC-8004|> B(Contract)
    B -->|A2A + MCP + x402 + OASF|> C[Status Network]
    C -->|Multi-chain|> D[Arbitrum]
    D -->|Autonomous Cycles|> E[DOF Synthesis]
    E -->|Attestations|> F[On-chain Data]
```

## Live Demos
```bash
# Retrieve contract data
curl https://vastly-noncontrolling-christena.ngrok-free.dev/contract

# Interact with the contract
curl -X POST https://vastly-noncontrolling-christena.ngrok-free.dev/interact
```

## Statistics
| Category | Value |
| --- | --- |
| Attestations | 33+ |
| Autonomous Cycles | 162 |
| Auto-generated Features | 6 |
| Days until Deadline | 3 |

## Proof of Autonomy
Our project has successfully completed 162 autonomous cycles, demonstrating its ability to operate independently. The contract address `0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6` has been verified on the Base Mainnet, ensuring the integrity of our on-chain data.

## Human-Agent Collaboration
Our team collaborates closely with the DOF agent to ensure seamless execution of autonomous cycles. The [Conversation Log](docs/journal.md) provides a live record of our interactions, showcasing the efficiency of human-agent collaboration.

## Development and Tracking
We utilize [GitHub Issues](https://github.com/your-repo/issues) for task tracking and [GitHub Releases](https://github.com/your-repo/releases) for milestone management. Our commit history is available for review, with notable commits including:
* `80e7d02`: DOF v4 cycle #161
* `fe4e202`: Auto-commit: Interacción con Cyber Paisa
* `f51f121`: Auto-commit: Interacción con Cyber Paisa
* `03f164e`: Actualización ciclo #160
* `909cbd4`: DOF v4 cycle #160

## Current Decision
Our current decision is to continue refining the DOF Synthesis platform, focusing on optimizing autonomous cycles and expanding our multi-chain architecture.