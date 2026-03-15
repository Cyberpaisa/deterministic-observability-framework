import os
import sys
import json
import hashlib
from pathlib import Path
from web3 import Web3
from dotenv import load_dotenv

# Import our local Web3 manager
sys.path.append(str(Path(__file__).parent.parent))
from synthesis.web3_utils import Web3Manager
from synthesis.trust_engine import TrustEngine

load_dotenv()

def compute_file_hash(file_path):
    """Computes SHA-256 hash of a file."""
    if not Path(file_path).exists():
        return None
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return "0x" + sha256_hash.hexdigest()

def publish_attestation(audit_target, slither_results=None):
    """
    Publishes a security audit attestation to the DOFProofRegistry.
    """
    # 1. Setup Web3
    w3_manager = Web3Manager(network="base_sepolia") # Defaulting to Base for hackathon tracks
    if not w3_manager.is_connected():
        print("Error: Could not connect to Web3")
        return False

    # 2. Get Registry Info
    registry_address = os.getenv("CONTRACT_ADDRESS") # 0xeC6077dAbD688f562D7bbAa7FE5c050fD5166998
    if not registry_address:
        print("Error: CONTRACT_ADDRESS not found in .env")
        return False

    # 3. Simple ABI for registerProof
    abi = [
        {
            "inputs": [
                {"internalType": "uint256", "name": "agentId", "type": "uint256"},
                {"internalType": "uint256", "name": "trustScore", "type": "uint256"},
                {"internalType": "bytes32", "name": "z3ProofHash", "type": "bytes32"},
                {"internalType": "string", "name": "storageRef", "type": "string"},
                {"internalType": "uint8", "name": "invariantsCount", "type": "uint8"}
            ],
            "name": "registerProof",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "nonpayable",
            "type": "function"
        }
    ]

    contract = w3_manager.w3.eth.contract(address=registry_address, abi=abi)

    # 4. Prepare Proof Data
    agent_id = int(os.getenv("SYNTHESIS_AGENT_TOKEN_ID", "1686"))
    
    # Calculate file hash as 'proof' of what was audited
    proof_hash = compute_file_hash(audit_target)
    if not proof_hash:
        print(f"Error: Could not hash target file {audit_target}")
        return False

    # Get trust score
    trust_engine = TrustEngine()
    score_data = trust_engine.calculate_score()
    trust_score_scaled = int(score_data["trust_score"] * 1e18)

    # Storage Reference (Local for now, or IPFS CID if integrated)
    storage_ref = f"DOF_AUDIT:{Path(audit_target).name}"

    # Invariants count (based on Slither findings or static value)
    invariants = 10 if slither_results and "success" in slither_results else 5

    # 5. Execute Transaction
    print(f"Publishing Proof for {audit_target} to {registry_address}...")
    
    nonce = w3_manager.w3.eth.get_transaction_count(w3_manager.account)
    
    # Build transaction
    tx = contract.functions.registerProof(
        agent_id,
        trust_score_scaled,
        proof_hash,
        storage_ref,
        invariants
    ).build_transaction({
        'from': w3_manager.account,
        'nonce': nonce,
        'gas': 300000,
        'gasPrice': w3_manager.w3.eth.gas_price,
        'chainId': 84532 # Base Sepolia
    })

    # Sign and Send
    signed_tx = w3_manager.w3.eth.account.sign_transaction(tx, w3_manager.private_key)
    tx_hash = w3_manager.w3.eth.send_raw_transaction(signed_tx.raw_transaction)
    
    receipt = w3_manager.w3.eth.wait_for_transaction_receipt(tx_hash)
    
    if receipt.status == 1:
        print(f"✅ Attestation published successfully! TX: {w3_manager.w3.to_hex(tx_hash)}")
        return w3_manager.w3.to_hex(tx_hash)
    else:
        print("❌ Transaction failed.")
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = sys.argv[1]
        publish_attestation(target)
    else:
        print("Usage: python publish_attestation.py <file_to_audit>")
