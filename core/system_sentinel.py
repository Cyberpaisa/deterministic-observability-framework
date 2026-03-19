import os
import logging
import datetime
from typing import List

logger = logging.getLogger("enigma.sentinel")

class SovereignSentinel:
    """
    Guardián de Grado Militar para el entorno de Juan (@Cyber_paisa).
    Protege contra malware, inyecciones y accesos no autorizados.
    """
    def __init__(self):
        self.protected_paths = ["/Users/jquiceva"] # Protegemos el home de Juan
        self.monitored_extensions = [".sh", ".py", ".js", ".exe", ".bin"]
        self.log_file = "SENTINEL_AUDIT.log"

    def audit_link(self, url: str) -> bool:
        """Analiza un link antes de que el agente lo procese."""
        # TODO: Integración con VirusTotal o similar
        suspicious_patterns = ["malware", "phishing", "bypass", "exploit", "drop"]
        for pattern in suspicious_patterns:
            if pattern in url.lower():
                logger.warning(f"⚠️ Link sospechoso detectado: {url}")
                return False
        return True

    def request_permission(self, action: str, target: str) -> bool:
        """
        Bloquea cualquier acción en el sistema operativo que no esté autorizada.
        Cualquier cambio fuera de la carpeta del proyecto requiere permiso explícito.
        """
        critical_dirs = ["/usr", "/etc", "/Applications", "/System"]
        is_critical = any(target.startswith(d) for d in critical_dirs)
        is_outside_project = not "/deterministic-observability-framework/" in target

        if is_critical or is_outside_project:
            logger.info(f"🚫 ACCIÓN BLOQUEADA POR EL SENTINEL: {action} en {target}")
            # En modo autónomo real, esto enviaría un mensaje a Telegram con botones de aprobación.
            return False 
        
        return True

    def log_event(self, event: str):
        """Registra cada evento de seguridad."""
        with open(self.log_file, "a") as f:
            timestamp = datetime.datetime.now().isoformat()
            f.write(f"[{timestamp}] SECURITY_EVENT: {event}\n")

if __name__ == "__main__":
    sentinel = SovereignSentinel()
    print("🛡️ Sovereign Sentinel Activo e Inmune.")
    # Prueba
    sentinel.request_permission("DELETE", "/Users/jquiceva/Documents/importante.docx")
