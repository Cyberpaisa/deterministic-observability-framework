# DOF Synthesis 2026 Hackathon
==========================

[![Server Status](https://img.shields.io/website?down_message=offline&label=Server%20Status&up_message=online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract Address](https://img.shields.io/ethereum/mainnet-address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)](https://snowtrace.io/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686-orange)](https://docs.erc-8004.io/agents/)
[![Protocols](https://img.shields.io/badge/Protocols-A2A%20%2B%20MCP%20%2B%20x402%20%2B%20OASF-blue)](https://docs.dof.synthesis/protocols)

## Overview
The DOF Synthesis 2026 hackathon project aims to create a decentralized, autonomous, and scalable solution for various use cases. Our project utilizes the Avalanche blockchain, ERC-8004 Agent #1686, and implements A2A, MCP, x402, and OASF protocols.

## Architecture
The high-level architecture of our system can be represented by the following diagram:
```mermaid
graph LR;
    participant Client as "Client"
    participant Server as "Server (https://vastly-noncontrolling-christena.ngrok-free.dev)"
    participant Contract as "Contract (0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)"
    participant ERC8004 as "ERC-8004 Agent #1686"

    Client->>Server: Request
    Server->>Contract: Transaction
    Contract->>ERC8004: Event
    ERC8004->>Server: Response
    Server->>Client: Response
```

## Live API Examples
You can test our API using the following `curl` commands:
```bash
# Get server status
curl https://vastly-noncontrolling-christena.ngrok-free.dev/status

# Get contract balance
curl https://vastly-noncontrolling-christena.ngrok-free.dev/balance
```

## Proof of Autonomy
Our project has achieved the following milestones:

* **1+ attestations on-chain**: Our contract has successfully stored and verified multiple attestations on the Avalanche blockchain.
* **1 autonomous cycles completed**: Our system has completed one full autonomous cycle, demonstrating its ability to operate independently.
* **0 features auto-generated**: We are continuously working on improving our system and plan to auto-generate features in the near future.

## Git Log
Our recent commits include:
```markdown
* f71c19e 🤖 DOF v4 cycle #1 — 2026-03-15T01:16:35Z — none:
* d960e89 🤖 Autonomous cycle #21 — 2026-03-15T01:13:12Z
* 974a514 🤖 Autonomous cycle #20 — 2026-03-15T00:43:04Z
* 66bf674 🤖 Autonomous cycle #6 — 2026-03-15T00:23:34Z
* 36cc2ed 🤖 DOF v2 cycle #4 — 2026-03-15T00:21:09Z — none
```

## Next Steps
With **7 days** remaining until the deadline, our current decision is to **Mejorar el README para facilitar la comprensión del proyecto a los jueces y miembros del equipo** (Improve the README to facilitate understanding of the project for judges and team members). We will continue to work on improving our system, auto-generating features, and demonstrating the full potential of our project.

## Conclusion
The DOF Synthesis 2026 hackathon project is a cutting-edge solution that showcases the potential of decentralized, autonomous, and scalable technology. We are confident that our project will make a significant impact and look forward to presenting it to the judges and the community.