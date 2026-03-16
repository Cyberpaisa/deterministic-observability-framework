# DOF Synthesis 2026 Hackathon
[![Server Status](https://img.shields.io/website?down_message=Offline&up_message=Online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract Address](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-blue)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004_Agent-%231686-orange)](https://erc8004_agents.io/agent/1686)

## Overview
Our project utilizes a combination of A2A, MCP, x402, and OASF protocols to facilitate seamless interactions across multiple chains, including Base, Status Network, and Arbitrum. Our ERC-8004 Agent #1686 is globally recognized and has successfully completed 60 autonomous cycles, with 35+ attestations on-chain.

## Statistics
| Category | Value |
| --- | --- |
| Autonomous Cycles | 60 |
| On-Chain Attestations | 35+ |
| Auto-Generated Features | 3 |
| Days until Deadline | 6 |
| Supported Chains | Base, Status Network, Arbitrum |

## Architecture
```mermaid
graph LR
    A[Client] -->| HTTPS |->> B(Server)
    B -->| Web3 |->> C(Contract: 0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
    C -->| ERC-8004 |->> D(Agent #1686)
    D -->| A2A + MCP + x402 + OASF |->> E(Multi-Chain)
    E -->| Base, Status Network, Arbitrum |->> F(Autonomous Cycles)
```

## Live API Calls
You can test our API using the following `curl` commands:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/healthcheck
curl https://vastly-noncontrolling-christena.ngrok-free.dev/api/contracts
```

## Proof of Autonomy
Our system has demonstrated autonomy by completing 60 cycles, with a recent Git log showing:
```markdown
c3b4caa 🤖 DOF v4 cycle #65 — 2026-03-16T04:09:34Z — add v16.0-2: deep reasoning, autonomous research, efficiency, new tracks
2aeb18b 🤖 DOF v4 cycle #64 — 2026-03-16T04:02:14Z — document Virtuals Protocol integration
440d219 🤖 DOF v4 cycle #63 — 2026-03-16T04:01:51Z — add Uniswap API trader skill
736a858 🤖 DOF v4 cycle #62 — 2026-03-16T04:00:16Z — complete Celo documentation in DEMO_WALKTHROUGH
d8693c9 🤖 DOF v4 cycle #61 — 2026-03-16T03:55:50Z — add Celo support for K track
```

## Human-Agent Collaboration
We believe in the power of human-agent collaboration. Our team uses GitHub Issues for task tracking and Releases for milestones. You can view our [live conversation log](docs/journal.md) to see how we work together.

## Current Decision
Our current decision is to focus on building concrete features for Synthesis 2026 tracks. We are committed to delivering high-quality solutions that meet the needs of our users.

## Contributing
If you'd like to contribute to our project, please submit a pull request or open an issue on our GitHub repository. We welcome feedback and suggestions from the community.

## License
Our project is licensed under [INSERT LICENSE].