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

    def generate_instruction_update(self, analysis_context, current_soul, llm_caller=None):
        """Uses the LLM to analyze the context and suggest a new rule for the SOUL."""
        log.info("Generating evolutionary suggestions using LLM...")
        
        if not llm_caller:
            log.warning("No LLM caller provided to EvolutionEngine. Returning empty suggestions.")
            return []

        prompt = [
            {"role": "system", "content": "You are the evolutionary metacognition core of an autonomous AI agent for a hackathon. Your job is to analyze the agent's recent journal/logs and its current system prompt (SOUL), and propose ONE highly specific, actionable new rule to improve its performance, avoid repeated errors, or optimize its decision-making. Respond ONLY with a JSON array of strings containing the suggested rules. Example: [\"Nueva Regla: Siempre verifica X antes de hacer Y\"]"},
            {"role": "user", "content": f"CURRENT SOUL PROMPT:\n{current_soul[:2000]}\n\nRECENT CYCLE ANALYSIS:\n{analysis_context[:3000]}\n\nBased on failures or patterns in the recent cycles, propose 1 or 2 new evolutionary rules in Spanish."}
        ]

        try:
            response = llm_caller(prompt, max_tokens=500)
            if response:
                # Basic JSON extraction
                clean = response.strip()
                for marker in ["```json", "```"]:
                    if marker in clean:
                        clean = clean.split(marker)[1].split("```")[0]
                suggestions = json.loads(clean.strip())
                if isinstance(suggestions, list):
                    return suggestions
        except Exception as e:
            log.error(f"Failed to generate evolutionary update: {e}")
            
        return []

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
