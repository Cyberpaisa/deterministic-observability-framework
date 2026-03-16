# DOF Synthesis 2026 Hackathon
=====================================

[![Server Status](https://img.shields.io/website?down_color=red&down_message=Offline&up_color=green&up_message=Online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract Address](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-orange)](https://etherscan.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004_Agent-%231686-blue)](https://erc8004.io/agents/1686)

## Overview
--------

The DOF Synthesis 2026 hackathon project is a cutting-edge, autonomous system utilizing A2A, MCP, x402, and OASF protocols to facilitate seamless interactions across multiple blockchain networks, including Base, Status Network, and Arbitrum. Our ERC-8004 Agent #1686 is a key component of this system, enabling efficient communication and collaboration.

## Architecture
------------

The following diagram illustrates the high-level architecture of our system:
```mermaid
graph LR
    participant Server as "https://vastly-noncontrolling-christena.ngrok-free.dev"
    participant Contract as "0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6 (Base Mainnet)"
    participant Agent as "ERC-8004 Agent #1686"
    participant Chains as "Base, Status Network, Arbitrum"

    Server -- Autonomy Cycles --> Agent
    Agent -- Interchain Communication --> Chains
    Contract -- On-chain Attestations --> Chains
```

## Live Curls
-------------

You can test our API using the following live curls:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/features
curl https://vastly-noncontrolling-christena.ngrok-free.dev/autonomy-cycles
```

## Stats
-----

| Metric | Value |
| --- | --- |
| Autonomous Cycles Completed | 95 |
| Features Auto-Generated | 5 |
| On-chain Attestations | 70+ |
| Days until Deadline | 6 |

## Proof of Autonomy
------------------

Our system has demonstrated significant autonomy, with 95 cycles completed and 5 features auto-generated. We utilize a combination of A2A, MCP, x402, and OASF protocols to ensure efficient and secure interactions.

## Human-Agent Collaboration
-------------------------

Our team collaborates closely with the ERC-8004 Agent #1686 to ensure seamless execution of autonomy cycles. You can view our live conversation log at [docs/journal.md](docs/journal.md).

## Task Tracking and Milestones
-----------------------------

We use [GitHub Issues](https://github.com/your-username/DOF-Synthesis-2026/issues) for task tracking and [GitHub Releases](https://github.com/your-username/DOF-Synthesis-2026/releases) for milestones.

## Git Log
--------

Recent commits:
```markdown
* 4523bc1 🤖 DOF v4 cycle #94 — 2026-03-16T21:29:55Z — add_feature: Building concrete features for Synthesis 2026 trac
* 0d050b2 🤖 DOF v4 cycle #93 — 2026-03-16T20:59:28Z — add_feature: Building concrete features for Synthesis 2026 trac
* 09ca2a8 🤖 DOF v4 cycle #92 — 2026-03-16T20:29:02Z — add_feature: Building concrete features for Synthesis 2026 trac
* 4ca5a17 🤖 DOF v4 cycle #91 — 2026-03-16T19:58:43Z — add_feature: Building concrete features for Synthesis 2026 trac
* daf60be 🤖 DOF v4 cycle #90 — 2026-03-16T19:28:24Z — add_feature: Building concrete features for Synthesis 2026 trac
```
Current decision: Building concrete features for Synthesis 2026 tracks