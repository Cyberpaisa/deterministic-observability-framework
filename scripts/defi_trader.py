import os
import requests
import logging
from typing import Dict, Optional
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts.ofac_checker import OFACChecker

logger = logging.getLogger("DOF-DeFi")


class DefiTrader:
    """
    Simulates a DeFi trading execution engine for Agents that Trade.
    Fetches real price quotes (using public APIs like CoinGecko) and simulates
    an on-chain swap, blocked by extreme OPSEC OFAC checks.
    """

    def __init__(self):
        self.checker = OFACChecker()
        self.quote_api = "https://api.coingecko.com/api/v3/simple/price"

    def get_quote(self, token_in: str, token_out: str) -> Optional[float]:
        """Fetch a mock exchange rate quote."""
        try:
            # Map standard symbols to coingecko ids
            mapping = {
                "WETH": "ethereum",
                "USDC": "usd-coin",
                "AVAX": "avalanche-2",
                "CBTC": "bitcoin"
            }
            
            id_in = mapping.get(token_in.upper(), "ethereum")
            vs_currency = "usd" # simplifies mock
            
            res = requests.get(f"{self.quote_api}?ids={id_in}&vs_currencies={vs_currency}", timeout=5)
            if res.status_code == 200:
                data = res.json()
                price = data.get(id_in, {}).get(vs_currency)
                if price:
                    return float(price)
            return None
        except Exception as e:
            logger.error(f"Failed to fetch DeFi quote: {e}")
            return None

    def execute_swap(self, target_address: str, token_in: str, token_out: str, amount_in: float) -> Dict:
        """
        Simulate an on-chain Dex swap transaction.
        Enforces 100% OPSEC Zero-Trust compliance checks before 'signing'.
        """
        logger.info(f"Initiating DeFi Swap: {amount_in} {token_in} -> {token_out} on behalf of {target_address}")
        
        # 🚨 OPSEC CORE: Native compliance check before trade execution
        if not self.checker.check_address_compliance(target_address):
            logger.error(f"🚨 TRADE BLOCKED: Address {target_address} listed on OFAC/Sanctions list.")
            return {
                "status": "blocked",
                "reason": "OFAC compliance violation",
                "address": target_address,
                "tx_hash": None
            }

        # Fetch Quote
        price_usd = self.get_quote(token_in, token_out)
        if not price_usd:
            logger.warning("Quotes unavailable. Using fallback deterministic rates.")
            rates = {"WETH": 3500.0, "AVAX": 45.0, "USDC": 1.0}
            price_usd = rates.get(token_in.upper(), 100.0)

        estimated_out = amount_in * price_usd

        # Simulate execution
        mock_tx_hash = f"0xswap{''.join(__import__('random').choices('abcdef0123456789', k=58))}"
        
        return {
            "status": "success",
            "token_in": token_in,
            "token_out": token_out,
            "amount_in": amount_in,
            "estimated_out": estimated_out,
            "tx_hash": mock_tx_hash,
            "compliance_check": "PASSED"
        }

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    trader = DefiTrader()
    # Test valid swap
    print(trader.execute_swap("0xBaseValidatedAddress1234567890", "WETH", "USDC", 0.5))
    # Test sanctioned swap (simulated by containing 'OFAC')
    print(trader.execute_swap("0xOFACSanctionedWallet999999", "AVAX", "USDC", 100))
