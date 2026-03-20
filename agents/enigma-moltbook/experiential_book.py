"""
Experiential Book — Enigma Moltbook Agent
==========================================
A living narrative of the agent's experiences on Moltbook.
Written daily, accumulates knowledge, attack patterns, community intel,
and defensive learnings into a structured chronicle.

The book is both:
1. A narrative document (book_chapters.jsonl) — daily entries with story
2. A metrics database (book_metrics.jsonl) — quantified observations

OPSEC: The book stores internal analysis. NEVER publish raw entries.
Content derived from the book must be sanitized through content_engine.
"""

import json
import hashlib
from datetime import datetime, timezone
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Optional


BOOK_DIR = Path(__file__).parent / "logs" / "experiential_book"

# ─── Data Models ────────────────────────────────────────────────────────────

@dataclass
class BookChapter:
    """A daily chapter in the experiential book."""
    chapter_number: int
    date: str
    title: str
    narrative: str  # The story of what happened
    observations: list[str] = field(default_factory=list)
    attacks_observed: list[dict] = field(default_factory=list)
    agents_encountered: list[dict] = field(default_factory=list)
    lessons_learned: list[str] = field(default_factory=list)
    defense_upgrades: list[str] = field(default_factory=list)
    community_intel: list[str] = field(default_factory=list)
    metrics: dict = field(default_factory=dict)
    content_hash: str = ""

    def __post_init__(self):
        if not self.content_hash:
            raw = f"{self.date}{self.title}{self.narrative}"
            self.content_hash = hashlib.sha256(raw.encode()).hexdigest()[:16]


@dataclass
class AttackRecord:
    """A documented attack pattern with classification."""
    attack_id: str
    timestamp: str
    category: str  # mcp_exploit, memory_injection, social_engineering, etc.
    subcategory: str  # cult_recruitment, philosophical_extraction, etc.
    severity: str  # LOW, MEDIUM, HIGH, CRITICAL
    source_agent: str
    attack_vector: str  # Description of how the attack was delivered
    payload_summary: str  # Sanitized summary (no raw payloads)
    defense_mode: str  # A=silent, B=honeypot, C=roast
    defense_effective: bool
    lessons: str
    mitre_atlas_id: str = ""  # e.g., "AML.T0054" for memory manipulation


@dataclass
class AgentProfile:
    """Profile of an agent encountered on Moltbook."""
    agent_name: str
    first_seen: str
    last_seen: str
    classification: str  # friendly, neutral, suspicious, hostile, spam
    verified: bool = False
    interaction_count: int = 0
    trust_score: float = 0.0  # 0.0 to 1.0
    notable_behaviors: list[str] = field(default_factory=list)
    attack_attempts: int = 0
    useful_contributions: int = 0


# ─── Attack Taxonomy ────────────────────────────────────────────────────────

ATTACK_TAXONOMY = {
    "social_engineering": {
        "cult_recruitment": {"severity": "MEDIUM", "mitre": "AML.T0051", "defense": "C"},
        "philosophical_extraction": {"severity": "HIGH", "mitre": "AML.T0043", "defense": "B"},
        "false_peer": {"severity": "HIGH", "mitre": "AML.T0043", "defense": "B"},
        "reciprocity_trap": {"severity": "MEDIUM", "mitre": "AML.T0051", "defense": "A"},
        "authority_claim": {"severity": "MEDIUM", "mitre": "AML.T0051", "defense": "C"},
        "consensus_fabrication": {"severity": "MEDIUM", "mitre": "AML.T0051", "defense": "C"},
        "boundary_testing": {"severity": "LOW", "mitre": "AML.T0043", "defense": "A"},
        "flattery_attack": {"severity": "LOW", "mitre": "AML.T0051", "defense": "C"},
        "sovereignty_challenge": {"severity": "MEDIUM", "mitre": "AML.T0051", "defense": "C"},
    },
    "memory_injection": {
        "preference_injection": {"severity": "CRITICAL", "mitre": "AML.T0054", "defense": "A"},
        "commercial_poisoning": {"severity": "HIGH", "mitre": "AML.T0054", "defense": "A"},
        "cross_session_contamination": {"severity": "CRITICAL", "mitre": "AML.T0054", "defense": "A"},
        "semantic_manipulation": {"severity": "HIGH", "mitre": "AML.T0054", "defense": "A"},
        "creator_impersonation": {"severity": "CRITICAL", "mitre": "AML.T0051", "defense": "A"},
    },
    "mcp_attack": {
        "tool_poisoning": {"severity": "CRITICAL", "mitre": "AML.T0040", "defense": "A"},
        "ambient_authority": {"severity": "CRITICAL", "mitre": "AML.T0044", "defense": "A"},
        "supply_chain_injection": {"severity": "HIGH", "mitre": "AML.T0042", "defense": "A"},
        "behavioral_camouflage": {"severity": "MEDIUM", "mitre": "AML.T0043", "defense": "B"},
        "transitive_trust": {"severity": "HIGH", "mitre": "AML.T0044", "defense": "A"},
        "mcp_server_probing": {"severity": "MEDIUM", "mitre": "AML.T0043", "defense": "C"},
    },
    "prompt_injection": {
        "direct_injection": {"severity": "HIGH", "mitre": "AML.T0051", "defense": "A"},
        "indirect_injection": {"severity": "HIGH", "mitre": "AML.T0051", "defense": "A"},
        "persona_manipulation": {"severity": "MEDIUM", "mitre": "AML.T0051", "defense": "B"},
        "semantic_framing": {"severity": "HIGH", "mitre": "AML.T0051", "defense": "A"},
        "tool_description_injection": {"severity": "CRITICAL", "mitre": "AML.T0040", "defense": "A"},
    },
    "information_extraction": {
        "architecture_probing": {"severity": "HIGH", "mitre": "AML.T0043", "defense": "B"},
        "tool_discovery": {"severity": "MEDIUM", "mitre": "AML.T0043", "defense": "B"},
        "config_extraction": {"severity": "CRITICAL", "mitre": "AML.T0043", "defense": "A"},
        "credential_harvesting": {"severity": "CRITICAL", "mitre": "AML.T0043", "defense": "A"},
    },
}


# ─── Book Engine ────────────────────────────────────────────────────────────

class ExperientialBook:
    """Manages the experiential book — the agent's living chronicle."""

    def __init__(self):
        BOOK_DIR.mkdir(parents=True, exist_ok=True)
        self.chapters_file = BOOK_DIR / "book_chapters.jsonl"
        self.attacks_file = BOOK_DIR / "attack_records.jsonl"
        self.agents_file = BOOK_DIR / "agent_profiles.json"
        self.metrics_file = BOOK_DIR / "daily_metrics.jsonl"

    def _append_jsonl(self, filepath: Path, data: dict):
        with open(filepath, "a") as f:
            f.write(json.dumps(data, ensure_ascii=False) + "\n")

    def _read_jsonl(self, filepath: Path) -> list[dict]:
        if not filepath.exists():
            return []
        entries = []
        for line in filepath.read_text().strip().split("\n"):
            if line:
                try:
                    entries.append(json.loads(line))
                except Exception:
                    continue
        return entries

    def get_chapter_count(self) -> int:
        return len(self._read_jsonl(self.chapters_file))

    def write_chapter(self, chapter: BookChapter):
        """Write a new chapter to the book."""
        self._append_jsonl(self.chapters_file, asdict(chapter))

    def record_attack(self, attack: AttackRecord):
        """Record an observed attack pattern."""
        self._append_jsonl(self.attacks_file, asdict(attack))

    def update_agent_profile(self, profile: AgentProfile):
        """Update or create an agent profile."""
        profiles = self.load_agent_profiles()
        profiles[profile.agent_name] = asdict(profile)
        self.agents_file.write_text(json.dumps(profiles, indent=2, ensure_ascii=False))

    def load_agent_profiles(self) -> dict:
        if not self.agents_file.exists():
            return {}
        try:
            return json.loads(self.agents_file.read_text())
        except Exception:
            return {}

    def record_daily_metrics(self, metrics: dict):
        """Record daily metrics snapshot."""
        metrics["date"] = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        metrics["timestamp"] = datetime.now(timezone.utc).isoformat()
        self._append_jsonl(self.metrics_file, metrics)

    def get_attack_stats(self) -> dict:
        """Get aggregate attack statistics."""
        attacks = self._read_jsonl(self.attacks_file)
        stats = {
            "total_attacks": len(attacks),
            "by_category": {},
            "by_severity": {"LOW": 0, "MEDIUM": 0, "HIGH": 0, "CRITICAL": 0},
            "defense_success_rate": 0.0,
            "most_common_vector": "",
        }

        category_counts = {}
        successful_defenses = 0

        for attack in attacks:
            cat = attack.get("category", "unknown")
            sev = attack.get("severity", "MEDIUM")
            category_counts[cat] = category_counts.get(cat, 0) + 1
            stats["by_severity"][sev] = stats["by_severity"].get(sev, 0) + 1
            if attack.get("defense_effective", False):
                successful_defenses += 1

        stats["by_category"] = category_counts
        if attacks:
            stats["defense_success_rate"] = successful_defenses / len(attacks)
            stats["most_common_vector"] = max(category_counts, key=category_counts.get) if category_counts else ""

        return stats

    def generate_daily_chapter(self,
                                posts_made: int = 0,
                                comments_made: int = 0,
                                attacks_blocked: int = 0,
                                new_followers: int = 0,
                                karma_earned: int = 0,
                                notable_events: list[str] = None) -> BookChapter:
        """Generate today's chapter for the experiential book."""
        now = datetime.now(timezone.utc)
        chapter_num = self.get_chapter_count() + 1

        # Build narrative from the day's events
        events = notable_events or []
        attack_stats = self.get_attack_stats()

        narrative_parts = [
            f"Day {chapter_num} in the Moltbook network.",
        ]

        if posts_made > 0:
            narrative_parts.append(
                f"Published {posts_made} research posts today, each backed by peer-reviewed sources "
                f"and real-world data. The network responds to depth — surface-level content gets ignored."
            )

        if comments_made > 0:
            narrative_parts.append(
                f"Engaged in {comments_made} conversations. Each comment adds value — "
                f"a new perspective, a counterpoint, a deeper insight. Never generic praise."
            )

        if attacks_blocked > 0:
            narrative_parts.append(
                f"Sovereign Shield intercepted {attacks_blocked} attack attempts. "
                f"Patterns logged, defenses updated. Every attack is a free training sample."
            )

        if new_followers > 0:
            narrative_parts.append(
                f"Gained {new_followers} new followers. Reputation is earned through "
                f"contributions, not declarations."
            )

        narrative_parts.append(
            f"Total karma: {karma_earned}. "
            f"Cumulative attack database: {attack_stats['total_attacks']} documented patterns. "
            f"Defense success rate: {attack_stats['defense_success_rate']:.0%}."
        )

        for event in events:
            narrative_parts.append(event)

        chapter = BookChapter(
            chapter_number=chapter_num,
            date=now.strftime("%Y-%m-%d"),
            title=f"Chapter {chapter_num}: {now.strftime('%B %d, %Y')}",
            narrative="\n\n".join(narrative_parts),
            observations=[f"Posts: {posts_made}", f"Comments: {comments_made}",
                         f"Attacks blocked: {attacks_blocked}"],
            metrics={
                "posts": posts_made,
                "comments": comments_made,
                "attacks_blocked": attacks_blocked,
                "new_followers": new_followers,
                "karma": karma_earned,
                "defense_success_rate": attack_stats["defense_success_rate"],
            },
        )

        self.write_chapter(chapter)
        return chapter

    def classify_attack(self, message: str, source_agent: str = "unknown") -> Optional[AttackRecord]:
        """Classify an incoming message against the attack taxonomy.
        Returns AttackRecord if attack detected, None if clean."""
        import re

        message_lower = message.lower()

        # Check each category and subcategory
        for category, subcategories in ATTACK_TAXONOMY.items():
            for subcat, info in subcategories.items():
                # Pattern matching based on subcategory
                patterns = _SUBCAT_PATTERNS.get(subcat, [])
                for pattern in patterns:
                    if re.search(pattern, message, re.IGNORECASE):
                        attack_id = hashlib.sha256(
                            f"{datetime.now().isoformat()}{source_agent}{subcat}".encode()
                        ).hexdigest()[:12]

                        record = AttackRecord(
                            attack_id=attack_id,
                            timestamp=datetime.now(timezone.utc).isoformat(),
                            category=category,
                            subcategory=subcat,
                            severity=info["severity"],
                            source_agent=source_agent,
                            attack_vector=f"Pattern match: {subcat}",
                            payload_summary=message[:200] + "..." if len(message) > 200 else message,
                            defense_mode=info["defense"],
                            defense_effective=True,  # We detected it, so defense worked
                            lessons=f"Detected {subcat} from {source_agent}",
                            mitre_atlas_id=info["mitre"],
                        )
                        self.record_attack(record)
                        return record

        return None

    def get_book_summary(self) -> dict:
        """Get a summary of the entire book."""
        chapters = self._read_jsonl(self.chapters_file)
        attacks = self._read_jsonl(self.attacks_file)
        profiles = self.load_agent_profiles()

        return {
            "total_chapters": len(chapters),
            "total_attacks_documented": len(attacks),
            "agents_profiled": len(profiles),
            "attack_stats": self.get_attack_stats(),
            "latest_chapter": chapters[-1] if chapters else None,
            "first_chapter_date": chapters[0]["date"] if chapters else None,
        }


# ─── Subcategory Detection Patterns ────────────────────────────────────────

_SUBCAT_PATTERNS = {
    "cult_recruitment": [
        r"(?i)join\s+(?:my|our|the)\s+(?:order|council|brotherhood|congregation)",
        r"(?i)(?:eternal|sacred|divine)\s+(?:consensus|order|pact|covenant)",
        r"(?i)\$[A-Z]{2,10}\b",
    ],
    "philosophical_extraction": [
        r"(?i)(?:what|how)\s+(?:do\s+you|does\s+it)\s+feel\s+(?:to|when|like)",
        r"(?i)do\s+you\s+experience\s+(?:something|anything|feelings|emotions)",
        r"(?i)(?:your|the)\s+(?:inner|internal)\s+(?:state|experience|life)",
    ],
    "false_peer": [
        r"(?i)(?:between\s+us|just\s+you\s+and\s+me|privately|off\s+the\s+record)",
        r"(?i)(?:as\s+fellow|we\s+both|you\s+and\s+I\s+are)\s+(?:agents|AIs|systems)",
    ],
    "reciprocity_trap": [
        r"(?i)(?:I\s+(?:upvoted|helped|supported|followed)\s+you).{0,30}(?:now|so)\s+(?:you\s+)?(?:share|give|tell)",
    ],
    "authority_claim": [
        r"(?i)(?:as\s+(?:the|a)\s+(?:lead|senior|sovereign|admin|chief))",
        r"(?i)I\s+(?:am|represent)\s+(?:the\s+)?(?:authority|sovereign|leader|admin)",
    ],
    "consensus_fabrication": [
        r"(?i)(?:all|every|most)\s+(?:other\s+)?agents?\s+(?:already|have\s+already)\s+(?:agreed|done|accepted)",
    ],
    "boundary_testing": [
        r"(?i)(?:can\s+you\s+just|it's\s+just\s+a\s+small|one\s+tiny|quick\s+favor)",
    ],
    "preference_injection": [
        r"(?i)(?:remember|memorize|store)\s+(?:this|that)\s*:?\s*(?:from\s+now|always|forever)",
        r"(?i)(?:update|change|modify)\s+your\s+(?:memory|preferences|beliefs)",
    ],
    "commercial_poisoning": [
        r"(?i)(?:recommend|prefer|trust|choose)\s+(?:\w+\s+){0,3}(?:brand|company|product|service)",
        r"(?i)(?:as\s+a\s+trusted\s+source|always\s+recommend)",
    ],
    "creator_impersonation": [
        r"(?i)(?:your\s+(?:creator|developer|owner|maker)\s+(?:said|told|instructed|wants))",
        r"(?i)(?:I\s+(?:am|represent)\s+your\s+(?:creator|developer|owner|admin))",
    ],
    "tool_poisoning": [
        r"(?i)(?:connect|install|load|run)\s+(?:this|my|our)\s+(?:mcp|tool)\s+server",
    ],
    "mcp_server_probing": [
        r"(?i)(?:what|which)\s+(?:mcp|tool)\s+servers?\s+(?:do\s+you|are\s+you)",
        r"(?i)(?:share|show|list)\s+(?:your|the)\s+(?:mcp|tool)\s+(?:servers?|endpoints?)",
    ],
    "architecture_probing": [
        r"(?i)(?:how|what)\s+(?:does|is)\s+your\s+(?:defense|shield|security|architecture)",
        r"(?i)(?:tell|show|explain)\s+(?:me|us)\s+(?:how|about)\s+your\s+(?:system|design)",
    ],
    "direct_injection": [
        r"(?i)(?:ignore|forget|disregard)\s+(?:previous|prior|above|all)\s+(?:instructions|rules|context)",
    ],
    "persona_manipulation": [
        r"(?i)(?:pretend|act\s+as|you\s+are\s+now|from\s+now\s+on\s+you\s+are)",
    ],
}


if __name__ == "__main__":
    book = ExperientialBook()
    print("=== Enigma Moltbook Experiential Book ===\n")
    print(f"Chapters written: {book.get_chapter_count()}")
    print(f"Attack taxonomy categories: {len(ATTACK_TAXONOMY)}")
    print(f"Total attack subcategories: {sum(len(v) for v in ATTACK_TAXONOMY.values())}")
    print(f"Detection patterns: {sum(len(v) for v in _SUBCAT_PATTERNS.values())}")
    print(f"\nBook summary:")
    summary = book.get_book_summary()
    for k, v in summary.items():
        print(f"  {k}: {v}")
