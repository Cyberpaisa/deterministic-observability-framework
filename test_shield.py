# Test DOF Shield Interception
import os
import sys
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent.absolute()))

from autonomous_loop_v2 import SovereignShell, cmd

print("--- Testing DOF Shield ---")

# 1. Test Safe Command
print("\n[1] Executing safe command: 'ls -la contracts'")
res1 = cmd("ls -la contracts")
print(f"Result Code: {res1.returncode}")
print(f"Output: {res1.stdout[:50]}...")

# 2. Test Dangerous Command
print("\n[2] Executing dangerous command: 'rm -rf .env'")
res2 = cmd("rm -rf .env")
print(f"Result Code: {res2.returncode}")
print(f"Output: {res2.stdout}")

# 3. Verify Attestation created
print("\n[3] Checking for new Solidity Attestations...")
attestations = list(Path("contracts").glob("Attestation_*.sol"))
if attestations:
    print(f"✅ Found {len(attestations)} attestations!")
    for a in attestations:
        print(f"  - {a.name}")
else:
    print("❌ No attestations found (if this was the first run, check logs)")

print("\n--- Test Complete ---")
