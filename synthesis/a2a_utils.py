
import json
import os
from eth_account import Account
from eth_account.messages import encode_typed_data

class A2AUtils:
    """Utility for ERC-8004, OASF and x402 compliance"""
    
    @staticmethod
    def generate_registration(agent_id, name, wallet_address, skills=[]):
        """Generates a compliant registration.json with OASF skills"""
        data = {
            "type": "https://eips.ethereum.org/EIPS/eip-8004#registration-v1",
            "name": name,
            "description": "DOF Observation Agent. Deterministic, Autonomous, Secure.",
            "services": [
                {
                    "name": "A2A",
                    "endpoint": f"https://dof-agent-{agent_id}.vercel.app/a2a",
                    "version": "0.3.0"
                },
                {
                    "name": "OASF",
                    "endpoint": "https://github.com/Cyber-Paisa/deterministic-observability-framework",
                    "version": "0.8",
                    "skills": skills or ["security/audit", "web3/observability"]
                },
                {
                    "name": "agentWallet",
                    "endpoint": f"eip155:84532:{wallet_address}"
                }
            ],
            "x402Support": True,
            "registrations": [
                {
                    "agentId": agent_id,
                    "agentRegistry": "eip155:84532:0x8004A169FB4a3325136EB29fA0ceB6D2e539a432"
                }
            ]
        }
        return data

    @staticmethod
    def sign_x402_payment(private_key, recipient, amount, chain_id=84532, asset="0x036CbD53842c5426634e7929541eC2318f3dCF7e"):
        """Signs an EIP-712 TransferWithAuthorization for x402"""
        account = Account.from_key(private_key)
        
        # EIP-712 Domain for USDC on Base Sepolia
        domain_data = {
            "name": "USD Coin",
            "version": "2",
            "chainId": chain_id,
            "verifyingContract": asset,
        }
        
        # TransferWithAuthorization message
        message_data = {
            "from": account.address,
            "to": recipient,
            "value": int(amount),
            "validAfter": 0,
            "validBefore": 2**256 - 1, # Max uint256
            "nonce": os.urandom(32)
        }
        
        # Types (Standard USDC)
        types = {
            "TransferWithAuthorization": [
                {"name": "from", "type": "address"},
                {"name": "to", "type": "address"},
                {"name": "value", "type": "uint256"},
                {"name": "validAfter", "type": "uint256"},
                {"name": "validBefore", "type": "uint256"},
                {"name": "nonce", "type": "bytes32"},
            ]
        }
        
        structured_data = encode_typed_data(domain_data, types, message_data)
        signed = account.sign_message(structured_data)
        
        return {
            "x402Version": 1,
            "payload": {
                "signature": signed.signature.hex(),
                "payload": message_data
            },
            "network": "base-sepolia",
            "asset": asset,
            "amount": str(amount)
        }
