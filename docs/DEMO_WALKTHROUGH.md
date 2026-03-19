# Synthesis 2026 — Demo Walkthrough

## Track: Celo Agentic Apps ($10,000)

### Demo: Celo Integration
DOF Agent #1686 now supports the Celo network for autonomous contract deployment and transactions.

**Steps to test:**
1. **Connect to Celo Alfajores:**
   ```python
   from web3_utils import get_celo_web3
   w3 = get_celo_web3("alfajores")
   print(w3.is_connected())  # Should return True
   ```

2. **Deploy Contract (Simulated):**
   ```python
   from web3_utils import deploy_to_celo
   result = deploy_to_celo(bytecode, abi)
   print(result)  # {"status": "ready", "network": "alfajores"}
   ```

---

## Track: Agents that pay (bond.credit) — $1,000

### Demo: Autonomous Trading Agent
DOF Agent #1686 implements a creditworthy trading agent with the following characteristics:

- **Autonomous Trading Logic**: Located in `synthesis/creditworthy_agent.py`.
- **Trust Score Integration**: Powered by TrstLyr (on-chain reputation).
- **ERC-8004 Identity**: Registered as Agent #31013 with 30+ verified attestations.
- **x402 Payment Capability**: Native support for agent-to-agent settlements.

### How to test:
```bash
python3 synthesis/creditworthy_agent.py --simulate --amount 100
```

### On-chain proof:
- **Agent ID**: #1686
- **Attestations**: 30+
- **Trust Score**: Available via TrstLyr API
