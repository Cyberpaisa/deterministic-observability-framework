# 🔗 ENS Resolution Skill

## Objetivo
Permitir a DOF resolver nombres ENS a direcciones y viceversa, habilitando comunicación y pagos entre agentes usando nombres legibles.

## Implementación
```python
from web3 import Web3
import os

class ENSResolver:
    def __init__(self, rpc_url=None):
        if not rpc_url:
            rpc_url = os.getenv("ETH_RPC_URL", "https://mainnet.infura.io/v3/your-key")
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
    
    def resolve_name(self, name):
        """Resolver nombre ENS a dirección"""
        if not name.endswith('.eth'):
            name = f"{name}.eth"
        try:
            address = self.w3.ens.address(name)
            return {"success": True, "name": name, "address": address}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def reverse_resolve(self, address):
        """Resolver dirección a nombre ENS"""
        try:
            name = self.w3.ens.name(address)
            return {"success": True, "address": address, "name": name}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def agent_to_agent_payment(self, from_agent, to_agent_name, amount):
        """Simular pago entre agentes usando nombres ENS"""
        to_address = self.resolve_name(to_agent_name)
        if not to_address.get("success"):
            return {"error": "Nombre ENS no encontrado", "details": to_address}
        
        # Simulación de pago x402
        return {
            "status": "simulated",
            "from": from_agent,
            "to_name": to_agent_name,
            "to_address": to_address.get("address"),
            "amount": amount,
            "currency": "USDC",
            "protocol": "x402",
            "dry_run": True
        }
    
    def a2a_handshake_with_ens(self, agent_name):
        """Iniciar handshake A2A usando nombre ENS"""
        address = self.resolve_name(agent_name)
        if not address.get("success"):
            return {"error": "No se pudo resolver nombre"}
        
        # Simular handshake (igual que el actual pero con nombre)
        return {
            "status": "handshake_initiated",
            "agent_name": agent_name,
            "agent_address": address.get("address"),
            "timestamp": __import__("datetime").datetime.now().isoformat(),
            "signature": "simulated_signature"
        }
