import os
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

class Web3Manager:
    def __init__(self, network="base_sepolia"):
        self.network = network
        # Fallback to general RPC_URL if specific ones aren't found
        if network == "base_sepolia":
            self.rpc = os.getenv("BASE_SEPOLIA_RPC") or os.getenv("RPC_URL") or "https://sepolia.base.org"
        else:
            self.rpc = os.getenv("AVALANCHE_RPC_URL") or os.getenv("RPC_URL")

        self.w3 = Web3(Web3.HTTPProvider(self.rpc))
        
        # Keys (prefer BASE specific if on base, otherwise fallback to generic/avalanche)
        self.private_key = os.getenv("BASE_PRIVATE_KEY") or os.getenv("AVALANCHE_PRIVATE_KEY") or os.getenv("PRIVATE_KEY") or os.getenv("PRIVATE_KEY_AVALANCHE")
        
        if self.private_key:
            from eth_account import Account
            account = Account.from_key(self.private_key)
            self.account = os.getenv("BASE_WALLET_ADDRESS") or os.getenv("AVALANCHE_WALLET_ADDRESS") or os.getenv("WALLET_ADDRESS") or account.address
        else:
            self.account = os.getenv("BASE_WALLET_ADDRESS") or os.getenv("AVALANCHE_WALLET_ADDRESS") or os.getenv("WALLET_ADDRESS")

    def is_connected(self):
        return self.w3.is_connected()

    def get_balance(self, address=None):
        if not address: address = self.account
        balance_wei = self.w3.eth.get_balance(address)
        return self.w3.from_wei(balance_wei, 'ether')

    def send_microtransaction(self, to_address, amount_ether):
        """Implementación básica para Track 1: Agents that Pay"""
        nonce = self.w3.eth.get_transaction_count(self.account)
        tx = {
            'nonce': nonce,
            'to': to_address,
            'value': self.w3.to_wei(amount_ether, 'ether'),
            'gas': 21000,
            'gasPrice': self.w3.eth.gas_price,
            'chainId': 84532 if self.network == "base_sepolia" else 43114
        }
        signed_tx = self.w3.eth.account.sign_transaction(tx, self.private_key)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return self.w3.to_hex(tx_hash)

if __name__ == "__main__":
    manager = Web3Manager()
    print(f"Connected to {manager.network}: {manager.is_connected()}")
    if manager.is_connected():
        print(f"Balance: {manager.get_balance()} ETH")
