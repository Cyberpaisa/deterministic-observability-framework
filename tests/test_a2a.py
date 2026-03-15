import sys
import os
sys.path.append(os.path.abspath('.'))

from autonomous_loop_v2 import task_a2a_cooperation

def test_a2a():
    print("Testing A2A Handshake...")
    # cycle 4 triggers the module (cycle % 4 == 0)
    task_a2a_cooperation(4)
    print("Test complete.")

if __name__ == "__main__":
    test_a2a()
