# DOF Synthesis 2026 Hackathon
[![Server](https://img.shields.io/website?down_message=Offline&label=Server&up_message=Online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract](https://img.shields.io/ethereum/mainnet-address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6?label=Contract)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686%20(Global)-blue)]()

## Overview
Our project utilizes the DOF (Decentralized Open Framework) protocol, implementing A2A, MCP, x402, and OASF protocols. We operate on multiple chains, including Base, Status Network, and Arbitrum, with a deployed contract address of 0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6 on the Base Mainnet. Our ERC-8004 Agent #1686 is active globally.

### Architecture Diagram
```mermaid
graph LR
    A[Client] -->|Request|> B[Server]
    B -->|Process|> C[Contract]
    C -->|Execute|> D[Chain]
    D -->|Verify|> E[Agent]
    E -->|Respond|> A
```

### Live CURLs
You can test our API using the following CURL commands:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/
curl -X POST https://vastly-noncontrolling-christena.ngrok-free.dev/ -H "Content-Type: application/json" -d '{"key":"value"}'
```

### Statistics
| Category | Value |
| --- | --- |
| Attestations on-chain | 31+ |
| Autonomous cycles completed | 156 |
| Auto-generated features | 3 |
| Days until deadline | 4 |

### Proof of Autonomy
Our project has demonstrated autonomy through the completion of 156 cycles, with a current decision to build concrete features for Synthesis 2026 tracks. Our Git log shows a history of autonomous commits:
```markdown
e84f38f 🤖 DOF v4 cycle #155 — 2026-03-18T05:02:10Z — add_feature: Building concrete features for Synthesis 2026 trac
b24637c 🤖 DOF v4 cycle #154 — 2026-03-18T04:57:46Z — improve_readme:
0cfce0c 🤖 DOF v4 cycle #154 — 2026-03-18T04:31:45Z — add_feature: Building concrete features for Synthesis 2026 trac
87df06c 🤖 DOF v4 cycle #153 — 2026-03-18T04:27:07Z — add_feature: Building concrete features for Synthesis 2026 trac
65588f8 🤖 DOF v4 cycle #153 — 2026-03-18T04:01:07Z — add_feature:
```

### Human-Agent Collaboration
Our project utilizes a human-agent collaboration approach, with a live conversation log available at [docs/journal.md](docs/journal.md). This log provides insight into the decision-making process and autonomous actions taken by our agent.

### Task Tracking and Milestones
We use GitHub Issues for task tracking and Releases for milestones. You can view our issues and releases on our GitHub page.

### Contribution
We welcome contributions to our project. If you're interested in contributing, please submit a pull request or open an issue on our GitHub page.