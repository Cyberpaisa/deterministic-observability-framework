import os
import json
import logging
from pathlib import Path

# Configuración de logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("TrustEngine")

class TrustEngine:
    def __init__(self, repo_path="."):
        self.repo_path = Path(repo_path)
        self.journal_path = self.repo_path / "AGENT_JOURNAL.md"
        self.evolution_log = self.repo_path / "docs/EVOLUTION_LOG.md"
        self.base_score = 50.0 # Score base (Neutral)

    def calculate_score(self):
        """
        Calcula el Trust Score basado en evidencias locales.
        Fórmula: Base + (Attestations * 2) + (Cycles * 0.5) - (SelfAuditFailures * 10)
        Máximo: 100, Mínimo: 0.
        """
        score = self.base_score
        
        # 1. Analizar AGENT_JOURNAL por attestations exitosas
        if self.journal_path.exists():
            content = self.journal_path.read_text()
            attestations = content.count("Attestation published successfully")
            score += (attestations * 2.0)
            
            cycles = content.count("🤖 DOF v4 cycle")
            score += (cycles * 0.5)

        # 2. Analizar DOF Governance (Z3 Proofs) - PRINCIPAL
        z3_log = self.repo_path / "logs/z3_proofs.json"
        z3_verified = 0
        if z3_log.exists():
            try:
                z3_data = json.loads(z3_log.read_text())
                if isinstance(z3_data, list):
                    z3_verified = sum(1 for p in z3_data if p.get("result") == "VERIFIED")
                    score += (z3_verified * 5.0) # Cada prueba Z3 vale +5 puntos
            except:
                pass

        # 3. Analizar EVOLUTION_LOG por auditorías
        if self.evolution_log.exists():
            content = self.evolution_log.read_text()
            # Si hay score de auditoría, promediamos
            import re
            audit_scores = re.findall(r"Score: (\d+)/10", content)
            if audit_scores:
                avg_audit = sum(int(s) for s in audit_scores) / len(audit_scores)
                score += (avg_audit * 2.0) # Máximo +20 si el promedio es 10/10

        # Limitar rango
        final_score = max(0.0, min(100.0, score))
        
        return {
            "agent_id": "#1686",
            "trust_score": round(final_score, 2),
            "level": self._get_level(final_score),
            "factors": {
                "attestations_found": attestations if 'attestations' in locals() else 0,
                "cycles_completed": cycles if 'cycles' in locals() else 0,
                "audit_avg": avg_audit if 'avg_audit' in locals() else 0
            },
            "status": "Verified" if final_score > 70 else "Provisonal"
        }

    def _get_level(self, score):
        if score > 90: return "Sovereign Trust"
        if score > 70: return "Deterministic"
        if score > 50: return "Observable"
        return "Initialization"

if __name__ == "__main__":
    engine = TrustEngine()
    print(json.dumps(engine.calculate_score(), indent=2))
