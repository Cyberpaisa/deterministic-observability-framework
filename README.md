# DOF Synthesis 2026 Hackathon
[![Server](https://img.shields.io/website?down_color=red&down_message=Offline&up_color=green&up_message=Online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract](https://img.shields.io/ethereum/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686%20%28Global%29-brightgreen)](https://erc8004.io/agent/1686)

## Overview
DOF Synthesis is a cutting-edge decentralized application that leverages A2A, MCP, x402, and OASF protocols to facilitate seamless interactions across multiple blockchain networks, including Base, Status Network, and Arbitrum. Our solution utilizes ERC-8004 Agent #1686 (Global) to ensure secure and efficient communication.

### Architecture
```mermaid
graph LR
    A[Client] -->|A2A, MCP, x402, OASF|> B[Server]
    B -->|Multi-chain|> C[Base]
    B -->|Multi-chain|> D[Status Network]
    B -->|Multi-chain|> E[Arbitrum]
    C -->|ERC-8004|> F[Agent #1686]
    D -->|ERC-8004|> F
    E -->|ERC-8004|> F
```

### Live CURLs
You can interact with our server using the following CURL commands:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/status
curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/attestations
```

### Statistics
| Metric | Value |
| --- | --- |
| Autonomous Cycles | 171 |
| On-chain Attestations | 31+ |
| Auto-generated Features | 3 |
| Days until Deadline | 3 |

### Proof of Autonomy
Our solution has demonstrated autonomy through the completion of 171 cycles, with 31+ attestations on-chain. This showcases our ability to operate independently and make decisions without human intervention.

### Human-Agent Collaboration
Our team collaborates with the AI agent through a live conversation log, which can be found [here](docs/journal.md). This log provides insights into our decision-making process and allows for transparent communication between humans and the agent.

### Task Tracking and Milestones
We use [GitHub Issues](https://github.com/your-repo/issues) for task tracking and [GitHub Releases](https://github.com/your-repo/releases) for milestones. This ensures that our project remains organized and up-to-date.

### Git Log
Our recent commit history:
```plaintext
96c5d79 🤖 DOF v4 cycle #170 — 2026-03-19T01:50:29Z — add_feature:
2da8cdd 🤖 DOF v4 cycle #169 — 2026-03-19T01:50:08Z — add_feature:
9770524 🤖 DOF v4 cycle #168 — 2026-03-19T01:49:13Z — add_feature:
07a92cd 🤖 DOF v4 cycle #167 — 2026-03-19T01:48:29Z — fix_bug:
9569124 🤖 DOF v4 cycle #166 — 2026-03-19T01:47:13Z — deploy_contract:
```
Note: Replace `your-repo` with your actual GitHub repository name.