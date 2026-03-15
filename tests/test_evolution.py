import sys
import os
sys.path.append(os.path.abspath('.'))

from synthesis.evolution_engine import EvolutionEngine
from autonomous_loop_v2 import groq, load_soul

def test_evolution():
    print("Testing Evolution Engine...")
    evo = EvolutionEngine("agents/synthesis/SOUL_AUTONOMOUS.md", "AGENT_JOURNAL.md")
    
    analysis = evo.analyze_recent_cycles(2)
    current_soul = str(load_soul())
    
    print("Sending to LLM via Groq Fallback Cascade...")
    suggestions = evo.generate_instruction_update(analysis, current_soul, llm_caller=groq)
    
    print("\n--- LLM Suggestions ---")
    print(suggestions)
    
    if suggestions:
        print("\nApplying first suggestion as a dry run (printing only)...")
        # We won't actually write to the soul file in this test to avoid corrupting it,
        # we just want to see if the LLM generation works.
        print(f"Would apply: {suggestions[0]}")
    else:
        print("\nNo suggestions generated.")

if __name__ == "__main__":
    test_evolution()
