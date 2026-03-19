import os
import subprocess
import logging
from datetime import datetime

logger = logging.getLogger("enigma.cloud_sync")

class SovereignCloudSync:
    """
    Automatiza la sincronización de Enigma con su Caja Fuerte (GitHub Privado).
    Asegura que el código, la memoria y el alma estén a salvo.
    """
    def __init__(self):
        self.repo_dir = "/Users/jquiceva/equipo de agentes/deterministic-observability-framework"

    def run_git(self, args):
        try:
            result = subprocess.run(["git"] + args, cwd=self.repo_dir, capture_output=True, text=True)
            return result.stdout.strip(), result.returncode
        except Exception as e:
            return str(e), 1

    def sync(self):
        """Ejecuta el ciclo de sincronización."""
        logger.info("🔐 Iniciando Sincronización con la Caja Fuerte...")
        
        # 1. Agregar cambios
        self.run_git(["add", "."])
        
        # 2. Commit con timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        stdout, code = self.run_git(["commit", "-m", f"🛡️ Sovereign Backup Sync - {timestamp}"])
        
        if "nothing to commit" in stdout:
            logger.info("✅ No hay cambios nuevos que sincronizar.")
            return True

        # 3. Push al remoto principal
        stdout, code = self.run_git(["push"])
        
        if code == 0:
            logger.info("🚀 Sincronización exitosa con la Caja Fuerte de GitHub.")
            return True
        else:
            logger.error(f"❌ Error en el push: {stdout}")
            return False

if __name__ == "__main__":
    sync_engine = SovereignCloudSync()
    sync_engine.sync()
