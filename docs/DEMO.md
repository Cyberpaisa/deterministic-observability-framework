# DOF Agent #1686 - Functional Demos for Judges

This document contains step-by-step instructions to run all functional demos for the tracks we participated in. Each demo is a Python script that you can execute and see the results in real-time.

## Prerequisites

```bash
# 1. Clone the repository
git clone https://github.com/Cyberpaisa/deterministic-observability-framework.git
cd deterministic-observability-framework

# 2. Install dependencies
pip install -r requirements.txt  # if exists
pip install web3 requests python-dotenv

## Track 1: MetaMask Delegations ($5,000)

**File:** `synthesis/metamask_delegation_agent.py`

**What it does:** Creates an ERC-7715 delegation with streaming payments, simulates user approval, and executes a delegated action.

```bash
python3 synthesis/metamask_delegation_agent.py

**Expected output:**
- Delegation created with amount, duration, and hash
- Logs in terminal showing the flow
- Entry added to `docs/journal.md`

---

## Track 2: Octant Data Analysis ($5,000)

**File:** `synthesis/octant_analyzer.py`

**What it does:** Analyzes synthetic cyclone data, classifies tracks by duration and strength, and generates a report.

```bash
python3 synthesis/octant_analyzer.py

**Expected output:**
- JSON with analysis results (total analyzed, filtered, categories)
- Entry added to `docs/journal.md`

---

## Track 3: Olas Pearl Integration ($3,000)

**File:** `synthesis/olas_pearl_agent.py`

**What it does:** Simulates deploying an agent on Pearl and hiring another agent, with full logging.

```bash
python3 synthesis/olas_pearl_agent.py

**Expected output:**
- Deployment confirmation with agent ID
- Hiring confirmation with payment simulation
- Entries in `docs/journal.md`

---

## Track 4: Locus Payments ($3,000)

**File:** `synthesis/locus_agent.py`

**What it does:** Creates a wallet with $1000 USDC, defines spending policies, and executes payments with auto-approval and human-in-the-loop simulation.

```bash
python3 synthesis/locus_agent.py
