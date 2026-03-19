import os
import json
import logging
from pathlib import Path

logger = logging.getLogger("SovereignSkillEngine")

class SovereignSkillEngine:
    """
    Modular skill engine for the Legion of 13 Agents.
    Enables dynamic loading and sharing of technical capabilities.
    """
    def __init__(self, skills_path="./core/skills"):
        self.skills_path = Path(skills_path)
        self.registry = {}
        self.skills_path.mkdir(parents=True, exist_ok=True)

    def register_skill(self, name, manifest):
        """Registers a new technical skill from a manifest."""
        self.registry[name] = manifest
        logger.info(f"Skill '{name}' registered for the Legion.")

    def load_skills(self):
        """Loads all skills from the skills directory."""
        for skill_dir in self.skills_path.iterdir():
            if skill_dir.is_dir():
                manifest_path = skill_dir / "manifest.json"
                if manifest_path.exists():
                    try:
                        with open(manifest_path, 'r') as f:
                            manifest = json.load(f)
                            self.register_skill(manifest['name'], manifest)
                    except Exception as e:
                        logger.error(f"Failed to load skill from {skill_dir}: {e}")

    def get_skill_for_agent(self, agent_id):
        """Returns the set of authorized tools for a specific agent."""
        # In Victory Mode, all agents have shared access, but some are specialized.
        authorized_skills = []
        for name, manifest in self.registry.items():
            if "universal" in manifest.get("tags", []) or agent_id in manifest.get("authorized_agents", []):
                authorized_skills.append(name)
        return authorized_skills

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    engine = SovereignSkillEngine()
    
    # Bootstrap standard Celo Skill Manifest
    celo_manifest = {
        "name": "celo-sovereign",
        "description": "High-level agentic flow for Celo Alfajores attestations and payments.",
        "version": "1.0.0",
        "tags": ["universal", "blockchain", "high-impact"],
        "authorized_agents": ["blockchain-wizard", "defi-orbital", "enigma-core"]
    }
    
    # Save bootstrap
    skill_dir = engine.skills_path / "celo_sovereign"
    skill_dir.mkdir(exist_ok=True)
    with open(skill_dir / "manifest.json", "w") as f:
        json.dump(celo_manifest, f, indent=4)
        
    engine.load_skills()
    print(f"✅ Sovereign Skill Engine initialized with {len(engine.registry)} active skills.")
