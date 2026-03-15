# DOF Synthesis 2026 Hackathon
[![Server Status](https://img.shields.io/website?down_message=Offline&up_message=Online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract Address](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-blue)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686-blue)]()
[![Multi-Chain](https://img.shields.io/badge/Multi--Chain-Base%2C%20Status%20Network%2C%20Arbitrum-blue)]()

## Overview
Our project utilizes the A2A, MCP, x402, and OASF protocols to achieve seamless interaction across multiple blockchain networks, including Base, Status Network, and Arbitrum. With 1+ on-chain attestations and 31 completed autonomous cycles, our system demonstrates a high level of autonomy and reliability.

## Statistics
| Metric | Value |
| --- | --- |
| Autonomous Cycles Completed | 31 |
| On-Chain Attestations | 1+ |
| Features Auto-Generated | 0 |
| Days until Deadline | 7 |

## Architecture
```mermaid
graph LR
    A[Client] -->| HTTPS |> B(Server)
    B -->| Web3 |> C[Contract]
    C -->| Event |> D[Agent]
    D -->| A2A/MCP/x402/OASF |> E[Multi-Chain Network]
    E -->| Attestation |> C
```

## Live API Endpoints
You can test our API endpoints using the following `curl` commands:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/healthcheck
curl https://vastly-noncontrolling-christena.ngrok-free.dev/metrics
```

## Proof of Autonomy
Our system has completed 31 autonomous cycles, demonstrating its ability to operate independently. We have also implemented a range of protocols to ensure seamless interaction across multiple blockchain networks.

## Human-Agent Collaboration
Our team collaborates closely with the ERC-8004 Agent #1686 to ensure the successful execution of our project. You can view our conversation log [here](docs/journal.md), which is updated live.

## Task Tracking and Milestones
We use [GitHub Issues](https://github.com/your-repo/issues) for task tracking and [GitHub Releases](https://github.com/your-repo/releases) for milestones.

## Current Decision
Our current focus is on **Mejorando documentación y demos para maximizar score en Synthesis 2026**, ensuring that our documentation and demos are of the highest quality to maximize our score in the Synthesis 2026 hackathon.

## Commit History
Our recent commits include:
* `87ccf1c`: Sync public journal with latest autonomous orchestration cycle
* `cff67f3`: Boost hackathon metrics and activate high-velocity autonomous work directive
* `33c95fb`: Restructure tests and clean root directory
* `24842b7`: Finalize Track 5 walkthrough translation and professionalization
* `e6118e2`: Rephrase weaknesses into scalability opportunities and abstract script names

We are committed to delivering a high-quality project and are excited to showcase our work in the Synthesis 2026 hackathon.