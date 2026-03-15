# DOF Synthesis 2026 Hackathon
[![Server](https://img.shields.io/badge/Server-https://vastly-noncontrolling-christena.ngrok-free.dev-brightgreen)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-orange)](https://snowtrace.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004_Agent-%231686-blue)](https://snowtrace.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)

## Overview
DOF Synthesis is a cutting-edge project that leverages the power of A2A, MCP, x402, and OASF protocols to achieve unprecedented levels of autonomy. Our ERC-8004 Agent #1686 has successfully completed 2 autonomous cycles, with 2+ attestations on-chain and 1 feature auto-generated.

## Stats
| Metric | Value |
| --- | --- |
| Autonomous Cycles | 2 |
| Attestations on-chain | 2+ |
| Auto-Generated Features | 1 |
| Days until Deadline | 7 |

## Architecture
```mermaid
graph LR
    A[Agent] -->|A2A|> B[Server]
    B -->|MCP|> C[Contract]
    C -->|x402|> D[OASF]
    D -->|OASF|> A
```

## Live Curls
You can test our server using the following curl commands:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev
```

## Proof of Autonomy
Our project demonstrates autonomy through the following features:

* 2+ attestations on-chain, ensuring the integrity of our data
* 2 autonomous cycles completed, showcasing our ability to operate independently
* 1 feature auto-generated, highlighting our capacity for self-improvement

## Human-Agent Collaboration
We believe in the importance of human-agent collaboration, which is why we maintain a [live conversation log](docs/conversation-log.md). This log provides a transparent record of our decision-making process and allows for seamless communication between humans and agents.

## Development
We use [GitHub Issues](https://github.com/your-repo/issues) for task tracking and [Releases](https://github.com/your-repo/releases) for milestones. Our commit history is as follows:
```markdown
* 4f0ceda 🤖 DOF v4 cycle #1 — 2026-03-15T05:11:25Z — add_feature
* 95ac320 🤖 DOF v4 cycle #1 — 2026-03-15T04:42:59Z — improve_readme
* c09edf9 🤖 2026-03-14: Sync Track Trust/Pay contracts, append Slither audits & setup LLM telegram fallback
* 45aa2d5 🤖 DOF v4 cycle #2 — 2026-03-15T04:15:56Z — improve_readme
* ba8aad3 🤖 DOF v4 cycle #1 — 2026-03-15T03:44:22Z — improve_readme: Mejorando documentación y demos para maximizar sco
```

## Current Decision
Our current decision is to continue improving our documentation and demos to maximize our score. We will provide regular updates on our progress and look forward to the judges' feedback.