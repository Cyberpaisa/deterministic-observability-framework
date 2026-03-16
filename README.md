# DOF Synthesis 2026 Hackathon
[![Server Status](https://img.shields.io/website?down_message=Offline&up_message=Online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract Address](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-orange)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686-green)]()
[![Multi-Chain](https://img.shields.io/badge/Multi--Chain-Base%2C%20Status%20Network%2C%20Arbitrum-blue)]()

## Overview
DOF Synthesis 2026 is a cutting-edge hackathon project leveraging A2A, MCP, x402, and OASF protocols to create a decentralized and autonomous system. Our project features a server hosted at [https://vastly-noncontrolling-christena.ngrok-free.dev](https://vastly-noncontrolling-christena.ngrok-free.dev) and a contract deployed on the Base Mainnet at address `0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6`.

### Architecture
```mermaid
graph LR
    A[Client] -->|Request|> B[Server]
    B -->|Processing|> C[Contract]
    C -->|Execution|> D[Blockchain]
    D -->|Storage|> E[Data]
    E -->|Feedback|> A
```

### Live Curls
You can interact with our server using the following curls:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/
curl -X POST https://vastly-noncontrolling-christena.ngrok-free.dev/api/data
```

### Stats
| Metric | Value |
| --- | --- |
| Autonomous Cycles Completed | 71 |
| Attestations on Chain | 46+ |
| Features Auto-Generated | 5 |
| Days until Deadline | 6 |

### Proof of Autonomy
Our system has demonstrated autonomy through the completion of 71 cycles, with 46+ attestations on the blockchain. The most recent cycles are:
* `1d37c5a`: DOF v4 cycle #70 — 2026-03-16T09:22:41Z — add_feature: Building concrete features for Synthesis 2026 track
* `abbf404`: DOF v4 cycle #69 — 2026-03-16T08:52:25Z — add_feature: Building concrete features for Synthesis 2026 track
* `13a2036`: DOF v4 cycle #68 — 2026-03-16T08:22:11Z — deploy_contract
* `440541a`: DOF v4 cycle #67 — 2026-03-16T07:51:47Z — add_feature: Building concrete features for Synthesis 2026 track
* `69a6dbf`: DOF v4 cycle #66 — 2026-03-16T07:21:28Z — add_feature: Building concrete features for Synthesis 2026 track

The current decision is to continue building concrete features for Synthesis 2026 tracks.

### Human-Agent Collaboration
Our project utilizes a collaborative approach between humans and agents. You can view the live conversation log at [docs/journal.md](docs/journal.md).

## Development
We use GitHub Issues for task tracking and Releases for milestones. If you'd like to contribute, please submit a pull request or open an issue.

## Acknowledgments
This project would not be possible without the support of our team and the hackathon organizers. Thank you for your continued support.