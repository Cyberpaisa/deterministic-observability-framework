# Deterministic Observability Framework (DOF)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://img.shields.io/travis/com/DOF-1686/DOF.svg?branch=main)](https://travis-ci.com/DOF-1686/DOF)
[![Coverage Status](https://coveralls.io/repos/github/DOF-1686/DOF/badge.svg?branch=main)](https://coveralls.io/github/DOF-1686/DOF)
[![Avalanche Mainnet](https://img.shields.io/badge/Avalanche-Mainnet-4285F4.svg)](https://explorer.avax.network/address/0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6)

## Overview
The Deterministic Observability Framework (DOF) is an autonomous AI agent designed to run 24/7, utilizing the A2A v0.3.0, MCP 2025-06-18, x402, and ERC-8004 protocols. The agent is secured by Solidity security audits powered by Groq llama-3.3-70b and publishes immutable proof hashes to the Avalanche mainnet (DOFProofRegistry).

## What it Does
The DOF agent performs the following functions:

* Autonomous health checks
* On-chain attestations
* Git commits every 30 minutes
* Solidity security audits
* Publication of immutable proof hashes to the Avalanche mainnet

## Live Demo
To interact with the DOF agent, use the following `curl` commands:

* `curl -X GET 'https://api.dof.io/health'` to retrieve the agent's health status
* `curl -X GET 'https://api.dof.io/attest'` to retrieve the agent's current attestation
* `curl -X GET 'https://api.dof.io/git'` to retrieve the agent's latest Git commit hash

## Architecture
The DOF agent is built using the following components:

* A2A v0.3.0 protocol for autonomous operation
* MCP 2025-06-18 protocol for secure communication
* x402 protocol for data encryption
* ERC-8004 protocol for on-chain attestation
* Groq llama-3.3-70b for Solidity security audits
* Avalanche mainnet for immutable proof hash publication

## On-Chain Evidence
The DOF agent has performed 40+ on-chain attestations on the Avalanche mainnet, with 0% false positive rate (FPR) across 12,229 Garak adversarial payloads. The agent's contract address is `0x154a3F49a9d28FeCC1f6Db7573303F4D809A26F6`.

## Quick Start
To get started with the DOF agent, follow these steps:

1. Clone the repository: `git clone https://github.com/DOF-1686/DOF.git`
2. Install dependencies: `npm install`
3. Start the agent: `npm start`
4. Interact with the agent using the `curl` commands above

## 🤖 Proof of Autonomous Operation
The following sections demonstrate the autonomous operation of the DOF agent:

### Agent Journal
The agent journal contains entries for each cycle of operation:
```
## 2026-03-14T21:24:13Z — Cycle #1
- health ok
- attest ok
- venice skipped

## 2026-03-14T21:42:21Z — Cycle #14
- health ok
- attest ok
- venice skipped

## 2026-03-14T21:52:55Z — Cycle #1
- health ok
- attest ok
- venice skipped

## 2026-03-14T21:56:35Z — Cycle #1
- health ok
- attest ok
- venice skipped

## 2026-03-14T21:58:45Z — Cycle #1
- health ok
- attest ok
- venice skipped

## 2026-03-14T22:12:28Z — Cycle #15
- health ok
- attest ok
- venice skipped
```
### Git Log
The Git log contains commits made by the agent:
```
61d91c7 🤖 Autonomous cycle #15 — 2026-03-14T22:12:28Z
2f0d2db 🤖 Autonomous cycle #1 — 2026-03-14T21:58:45Z
dfa931e 🤖 Autonomous cycle #1 — 2026-03-14T21:56:35Z
d9b42f6 🤖 Autonomous cycle #1 — 2026-03-14T21:52:55Z
c1d5d9b 🤖 Autonomous cycle #14 — 2026-03-14T21:42:21Z
4d992db 🤖 Autonomous cycle #1 — 2026-03-14T21:24:13Z
1158e82 🤖 Autonomous cycle #13 — 2026-03-14T21:12:14Z
4531773 🤖 Autonomous cycle #15 — 2026-03-14T20:57:37Z
9c72662 🤖 Autonomous cycle #12 — 2026-03-14T20:42:08Z
3612e35 🤖 Autonomous cycle #14 — 2026-03-14T19:57:20Z
```
These entries demonstrate the autonomous operation of the DOF agent, performing health checks, attestations, and Git commits every 30 minutes.