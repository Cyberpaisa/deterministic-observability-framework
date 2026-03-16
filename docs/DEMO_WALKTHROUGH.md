
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
