import sys
import os

# Asegurar que el path del proyecto esté incluido
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

try:
    from core.mission_control import MissionControl
except ImportError:
    # Fallback si se ejecuta desde core/
    from mission_control import MissionControl

def main():
    mc = MissionControl()
    mc.start_chat_session()

if __name__ == "__main__":
    main()

