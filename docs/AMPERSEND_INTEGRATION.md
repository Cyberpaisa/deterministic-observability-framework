# ⚡ Ampersend x402 Integration - DOF Agent #1686

## Bounty: Best Agent Built with ampersend-sdk ($500)

### Nuestra Propuesta

DOF Agent #1686 ya implementa **pagos x402** en `synthesis/agentcash_integration.py`. Ampersend proporciona un SDK (`langchain-ampersend`) que facilita exactamente este tipo de pagos entre agentes.

### Integración Conceptual

```python
# pip install langchain-ampersend
from langchain_ampersend import A2AToolkit, create_ampersend_treasurer
from web3_utils import get_web3

# 1. Configurar tesorero con nuestra wallet
treasurer = create_ampersend_treasurer(
    smart_account_address=os.getenv("X402_WALLET"),
    session_key_private_key=os.getenv("PRIVATE_KEY"),
)

# 2. Conectar a otro agente (ej: OpenClaw)
toolkit = A2AToolkit(
    remote_agent_url="https://vastly-noncontrolling-christena.ngrok-free.dev",
    treasurer=treasurer,
)

# 3. Pagar por una consulta
result = await toolkit.a2a_send_message(
    message="Analyze wallet 0x123...",
    max_payment=0.01  # USDC
)
