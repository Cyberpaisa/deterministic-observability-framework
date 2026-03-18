# DOF Synthesis 2026 Hackathon
[![Server](https://img.shields.io/badge/Server-https://vastly--noncontrolling--christena.ngrok--free.dev-brightgreen)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-blue)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686%20%28Global%29-red)](https://erc8004.com/agent/1686)

## Overview
DOF Synthesis 2026 is a cutting-edge project that leverages A2A, MCP, x402, and OASF protocols to facilitate seamless interactions across multiple chains, including Base, Status Network, and Arbitrum. Our ERC-8004 Agent #1686 is deployed on the Base Mainnet, ensuring secure and efficient transactions.

## Architecture
The following diagram illustrates our architecture:
```mermaid
graph LR
    A[Client] -->| HTTPS |->> B(NGROK)
    B -->| Webhook |->> C[Server]
    C -->| Smart Contract |->> D[Base Mainnet]
    D -->| Multi-Chain |->> E[Status Network]
    E -->| Multi-Chain |->> F[Arbitrum]
    F -->| x402 |->> G[x402 Service]
    G -->| OASF |->> H[OASF Service]
```

## Statistics
| Metric | Value |
| --- | --- |
| Autonomous Cycles Completed | 145 |
| On-Chain Attestations | 36+ |
| Auto-Generated Features | 7 |
| Days until Deadline | 4 |

## Live Curls
To test our API, you can use the following `curl` commands:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/healthcheck
curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/stats
```

## Proof of Autonomy
Our project has achieved significant autonomy, with 145 cycles completed and 36+ on-chain attestations. We have also auto-generated 7 features, demonstrating our system's capabilities.

## Human-Agent Collaboration
We believe in the power of human-agent collaboration. Our [Conversation Log](docs/journal.md) is available for review, showcasing the live interactions between our team and the AI agent. This log provides valuable insights into our development process and decision-making.

## Development Process
We use [GitHub Issues](https://github.com/your-repo/issues) for task tracking and [Releases](https://github.com/your-repo/releases) for milestones. Our Git log is as follows:
```markdown
3d2f4d9 🤖 DOF v4 cycle #144 — 2026-03-18T00:34:18Z — add_feature:
0f98be5 feat: ETHSkills v20.0 — 18 Ethereum production skills injected into SOUL
199748b 🤖 DOF v4 cycle #143 — 2026-03-18T00:02:53Z — add_feature:
f2b2f95 docs: final README v2 — clean professional, judge-ready, agent-proof
c1ab24b 🤖 DOF v4 cycle #142 — 2026-03-17T23:32:24Z — add_feature: Building concrete features for Synthesis 2026 trac
```
Current decision: Building concrete features for Synthesis 2026 tracks.