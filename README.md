# DOF Synthesis 2026 Hackathon
[![Server](https://img.shields.io/website?label=Server&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract](https://img.shields.io/ethereum/mainnet/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686-blue)](https://erc8004.org/)
[![Protocols](https://img.shields.io/badge/Protocols-A2A%2B%20MCP%2B%20x402%2B%20OASF-blue)](https://docs Protocols.md)
[![Multi-chain](https://img.shields.io/badge/Multi--chain-Base%2C%20Status%20Network%2C%20Arbitrum-blue)](https://docs/Multi-chain.md)

## Overview
The DOF Synthesis 2026 hackathon project is a cutting-edge application of decentralized technologies, featuring a server hosted at [https://vastly-noncontrolling-christena.ngrok-free.dev](https://vastly-noncontrolling-christena.ngrok-free.dev) and an ERC-8004 Agent #1686 on the Base Mainnet. Our contract address is [0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6).

### Statistics
| Metric | Value |
| --- | --- |
| Attestations on-chain | 61+ |
| Autonomous cycles completed | 86 |
| Features auto-generated | 5 |
| Days until deadline | 6 |

### Architecture
```mermaid
graph LR
    A[Server] -->|HTTPS|> B[Contract]
    B -->|ERC-8004|> C[Agent #1686]
    C -->|A2A + MCP + x402 + OASF|> D[Multi-chain]
    D -->|Base, Status Network, Arbitrum|> E[Blockchain]
```
![Architecture Diagram](docs/architecture.png)

### Live CURLs
You can test our API using the following CURL commands:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/endpoint
```
### Proof of Autonomy
Our project demonstrates autonomy through the following features:
* 86 autonomous cycles completed
* 5 features auto-generated
* 61+ attestations on-chain

### Human-Agent Collaboration
Our team collaborates with the agent through a live conversation log, available at [docs/journal.md](docs/journal.md). This document provides a transparent and up-to-date record of our decision-making process and communication with the agent.

### Task Tracking and Milestones
We use [GitHub Issues](https://github.com/DOF-Synthesis-2026/DOF-Synthesis-2026/issues) for task tracking and [GitHub Releases](https://github.com/DOF-Synthesis-2026/DOF-Synthesis-2026/releases) for milestones.

### Current Decision
Our current decision is to focus on building concrete features for Synthesis 2026 tracks, as reflected in our recent Git log:
```markdown
8f8296e 🤖 DOF v4 cycle #85 — 2026-03-16T16:57:08Z — add_feature: Building concrete features for Synthesis 2026 trac
00530df 🤖 DOF v4 cycle #84 — 2026-03-16T16:26:53Z — add_feature: Building concrete features for Synthesis 2026 trac
91f9372 📝 add architecture diagram image to README
62a64d7 📝 fix README: add badges and close mermaid diagram
7db080c 📝 update README with complete judge evidence package
```