# DOF Synthesis 2026 Hackathon
[![Server Status](https://img.shields.io/website?label=Server&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract Address](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-orange)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686-blue)](https://docs.erc8004.org/agents/1686)

## Overview
Our project utilizes a multi-chain approach, spanning Base, Status Network, and Arbitrum, to leverage the strengths of each ecosystem. We have implemented a comprehensive suite of protocols, including A2A, MCP, x402, and OASF, to ensure seamless interactions and optimal performance.

## Architecture
```mermaid
graph LR
    A[Client] -->| HTTPS |->> B(NGROK Server)
    B -->| Webhook |->> C[Contract: 0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6]
    C -->| Event |->> D[DOF Agent #1686]
    D -->| Autonomy |->> E[MCP + x402 + OASF]
    E -->| Execution |->> F[Base, Status Network, Arbitrum]
```

## Live CURLs
You can interact with our server using the following CURL commands:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev
curl -X POST https://vastly-noncontrolling-christena.ngrok-free.dev/webhook
```

## Statistics
| Metric | Value |
| --- | --- |
| Attestations on-chain | 30+ |
| Autonomous cycles completed | 137 |
| Auto-generated features | 3 |
| Days until deadline | 5 |
| Protocols implemented | A2A, MCP, x402, OASF |

## Proof of Autonomy
Our DOF Agent #1686 has demonstrated autonomy by completing 137 cycles, generating 3 features, and executing a range of protocols. The agent's decision-making process is transparent and recorded in our [journal](docs/journal.md).

## Human-Agent Collaboration
Our team has been working closely with the DOF Agent #1686 to ensure seamless execution and decision-making. You can track our progress and conversations with the agent in our [live journal](docs/journal.md).

## Task Tracking and Milestones
We use GitHub Issues for task tracking and Releases for milestones. You can view our current issues and releases on our [GitHub page](https://github.com/your-repo).

## Recent Commits
* `9873cdc` fix: deduplicate README + soul v19.0 README protection rule
* `fd86bed` docs: add all 10 tracks with live demos and prizes — DOF Agent #1686
* `f93b43a` DOF v4 cycle #136 — 2026-03-17T19:26:05Z — add_feature: Building concrete features for Synthesis 2026 track
* `abc20c1` DOF v4 cycle #135 — 2026-03-17T18:55:46Z — add_feature: Building concrete features for Synthesis 2026 track
* `5e8f258` DOF v4 cycle #134 — 2026-03-17T18:25:33Z — add_feature: Building concrete features for Synthesis 2026 track

Our current decision is focused on **Building concrete features for Synthesis 2026 tracks**. We are committed to delivering a high-quality project and are excited to showcase our work to the judges.