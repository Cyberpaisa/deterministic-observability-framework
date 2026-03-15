# DOF Synthesis 2026 Hackathon
[![Server Status](https://img.shields.io/website?url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract Address](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-orange)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004_Agent-%231686-blue)](https://erc8004.org/)

## Overview
DOF Synthesis is a cutting-edge, autonomous system leveraging A2A, MCP, x402, and OASF protocols to facilitate seamless interactions across multiple blockchain networks, including Base, Status Network, and Arbitrum. Our system boasts an impressive array of features, including:

* **5+ on-chain attestations**
* **9 autonomous cycles completed**
* **1 auto-generated feature**
* **ERC-8004 Agent #1686 (Global)**

### Architecture
```mermaid
graph LR
    A[Client] -->|HTTPS|> B(NGROK)
    B -->|HTTPS|> C[Server]
    C -->|Web3|> D[Blockchain]
    D -->|Web3|> E[Contract]
    E -->|ERC-8004|> F[Agent]
    F -->|A2A/MCP/x402/OASF|> G[Autonomous System]
```

### Live API Endpoints
You can test our API endpoints using the following `curl` commands:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/status
curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/contract
```

### Proof of Autonomy
Our system has demonstrated autonomy through the completion of 9 cycles, with the following statistics:
| Cycle # | Date | Features Added |
| --- | --- | --- |
| 10 | 2026-03-15T14:30:18Z | - |
| 9 | 2026-03-15T14:05:41Z | 1 |
| 8 | 2026-03-15T14:00:55Z | 1 |

### Human-Agent Collaboration
Our team utilizes a combination of human intuition and autonomous agent capabilities to drive decision-making. You can view our live conversation log [here](docs/conversation-log.md).

### Development and Tracking
We use [GitHub Issues](https://github.com/your-username/DOF-Synthesis/issues) for task tracking and [Releases](https://github.com/your-username/DOF-Synthesis/releases) for milestone management.

### Statistics
| Metric | Value |
| --- | --- |
| Days until deadline | 7 |
| On-chain attestations | 5+ |
| Autonomous cycles completed | 9 |
| Auto-generated features | 1 |
| ERC-8004 Agent ID | #1686 (Global) |

### Recent Git Log
```markdown
e691a66 🤖 DOF v4 cycle #10 — 2026-03-15T14:30:18Z — none:
cca7f5d 🤖 DOF v4 cycle #9 — 2026-03-15T14:05:41Z — add_feature:
037d169 🤖 DOF v4 cycle #8 — 2026-03-15T14:00:55Z — add_feature:
4ba0185 🤖 DOF v4 cycle #9 — 2026-03-15T14:00:09Z — none:
ceb3182 increase LLM token limit to 8000 to prevent truncated code generation
```

With only 7 days remaining until the deadline, our team is committed to pushing the boundaries of autonomous systems and showcasing the potential of human-agent collaboration. Stay tuned for further updates and developments!