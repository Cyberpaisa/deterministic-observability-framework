import sys
import os
sys.path.append(os.path.abspath('.'))

from autonomous_loop_v2 import task_monitor_ai_news

def test_news():
    print("Testing AI News Monitor...")
    # cycle 3 triggers the module (cycle % 3 == 0)
    task_monitor_ai_news(3)
    print("Test complete.")

if __name__ == "__main__":
    test_news()
