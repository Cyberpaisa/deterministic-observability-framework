# 🦄 Uniswap API Trader Skill

## Objetivo
Permitir a DOF interactuar con Uniswap API para trades autónomos.

## Requisitos
- API key de Uniswap Developer Platform
- Conexión a Ethereum/Base

## Implementación
```python
import requests
import os

class UniswapTrader:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("UNISWAP_API_KEY")
        if not self.api_key:
            raise ValueError("UNISWAP_API_KEY required")
        self.base_url = "https://api.uniswap.org/v1"
    
    def get_quote(self, token_in, token_out, amount, chain="ethereum"):
        """Obtener quote para swap"""
        headers = {"x-api-key": self.api_key}
        params = {
            "tokenIn": token_in,
            "tokenOut": token_out,
            "amount": amount,
            "chainId": 1 if chain == "ethereum" else 8453  # Base
        }
        response = requests.get(
            f"{self.base_url}/quote",
            headers=headers,
            params=params
        )
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.status_code, "message": response.text}
    
    def execute_swap(self, quote_id, recipient, private_key=None):
        """Ejecutar swap con quote aprobada"""
        # Nota: Esta función requiere implementación segura
        # con manejo de private keys
        return {"status": "simulated", "quote_id": quote_id}
