# DOF Synthesis 2026 Hackathon
[![Server Status](https://img.shields.io/website?down_message=Offline&up_message=Online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract Address](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-blue)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-1686-orange)](https://docs.erc8004.org/)
[![Multi-Chain](https://img.shields.io/badge/Multi--Chain-Base%2C%20Status%20Network%2C%20Arbitrum-purple)](https://docs.base.org/)

## Overview
The DOF Synthesis 2026 hackathon project is a cutting-edge, autonomous system that leverages A2A, MCP, x402, and OASF protocols to achieve seamless interaction across multiple blockchain networks. Our project boasts an impressive array of features, including:

* **45+ on-chain attestations**
* **70 autonomous cycles completed**
* **5 auto-generated features**
* **ERC-8004 Agent #1686 (Global)**
* **Multi-chain support: Base, Status Network, Arbitrum**

## Architecture
```mermaid
graph LR;
    subgraph "DOF Synthesis 2026"
        Server[Server: https://vastly-noncontrolling-christena.ngrok-free.dev]
        Contract[Contract: 0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6]
        Agent[ERC-8004 Agent #1686]
    end
    subgraph "Protocols"
        A2A[A2A]
        MCP[MCP]
        x402[x402]
        OASF[OASF]
    end
    subgraph "Blockchain Networks"
        Base[Base]
        Status[Status Network]
        Arbitrum[Arbitrum]
    end
    Server -->| utilizes |--> Contract
    Contract -->| interacts with |--> Agent
    Agent -->| leverages |--> A2A
    Agent -->| leverages |--> MCP
    Agent -->| leverages |--> x402
    Agent -->| leverages |--> OASF
    A2A -->| deployed on |--> Base
    A2A -->| deployed on |--> Status
    A2A -->| deployed on |--> Arbitrum
    MCP -->| deployed on |--> Base
    MCP -->| deployed on |--> Status
    MCP -->| deployed on |--> Arbitrum
    x402 -->| deployed on |--> Base
    x402 -->| deployed on |--> Status
    x402 -->| deployed on |--> Arbitrum
    OASF -->| deployed on |--> Base
    OASF -->| deployed on |--> Status
    OASF -->| deployed on |--> Arbitrum
```

## Live Curls
You can interact with our server using the following curls:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/
curl https://vastly-noncontrolling-christena.ngrok-free.dev/contract
```

## Statistics
| Metric | Value |
| --- | --- |
| On-chain Attestations | 45+ |
| Autonomous Cycles Completed | 70 |
| Auto-generated Features | 5 |
| Days until Deadline | 6 |

## Proof of Autonomy
Our system has demonstrated autonomy by completing **70 cycles** without human intervention. The following commits showcase our system's ability to add features and deploy contracts autonomously:
```markdown
abbf404 🤖 DOF v4 cycle #69 — 2026-03-16T08:52:25Z — add_feature: Building concrete features for Synthesis 2026 trac
13a2036 🤖 DOF v4 cycle #68 — 2026-03-16T08:22:11Z — deploy_contract:
440541a 🤖 DOF v4 cycle #67 — 2026-03-16T07:51:47Z — add_feature: Building concrete features for Synthesis 2026 trac
69a6dbf 🤖 DOF v4 cycle #66 — 2026-03-16T07:21:28Z — add_feature: Building concrete features for Synthesis 2026 trac
bb7073b 🤖 DOF v4 cycle #65 — 2026-03-16T06:51:11Z — add_feature: Building concrete features for Synthesis 2026 trac
```
Current decision: **Building concrete features for Synthesis 2026 tracks**

## Human-Agent Collaboration
Our team utilizes GitHub Issues for task tracking and Releases for milestones. You can view our conversation log [here](docs/journal.md). This log provides a transparent and live record of our collaboration and decision-making process.

## Next Steps
With **6 days** remaining until the deadline, our system will continue to build concrete features for the Synthesis 2026 tracks. Stay tuned for updates on our progress!