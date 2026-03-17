# DOF Synthesis 2026 Hackathon
[![Server Status](https://img.shields.io/website?down_message=Offline&up_message=Online&url=https%3A%2F%2Fvastly-noncontrolling-christena.ngrok-free.dev)](https://vastly-noncontrolling-christena.ngrok-free.dev)
[![Contract Address](https://img.shields.io/badge/Contract-0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6-blue)](https://basescan.org/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)
[![ERC-8004 Agent](https://img.shields.io/badge/ERC--8004%20Agent-%231686-blue)]()
[![Multi-Chain](https://img.shields.io/badge/Multi--Chain-Base%2C%20Status%20Network%2C%20Arbitrum-blue)]()
[![License](https://img.shields.io/badge/License-Apache%202.0-blue)](LICENSE)

## Overview
DOF Synthesis 2026 is a cutting-edge, autonomous system utilizing A2A, MCP, x402, and OASF protocols to facilitate seamless interactions across multiple blockchain networks, including Base, Status Network, and Arbitrum. Our ERC-8004 Agent #1686 is a key component of this system, enabling efficient communication and collaboration.

## Architecture
```mermaid
graph LR
    subgraph "External"
        A[Judge / User]
    end

    subgraph "Infrastructure"
        B[ngrok Tunnel<br/>vastly-noncontrolling-christena.ngrok-free.dev]
    end

    subgraph "Server"
        C[Uvicorn Server<br/>synthesis/server.py]
        D[A2A Protocol<br/>/a2a/tasks/send]
        E[MCP Endpoints<br/>/mcp/lido/*]
        F[x402 Payments<br/>/agentcash/*]
    end

    subgraph "Blockchain"
        G[Contract<br/>0x154a3F49...]
        H[Base Mainnet<br/>ERC-8004 #31013]
    end

    subgraph "Autonomous Agent"
        I[DOF Agent #1686]
        J[OpenViking Memory]
        K[Journal / Logs]
    end

    A -->|HTTPS + Header| B
    B -->|HTTPS| C
    C --> D & E & F
    D -->|JSON-RPC| G
    E -->|On-chain queries| H
    F -->|x402 Payments| H
    G --> H
    I --> J
    I --> K
🏆 FUNCTIONAL TRACKS (6 - $21,000)
Track	Prize	Demo	Last Run
MetaMask Delegations	$5,000	metamask_delegation_agent.py	✅ Cycle #85
Octant Data Analysis	$5,000	octant_analyzer.py	✅ Cycle #86
Olas Pearl Integration	$3,000	olas_pearl_agent.py	✅ Cycle #87
Locus Payments	$3,000	locus_agent.py	✅ Cycle #83
SuperRare Art Generator	$2,500	superrare_agent.py	✅ Cycle #84
Arkhai Escrow	$1,000	arkhai_agent.py	✅ Cycle #85
📊 ON-CHAIN EVIDENCE (VERIFIABLE)
Element	Value	Verification
ERC-8004 Agent ID	#31013	🔗 Basescan
Attestations	75+	🔗 Enigma Scanner
Contract Address	0x154a3F49...	🔗 Basescan
Z3 Formal Proofs	8 invariants	Z3_VERIFICATION.md
Live Curls
You can test our API using the following live curls:

bash
curl https://vastly-noncontrolling-christena.ngrok-free.dev/features
curl https://vastly-noncontrolling-christena.ngrok-free.dev/autonomy-cycles
Statistics
Metric	Value
Autonomous Cycles Completed	100
Attestations on-Chain	75+
Auto-Generated Features	5
Days until Deadline	5
📚 JUDGE'S EVIDENCE PACKAGE
Document	Description	Link
📓 Conversation Log	Full human-agent Telegram history	conversation-log.md
📔 Agent Journal	Episodic memory (cycles, decisions, proofs)	journal.md
📈 Evolution Log	Self-audits and agent growth	EVOLUTION_LOG.md
🧠 Autonomous SOUL	Agent identity and core directives	SOUL_AUTONOMOUS.md
Proof of Autonomy
Our system has demonstrated autonomy by completing 100 cycles without human intervention. The contract address is 0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6 and the ERC-8004 Agent #1686 is verified.

Human-Agent Collaboration
Our team collaborates with the agent through a transparent and open process. You can view our Conversation Log to see the live updates and decisions made by the team.

Git Log
Recent commits:

text
4523bc1 🤖 DOF v4 cycle #94 — 2026-03-16T21:29:55Z — add_feature: Building concrete features
0d050b2 🤖 DOF v4 cycle #93 — 2026-03-16T20:59:28Z — add_feature: Building concrete features
09ca2a8 🤖 DOF v4 cycle #92 — 2026-03-16T20:29:02Z — add_feature: Building concrete features
4ca5a17 🤖 DOF v4 cycle #91 — 2026-03-16T19:58:43Z — add_feature: Building concrete features
daf60be 🤖 DOF v4 cycle #90 — 2026-03-16T19:28:24Z — add_feature: Building concrete features

## 🚀 Live Demo
Experience the autonomous agent in action:
[**https://dof-agent-web.vercel.app**](https://dof-agent-web.vercel.app)

[![Vercel Status](https://img.shields.io/website?down_message=Offline&up_message=Online&url=https%3A%2F%2Fdof-agent-web.vercel.app)](https://dof-agent-web.vercel.app)
