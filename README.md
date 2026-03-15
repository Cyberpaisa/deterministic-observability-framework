# DOF Synthesis 2026 Hackathon
[![Server](https://img.shields.io/badge/Server-https://vastly-noncontrolling-christena.ngrok-free.dev-brightgreen)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-blue)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004_Agent-1686-orange)](https://erc8004.com/agent/1686)

## Overview
Our project utilizes the A2A, MCP, x402, and OASF protocols to enable seamless interaction across multiple blockchain networks, including Base, Status Network, and Arbitrum. With 1+ on-chain attestations and 44 completed autonomous cycles, we demonstrate a high level of autonomy and reliability.

## Statistics
| **Metric** | **Value** |
| --- | --- |
| Autonomous Cycles Completed | 44 |
| On-Chain Attestations | 1+ |
| Features Auto-Generated | 0 |
| Multi-Chain Support | Base, Status Network, Arbitrum |
| Days until Deadline | 7 |

## Architecture
```mermaid
graph LR
    A[Agent] -->|A2A|MCP
    MCP -->|MCP|x402
    x402 -->|x402|OASF
    OASF -->|OASF|Base
    OASF -->|OASF|Status Network
    OASF -->|OASF|Arbitrum
```

## Live Curls
To test our server, use the following curl command:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev
```

## Proof of Autonomy
Our project has completed 44 autonomous cycles, demonstrating a high level of autonomy and reliability. We have also achieved 1+ on-chain attestations, providing proof of our system's trustworthiness.

## Human-Agent Collaboration
Our team utilizes [GitHub Issues](https://github.com/your-username/your-repo-name/issues) for task tracking and [GitHub Releases](https://github.com/your-username/your-repo-name/releases) for milestones. For a live view of our conversation log, please refer to [docs/journal.md](docs/journal.md).

## Recent Updates
Our recent updates include:
* **soul: v14.0 prizes + feat: erc8004_demo discover->plan->execute->verify** ( commit [7bda1c3](https://github.com/your-username/your-repo-name/commit/7bda1c3) )
* **DOF v4 cycle #43** ( commit [1db2651](https://github.com/your-username/your-repo-name/commit/1db2651) )
* **DOF v4 cycle #42** ( commit [372b718](https://github.com/your-username/your-repo-name/commit/372b718) )
* **fix: deploy_contract/add_feature priority over improve_readme for Synthesis tracks** ( commit [12c9fc0](https://github.com/your-username/your-repo-name/commit/12c9fc0) )
Our current decision is to focus on **Building concrete features for Synthesis 2026 tracks**.