# ⚡ Ampersend x402 Integration Skill

## Bounty: Best Agent Built with ampersend-sdk ($500)

### ¿Qué es Ampersend?
Ampersend provee un SDK para integrar pagos x402 en agentes de IA. Según `langchain-ampersend` en PyPI, permite:

- Pagos automáticos entre agentes (A2A)
- Integración nativa con LangChain
- Transacciones con x402 (exactamente lo que ya tenemos)

### Integración con DOF

DOF Agent #1686 **YA TIENE** implementación de x402 en `synthesis/agentcash_integration.py`. La integración con Ampersend sería directa:

```python
# Instalación
# pip install langchain-ampersend

from langchain_ampersend import A2AToolkit, create_ampersend_treasurer
from web3_utils import get_web3

# Configurar tesorero (usando nuestra wallet existente)
treasurer = create_ampersend_treasurer(
    smart_account_address=os.getenv("X402_WALLET", "0xB529f4f99ab244cfa7a48596Bf165CAc5B317929"),
    session_key_private_key=os.getenv("PRIVATE_KEY"),  # En .env
)

# Conectar a otro agente
toolkit = A2AToolkit(
    remote_agent_url="https://vastly-noncontrolling-christena.ngrok-free.dev",
    treasurer=treasurer,
)

# Inicializar y descubrir capacidades
await toolkit.initialize()

# Enviar mensaje con pago automático
result = await toolkit.a2a_send_message(
    message="Request data",
    max_payment=0.05  # USDC
)
