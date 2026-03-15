import sys
import os
from pathlib import Path
import json

# Add current dir to path to import autonomous_loop_v2
sys.path.append(os.getcwd())

from autonomous_loop_v2 import run_slither_audit

test_file = "contracts/test_vulnerable.sol"
print(f"--- Running Slither Test on {test_file} ---")

ok, report = run_slither_audit(test_file)

print(f"\nAudit Passed: {ok}")
print(f"Report Summary:\n{report}")

if not ok:
    print("\n✅ Verification SUCCESS: Slither correctly blocked the vulnerable contract.")
else:
    print("\n❌ Verification FAILED: Slither should have blocked this contract.")
