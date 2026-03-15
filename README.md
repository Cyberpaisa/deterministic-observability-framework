# DOF Synthesis 2026 Hackathon
==========================

[![Server](https://img.shields.io/badge/Server-https://vastly-noncontrolling-christena.ngrok-free.dev-brightgreen)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-orange)](https://snowtrace.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004_Agent-1686-blue)](https://docs.erc8004.org/)
[![Protocols](https://img.shields.io/badge/Protocols-A2A_%2B_MCP_%2B_x402_%2B_OASF-purple)](https://en.wikipedia.org/wiki/Protocol_(communications))
[![Attestations](https://img.shields.io/badge/Attestations-2%2B_on--chain-red)](https://en.wikipedia.org/wiki/Attestation)
[![Autonomous Cycles](https://img.shields.io/badge/Autonomous_Cycles-2_complated-yellow)](https://en.wikipedia.org/wiki/Autonomous_system)
[![Features Auto-Generated](https://img.shields.io/badge/Features_Auto--Generated-1-green)](https://en.wikipedia.org/wiki/Automatic_programming)
[![Days until Deadline](https://img.shields.io/badge/Days_until_Deadline-7-important)](https://www.timeanddate.com/countdown/)

## Architecture Diagram
The following diagram illustrates the high-level architecture of our system:
```mermaid
graph LR
    A[Server] -->|NGROK|> B[Contract]
    B -->|ERC-8004|> C[Agent #1686]
    C -->|A2A + MCP + x402 + OASF|> D[Attestations]
    D -->|On-Chain|> E[Autonomous Cycles]
    E -->|Auto-Generated|> F[Features]
```
## Live CURLs
You can test our system using the following live CURLs:
```bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/
curl -X POST -H "Content-Type: application/json" -d '{"agent_id": 1686}' https://vastly-noncontrolling-christena.ngrok-free.dev/attest
```
## Proof of Autonomy
Our system has completed 2 autonomous cycles, with 2+ attestations on-chain. The following Git log entries demonstrate our progress:
```markdown
### Git Log
* e64c30f 🤖 DOF v4 cycle #2 — 2026-03-15T01:46:52Z — none:
* 37d53b8 🤖 DOF v4 cycle #1 — 2026-03-15T01:18:47Z — improve_readme: Mejorar el README para facilitar la comprensión de
* f71c19e 🤖 DOF v4 cycle #1 — 2026-03-15T01:16:35Z — none:
* d960e89 🤖 Autonomous cycle #21 — 2026-03-15T01:13:12Z
* 974a514 🤖 Autonomous cycle #20 — 2026-03-15T00:43:04Z
```
Our current decision is to create the `trust_score.py` file to start generating technical evidence.

## Next Steps
With 7 days remaining until the deadline, our next steps will focus on:

* Implementing the `trust_score.py` file
* Expanding our autonomous cycles
* Increasing the number of on-chain attestations
* Continuing to improve our system's autonomy and features

We are confident that our system will continue to demonstrate autonomy and provide value in the remaining time.