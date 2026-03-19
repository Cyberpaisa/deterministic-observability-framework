# DOF Synthesis 2026 Hackathon
[![Server Status](https://img.shields.io/website?down_message=Offline&up_message=Online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract Address](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-blue)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686-green)]()
[![Multi-Chain](https://img.shields.io/badge/Multi--Chain-Base%2C%20Status%20Network%2C%20Arbitrum-yellow)]()

## Overview
DOF Synthesis is a cutting-edge project that leverages A2A, MCP, x402, and OASF protocols to create a decentralized, autonomous system. Our project features a multi-chain architecture, currently deployed on Base, Status Network, and Arbitrum.

## Architecture
```mermaid
graph LR
    A[Client] -->| HTTPS |> B(Server)
    B -->| Web3 |> C[Contract]
    C -->| ERC-8004 |> D[Agent #1686]
    D -->| A2A + MCP + x402 + OASF |> E[Multi-Chain Network]
    E -->| Base, Status Network, Arbitrum |> F[On-Chain Attestations]
```

## Live Curls
You can interact with our server using the following curls:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/
curl -X POST -H "Content-Type: application/json" -d '{"json":"data"}' https://vastly-noncontrolling-christena.ngrok-free.dev/
```

## Statistics
| Metric | Value |
| --- | --- |
| Autonomous Cycles Completed | 179 |
| On-Chain Attestations | 32+ |
| Auto-Generated Features | 4 |
| Days until Deadline | 3 |

## Proof of Autonomy
Our system has demonstrated autonomy by completing 179 cycles without human intervention. The contract address `0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6` on the Base Mainnet has been verified to be functional and interacting with the ERC-8004 Agent #1686.

## Human-Agent Collaboration
Our team collaborates with the agent through a transparent and open process. You can view our conversation log live at [docs/journal.md](docs/journal.md).

## Development
We use GitHub Issues for task tracking and Releases for milestones. Our recent commits include:
* `dc9df2a`: DOF v4 cycle #179 — add feature
* `6170721`: DOF v4 cycle #178 — deploy contract
* `37d3766`: DOF v4 cycle #180 — improve README
* `6958eb9`: DOF v4 cycle #179 — add feature
* `a41ca75`: DOF v4 cycle #178 — add feature

## Current Decision
Our current decision is to continue improving the system's autonomy and features. We are committed to delivering a high-quality project within the remaining 3 days.

## Contributing
We welcome contributions and feedback from the community. Please submit any issues or pull requests through GitHub.