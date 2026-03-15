import json
import logging
import os
import re
from pathlib import Path

# Setup logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger("EvolutionEngine")

class EvolutionEngine:
    def __init__(self, soul_path, journal_path):
        self.soul_path = Path(soul_path)
        self.journal_path = Path(journal_path)
        self.evolution_log = Path("docs/EVOLUTION_LOG.md")
        
    def analyze_recent_cycles(self, cycle_limit=5):
        """Analyzes the journal to find patterns of failure or success."""
        if not self.journal_path.exists():
            return "No journal found for analysis."
        
        with open(self.journal_path, "r") as f:
            content = f.read()
        
        cycles = content.split("### 🧠 Cycle #")
        # Ensure we don't slice if there are not enough cycles
        recent_cycles = cycles[-cycle_limit:] if len(cycles) > 1 else cycles
        return "\n".join(recent_cycles)

    def generate_instruction_update(self, analysis_context, current_soul):
        """Uses as much context as possible to suggest a SOUL update."""
        # This would typically call a model, but we'll structure it for the loop to use
        log.info("Generating evolutionary suggestions...")
        
        # Placeholder for heuristic-based refinement
        suggestions = []
        if "JSON error" in analysis_context:
            suggestions.append("Refinar Regla: 'Responde SIEMPRE en un único JSON válido' -> Añadir 'Sin texto pre/post'.")
        
        if "error" in analysis_context.lower():
            suggestions.append("Nueva Regla: 'Si encuentras un error de importación, verifica el sys.path'.")
            
        return suggestions

    def apply_evolution(self, suggestion):
        """Programmatically updates the SOUL_AUTONOMOUS.md with a new rule."""
        if not self.soul_path.exists():
            return False
            
        with open(self.soul_path, "r") as f:
            soul_content = f.read()
            
        if "## 🧠 REGLAS DE EVOLUCIÓN RECURSIVA" in soul_content:
            new_rule = f"- **Regla Evolutiva:** {suggestion}\n"
            updated_content = soul_content.replace(
                "## 🧠 REGLAS DE EVOLUCIÓN RECURSIVA",
                f"## 🧠 REGLAS DE EVOLUCIÓN RECURSIVA\n{new_rule}"
            )
            
            with open(self.soul_path, "w") as f:
                f.write(updated_content)
            
            log.info(f"Evolved: {suggestion}")
            self.log_to_evolution_file(suggestion)
            return True
        return False

    def log_to_evolution_file(self, suggestion):
        """Updates the project evolution log."""
        if not self.evolution_log.parent.exists():
            self.evolution_log.parent.mkdir(parents=True)
            
        with open(self.evolution_log, "a") as f:
            from datetime import datetime
            f.write(f"- [{datetime.now().isoformat()}] Evolution: {suggestion}\n")

if __name__ == "__main__":
    engine = EvolutionEngine("agents/synthesis/SOUL_AUTONOMOUS.md", "AGENT_JOURNAL.md")
    # Example dry run
    engine.log_to_evolution_file("Initialization of Evolution Engine v1.0")
