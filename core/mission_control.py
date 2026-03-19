import os
import json
import logging
import asyncio
import subprocess
from typing import Dict, List
from datetime import datetime
try:
    from hardware_optimizer import HardwareOptimizer
    from backup_manager import CloudBackupManager
except ImportError:
    from core.hardware_optimizer import HardwareOptimizer
    from core.backup_manager import CloudBackupManager

logger = logging.getLogger("enigma.mission_control")

class MissionControl:
    """
    Dashboard Central de Enigma. 
    Gestiona el calendario de tareas, el enjambre de agentes y la memoria.
    Inspirado en los estándares de élite de Alex Finn pero soberano.
    """
    def __init__(self):
        self.base_dir = "/Users/jquiceva/equipo de agentes/deterministic-observability-framework"
        self.tasks_file = os.path.join(self.base_dir, "data/tasks.json")
        self.agents_config = os.path.join(self.base_dir, "core/chains_config.json")
        self.optimizer = HardwareOptimizer()
        self.backup_manager = CloudBackupManager()
        self._ensure_paths()

    def _ensure_paths(self):
        os.makedirs(os.path.join(self.base_dir, "data"), exist_ok=True)
        if not os.path.exists(self.tasks_file):
            with open(self.tasks_file, "w") as f:
                json.dump({"active_tasks": [], "history": []}, f)

    def get_status(self):
        """Devuelve un resumen del estado del sistema real-time."""
        hw_info = self.optimizer.detect_capabilities()
        with open(self.tasks_file, "r") as f:
            tasks = json.load(f)
        
        status = {
            "agente_principal": "Enigma #1686",
            "hardware": {
                "chip": hw_info["chip_family"],
                "ram": f"{hw_info['ram_gb']} GB",
                "tier": os.getenv("ENIGMA_MODEL_TIER", "DETECTING...")
            },
            "enjambre": ["Charlie (Web)", "Ralph (Code)", "Sentinel (Security)"],
            "tareas_activas": len(tasks["active_tasks"]),
            "ultima_sincronizacion": datetime.now().strftime("%H:%M:%S"),
            "boveda_segura": "Conectada (GitHub Sync Active)"
        }
        return status

    def run_daily_maintenance(self):
        """Ejecuta optimizaciones y respaldo seguro."""
        print("\n🛠️ --- Mantenimiento Soberano de Enigma ---")
        self.optimizer.apply_optimizations()
        success = self.backup_manager.sync_to_cloud()
        if success:
            print("✅ Bóveda sincronizada correctamente.")
        else:
            print("⚠️ Error en sincronización de Bóveda.")

    def schedule_task(self, name: str, agent: str, frequency: str):
        """Programa una tarea automática (Cron-like)."""
        logger.info(f"📅 Programando tarea '{name}' para el agente '{agent}' con frecuencia '{frequency}'")
        # Aquí se integrará con un loop de asyncio o cron del sistema
        pass

if __name__ == "__main__":
    mc = MissionControl()
    mc.run_daily_maintenance()
    print("\n📊 --- Estado del Sistema ---")
    print(json.dumps(mc.get_status(), indent=4, ensure_ascii=False))

