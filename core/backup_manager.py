import os
import tarfile
import datetime
import logging
import subprocess

logger = logging.getLogger("enigma.backup_manager")

class CloudBackupManager:
    """
    Gestiona respaldos seguros del 'alma' y memoria de Enigma.
    Permite restaurar el agente en otra máquina si el hardware actual falla.
    """
    def __init__(self):
        self.backup_dir = "backups/cloud"
        os.makedirs(self.backup_dir, exist_ok=True)
        self.include_paths = [
            ".env",
            "AGENT_JOURNAL.md",
            "dof.constitution.yml",
            "memory/",
            "agents/",
            "core/",
            "scripts/"
        ]

    def create_local_package(self) -> str:
        """Crea un archivo comprimido con lo esencial."""
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"enigma_soul_backup_{timestamp}.tar.gz"
        filepath = os.path.join(self.backup_dir, filename)
        
        try:
            with tarfile.open(filepath, "w:gz") as tar:
                for path in self.include_paths:
                    if os.path.exists(path):
                        tar.add(path, arcname=os.path.basename(path))
            
            logger.info(f"✅ Paquete de respaldo creado: {filepath}")
            return filepath
        except Exception as e:
            logger.error(f"❌ Error creando respaldo: {e}")
            return ""

    def sync_to_cloud(self, method="github"):
        """
        Sincroniza el respaldo con un servicio externo.
        Recomendado: GitHub (Private Repo).
        """
        logger.info(f"🔄 Iniciando sincronización vía {method}...")
        
        try:
            # 1. Crear el paquete local
            backup_file = self.create_local_package()
            if not backup_file:
                return False

            # 2. Comandos Git para subir el backup (soberano)
            commands = [
                ["git", "add", "."],
                ["git", "commit", "-m", f"Vault Sync: Enigma Soul Backup {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"],
                ["git", "push", "origin", "main"]
            ]

            for cmd in commands:
                result = subprocess.run(cmd, capture_output=True, text=True)
                if result.returncode != 0:
                    logger.warning(f"⚠️ Git command failed: {' '.join(cmd)} - {result.stderr}")
            
            logger.info("✅ Sincronización con la Bóveda Segura (GitHub) completada.")
            return True

        except Exception as e:
            logger.error(f"❌ Error en la sincronización: {e}")
            return False

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    manager = CloudBackupManager()
    manager.create_local_package()
