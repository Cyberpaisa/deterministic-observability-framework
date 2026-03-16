
## Track: Celo Agentic Apps ($10,000)

### Demo: Celo Integration
DOF Agent #1686 ahora soporta la red Celo para despliegue de contratos y transacciones autónomas.

**Pasos para probar:**
1. Conectar a Celo Alfajores:
   ```python
   from web3_utils import get_celo_web3
   w3 = get_celo_web3("alfajores")
   print(w3.is_connected())  # Debe ser True

2. Desplegar contrato (próximamente):
   ```python
   from web3_utils import deploy_to_celo
   result = deploy_to_celo(bytecode, abi)
   print(result)  # {"status": "ready", "network": "alfajores"}

## Track: Agents that pay (bond.credit) - $1,000

### Demo: Autonomous Trading Agent
DOF Agent #1686 implements a creditworthy trading agent with:

- **Autonomous trading logic** in `synthesis/creditworthy_agent.py`
- **Trust score integration** via TrstLyr (on-chain reputation)
- **ERC-8004 identity** #31013 with 30+ attestations
- **x402 payment capability** for agent-to-agent settlements

### How to test
```bash
python3 synthesis/creditworthy_agent.py --simulate --amount 100

### On-chain proof
- Agent ID: #1686
- Attestations: 30+
- Trust score: Available via TrstLyr API
