import os
import tarfile
import datetime
import logging

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
        Recomendado: GitHub (Private Repo) o Hugging Face Spaces.
        """
        # TODO: Implementar git push o upload a HF/Drive
        logger.info(f"🔄 Preparando sincronización vía {method}...")
        pass

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    manager = CloudBackupManager()
    manager.create_local_package()
