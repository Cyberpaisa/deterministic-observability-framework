import os
import platform
import subprocess
import logging

logger = logging.getLogger("enigma.hardware_optimizer")

class HardwareOptimizer:
    """
    Optimiza el rendimiento de Enigma basándose en el hardware detectado.
    Enfocado en chips Apple Silicon (M1/M2/M3/M4).
    """
    def __init__(self):
        self.system = platform.system()
        self.machine = platform.machine()
        self.processor = platform.processor()

    def detect_capabilities(self):
        """Detecta si estamos en un Apple Silicon potente (M4 Max detected)."""
        is_apple_silicon = "arm" in self.machine.lower() or "apple" in self.processor.lower()
        
        # Detectar RAM total
        try:
            ram_gb = int(subprocess.check_output(['sysctl', '-n', 'hw.memsize']).decode().strip()) / (1024**3)
        except:
            ram_gb = 0

        info = {
            "is_apple_silicon": is_apple_silicon,
            "ram_gb": round(ram_gb, 2),
            "chip_family": self.processor if is_apple_silicon else "Generic",
            "suggested_backend": "MLX / MPS" if is_apple_silicon else "CPU/CUDA"
        }
        return info

    def apply_optimizations(self):
        """Aplica variables de entorno para aceleración por hardware."""
        info = self.detect_capabilities()
        
        if info["is_apple_silicon"]:
            logger.info(f"🚀 Apple Silicon detectado ({info['chip_family']}). Optimizando para Metal Performance Shaders (MPS)...")
            os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"
            os.environ["OLLAMA_NUM_GPU"] = "1" # Forzar uso de GPU en Ollama
            os.environ["MLX_MAX_MEM"] = f"{int(info['ram_gb'] * 0.70)}G" # Usar hasta el 70% de RAM para MLX
            
            # Sugerencia de modelos basados en 36GB RAM
            if info["ram_gb"] >= 32:
                logger.info("💎 Memoria detectada >= 32GB. Recomendado: Qwen2.5-32B o Llama-3.1-70B (4-bit).")
            else:
                logger.info("📊 Memoria detectada < 32GB. Recomendado: Llama-3.1-8B o Mistral-Nemo-12B.")
        
        return info

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    optimizer = HardwareOptimizer()
    stats = optimizer.apply_optimizations()
    print(f"\n--- Optimización de Sistema Completada ---")
    print(f"Chip: {stats['chip_family']}")
    print(f"RAM Disponible: {stats['ram_gb']} GB")
    print(f"Backend Sugerido: {stats['suggested_backend']}")
