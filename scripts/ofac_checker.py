import os
import json
import logging
from typing import Dict, Any, Tuple

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("OFAC-Checker")

# Simulated OFAC Sanctions List (Ethereum Addresses)
# Source: U.S. Department of the Treasury (Simulated for Hackathon Demo)
SANCTIONED_ADDRESSES = {
    # Tornado Cash Router
    "0xd90e2f925da726b50c4ed8d0fb90ad053324f31b": "Tornado Cash (OFAC Sanctioned 2022-08-08)",
    # Lazarus Group (North Korea) Hash
    "0x8576acc5c05d6ce88f4e49bf65bdf0c62f91353c": "Lazarus Group associated address",
    # Chatex (Ransomware) 
    "0x7f367cc41522ce07553e823bf3be79a889debe1b": "Chatex OTC Service",
    # Hydra Market
    "0x1f9090aae28b8a3dceadf281b0f12828e676c326": "Hydra Market linked entity"
}

def check_address_compliance(address: str) -> Tuple[bool, str]:
    """
    Checks if an Ethereum address is present on the OFAC sanctions list.
    
    Args:
        address (str): The Ethereum address to check (0x...)
        
    Returns:
        Tuple[bool, str]: (is_compliant, reason/message)
    """
    if not address or not address.startswith("0x"):
        return False, "Invalid address format"
        
    addr_lower = address.lower()
    
    if addr_lower in SANCTIONED_ADDRESSES:
        entity = SANCTIONED_ADDRESSES[addr_lower]
        logger.warning(f"🚨 COMPLIANCE ALERT: Address {address} is on the OFAC Sanctions List! Entity: {entity}")
        return False, f"Address sanctioned: {entity}"
        
    logger.info(f"✅ COMPLIANCE CHECK PASSED: Address {address} is clear.")
    return True, "Address is clear of sanctions"

def verify_transaction_payload(payload: Dict[str, Any]) -> Tuple[bool, str]:
    """
    Verifies a transaction payload (e.g., from an x402 payment) for compliance.
    """
    target_address = payload.get("to")
    
    if not target_address:
         return True, "No target address in payload, ignoring compliance check."
         
    is_compliant, msg = check_address_compliance(target_address)
    
    if not is_compliant:
        # Pre-emptive strike: Block the transaction
        logger.error(f"Transaction blocked by Compliance Engine (Track 4). Reason: {msg}")
        
    return is_compliant, msg

if __name__ == "__main__":
    # Test the checker directly
    print("Testing clean address:")
    check_address_compliance("0x1111111111111111111111111111111111111111")
    
    print("\nTesting sanctioned address (Tornado Cash):")
    check_address_compliance("0xd90e2f925Da726b50C4Ed8D0Fb90Ad053324F31b")
