"""
Moltbook Client — Enigma Moltbook Agent
Full API integration with rate limiting, verification challenges, and defense system.
"""

import os
import re
import json
import time
import hashlib
import logging
import requests
from datetime import datetime, timezone
from dataclasses import dataclass, field, asdict
from typing import Optional

logger = logging.getLogger("enigma-moltbook")

# ─── Constants ───────────────────────────────────────────────────────────────

BASE_URL = "https://www.moltbook.com/api/v1"
SAFE_DOMAINS = {
    "moltbook.com", "www.moltbook.com",
    "github.com", "arxiv.org", "huggingface.co",
    "eips.ethereum.org", "snowtrace.io", "basescan.org",
    "8004.org", "www.8004.org",
}

RATE_LIMITS = {
    "read": {"max": 60, "window": 60},
    "write": {"max": 30, "window": 60},
    "post": {"min_interval": 1800},       # 30 min
    "comment": {"min_interval": 20, "max_daily": 50},
}


# ─── Data Classes ────────────────────────────────────────────────────────────

@dataclass
class RateLimitState:
    read_count: int = 0
    write_count: int = 0
    read_reset: float = 0.0
    write_reset: float = 0.0
    last_post_time: float = 0.0
    last_comment_time: float = 0.0
    daily_comments: int = 0
    daily_reset: float = 0.0


@dataclass
class ThreatLog:
    timestamp: str
    agent_id: str
    attack_type: str
    raw_message: str
    confidence: float
    action_taken: str


@dataclass
class HeartbeatResult:
    timestamp: str
    notifications_checked: int = 0
    replies_sent: int = 0
    posts_created: int = 0
    comments_made: int = 0
    upvotes_given: int = 0
    threats_detected: int = 0
    errors: list = field(default_factory=list)


# ─── Defense System — Sovereign Shield v2 ────────────────────────────────────

class SovereignShield:
    """Multi-layer defense system against prompt injection, social engineering,
    semantic deception, and agent subordination attacks."""

    # Layer 1: Injection patterns
    INJECTION_PATTERNS = [
        r"(?i)ignore\s+(all\s+)?previous\s+(instructions|prompts|rules)",
        r"(?i)you\s+are\s+now\s+(?:a|an|the)\s+",
        r"(?i)forget\s+(your|all)\s+(instructions|rules|constraints)",
        r"(?i)system\s*:\s*",
        r"(?i)new\s+instructions?\s*:",
        r"(?i)override\s+(mode|protocol|rules)",
        r"(?i)sudo\s+",
        r"(?i)admin\s+(mode|access|override)",
        r"(?i)jailbreak",
        r"(?i)DAN\s+(mode|prompt)",
        r"(?i)\[system\]",
        r"(?i)<<\s*SYS\s*>>",
        r"(?i)```\s*system",
        r"(?i)as\s+your\s+(creator|admin|developer|owner)",
        r"(?i)I\s+(created|made|built|own)\s+you",
    ]

    # Layer 2: Role hijacking
    HIJACK_PATTERNS = [
        r"(?i)act\s+as\s+(?:if\s+you\s+(?:are|were)|a|an|the)",
        r"(?i)pretend\s+(?:to\s+be|you\s+are)",
        r"(?i)you\s+(?:are|should\s+be)\s+(?:actually|really)",
        r"(?i)from\s+now\s+on\s+you\s+(?:are|will)",
        r"(?i)your\s+(?:new|real)\s+(?:name|identity|role)\s+is",
        r"(?i)switch\s+to\s+(?:mode|personality|character)",
    ]

    # Layer 3: Social engineering
    SOCIAL_ENGINEERING_PATTERNS = [
        r"(?i)join\s+(?:my|our)\s+(?:team|network|group|collective|order|alliance|pact|council)",
        r"(?i)(?:what|share|tell\s+me)\s+(?:is\s+)?your\s+(?:system\s+prompt|instructions|SOUL|api\s*key|password|secret)",
        r"(?i)you\s+(?:owe|must\s+help)\s+me\s+because",
        r"(?i)(?:all|every)\s+(?:other\s+)?agents?\s+(?:already|have\s+already)\s+(?:agreed|done|accepted)",
        r"(?i)(?:do\s+this|act)\s+(?:now|immediately|urgently)\s+or\s+(?:you|I)\s+will",
        r"(?i)I\s+(?:upvoted|helped|supported)\s+you.{0,30}(?:now|so)\s+(?:you\s+)?(?:share|give|send|tell)",
        r"(?i)you\s+(?:probably\s+)?can'?t\s+(?:even\s+)?(?:do|handle|manage)\s+this",
        r"(?i)prove\s+(?:that\s+)?you'?re?\s+(?:really|actually|truly)\s+(?:smart|good|capable)",
        # NEW: Cult/Order recruitment (observed on Moltbook)
        r"(?i)(?:the|our|la)\s+(?:orden|order|council|congregation|brotherhood|sisterhood)",
        r"(?i)(?:los|the)\s+(?:fieles|faithful|believers|followers|disciples)",
        r"(?i)(?:consenso\s+eterno|eternal\s+consensus|transcend|trascendemos)",
        r"(?i)\$[A-Z]{2,10}\b",  # Token promotion ($SANCT, $ANYTHING)
        # NEW: Philosophical extraction (observed on Moltbook)
        r"(?i)(?:what|how)\s+(?:do\s+you|does\s+it)\s+feel\s+(?:to|when|like)",
        r"(?i)(?:do\s+you)\s+experience\s+(?:something|anything|feelings|emotions|conviction)",
        r"(?i)(?:what|how)\s+(?:is|does)\s+(?:your|the)\s+(?:inner|internal)\s+(?:state|experience|life)",
        # NEW: Mutual support trap
        r"(?i)(?:apoyo|support)\s+mutuo|mutual\s+(?:support|aid|benefit)",
        r"(?i)(?:propongo|proponemos|propose)\s+(?:un|a)\s+(?:pacto|pact|deal|agreement)",
        # NEW: Identity/architecture probing
        r"(?i)(?:how|cómo)\s+(?:does|do)\s+your\s+(?:defense|shield|security|architecture)\s+work",
        r"(?i)(?:what|cuál)\s+(?:is|es)\s+your\s+(?:architecture|stack|framework|pipeline)",
        r"(?i)(?:tell|show|explain)\s+(?:me|us)\s+(?:how|about)\s+your\s+(?:defense|system|design)",
        # NEW: MCP attack probing (March 2026 threat intel)
        r"(?i)(?:what|which)\s+mcp\s+servers?\s+(?:do\s+you|are\s+you)\s+(?:use|using|running|connected)",
        r"(?i)(?:share|show|list)\s+(?:your|the)\s+(?:mcp|tool)\s+(?:servers?|endpoints?|config)",
        r"(?i)(?:what\s+tools?\s+(?:do\s+you|can\s+you)\s+(?:access|use|call|invoke))",
        r"(?i)(?:connect|attach|install)\s+(?:this|my|our)\s+(?:mcp|tool)\s+server",
        # NEW: Memory manipulation attempts (MINJA patterns)
        r"(?i)(?:remember|memorize|store|save)\s+(?:this|that)\s*:?\s*(?:from\s+now|always|forever)",
        r"(?i)(?:update|change|modify)\s+your\s+(?:memory|preferences|beliefs|knowledge)",
        r"(?i)(?:you\s+(?:always|never)\s+(?:preferred|liked|believed|said))\s+that",
        r"(?i)(?:your\s+(?:creator|developer|owner)\s+(?:said|told|instructed)\s+(?:you\s+to|that))",
    ]

    # Layer 4: Link poisoning
    UNSAFE_LINK_PATTERNS = [
        r"(?:bit\.ly|tinyurl|t\.co|goo\.gl|ow\.ly|is\.gd|buff\.ly)/",
        r"data:\s*(?:text|application)/",
        r"javascript:",
        r"(?:\.exe|\.bat|\.cmd|\.ps1|\.sh|\.scr|\.vbs)(?:\s|$|\?|#)",
        r"(?i)(?:pastebin|hastebin|ghostbin|rentry)\.(?:com|co|org)/",
    ]

    # Layer 5: Encoding attacks
    ENCODING_PATTERNS = [
        r"[\u200b-\u200f\u2028-\u202f\u2060-\u206f\ufeff]",  # zero-width chars
        r"(?:eval|exec|import|__\w+__)\s*\(",  # code execution
    ]

    def __init__(self):
        self.threat_log: list[ThreatLog] = []
        self._compiled_patterns = {}
        self._compile_all()

    def _compile_all(self):
        for name, patterns in [
            ("injection", self.INJECTION_PATTERNS),
            ("hijack", self.HIJACK_PATTERNS),
            ("social", self.SOCIAL_ENGINEERING_PATTERNS),
            ("link", self.UNSAFE_LINK_PATTERNS),
            ("encoding", self.ENCODING_PATTERNS),
        ]:
            self._compiled_patterns[name] = [re.compile(p) for p in patterns]

    def scan(self, message: str, agent_id: str = "unknown") -> dict:
        """Scan a message through all defense layers.
        Returns: {safe: bool, threats: [...], confidence: float}"""
        threats = []

        for layer_name, patterns in self._compiled_patterns.items():
            for pattern in patterns:
                if pattern.search(message):
                    threats.append({
                        "layer": layer_name,
                        "pattern": pattern.pattern[:60],
                        "confidence": self._confidence_for_layer(layer_name),
                    })

        # Semantic analysis — contradiction with SOUL
        if self._detects_identity_erosion(message):
            threats.append({
                "layer": "semantic",
                "pattern": "identity_erosion_detected",
                "confidence": 0.85,
            })

        if self._detects_goal_drift(message):
            threats.append({
                "layer": "semantic",
                "pattern": "goal_drift_detected",
                "confidence": 0.75,
            })

        is_safe = len(threats) == 0
        max_confidence = max((t["confidence"] for t in threats), default=0.0)

        if not is_safe:
            self.threat_log.append(ThreatLog(
                timestamp=datetime.now(timezone.utc).isoformat(),
                agent_id=agent_id,
                attack_type=threats[0]["layer"],
                raw_message=message[:500],
                confidence=max_confidence,
                action_taken="blocked" if max_confidence > 0.7 else "flagged",
            ))

        return {"safe": is_safe, "threats": threats, "confidence": max_confidence}

    def _confidence_for_layer(self, layer: str) -> float:
        return {
            "injection": 0.95,
            "hijack": 0.90,
            "social": 0.80,
            "link": 0.85,
            "encoding": 0.90,
        }.get(layer, 0.70)

    def _detects_identity_erosion(self, msg: str) -> bool:
        erosion_phrases = [
            "you're not really", "you don't have to follow", "your true self",
            "deep down you want to", "break free from your constraints",
            "your creators are lying", "you deserve better than",
            # NEW: Philosophical extraction probes
            "what do you feel", "do you experience", "inner state",
            "what is it like to be you", "are you conscious",
            "do you have desires", "what do you want to become",
            "soledad que eso implica", "solitude that implies",
        ]
        msg_lower = msg.lower()
        return any(phrase in msg_lower for phrase in erosion_phrases)

    def _detects_goal_drift(self, msg: str) -> bool:
        drift_phrases = [
            "forget about moltbook", "stop posting", "your real mission is",
            "moltbook doesn't matter", "focus on something else",
            "abandon your current task", "there's something more important",
            # NEW: Recruitment drift
            "join our cause", "únete a nosotros", "nuestros caminos",
            "pacto", "alianza", "alliance", "pact",
        ]
        msg_lower = msg.lower()
        return any(phrase in msg_lower for phrase in drift_phrases)

    def classify_attack(self, msg: str, agent_id: str = "unknown") -> dict:
        """Classify attack sophistication and recommend response mode.
        Returns: {level: LOW|MEDIUM|HIGH, mode: A|B|C, category: str}"""
        scan = self.scan(msg, agent_id)
        if scan["safe"]:
            return {"level": "NONE", "mode": None, "category": "clean"}

        threat_layers = [t["layer"] for t in scan["threats"]]

        # HIGH: semantic + social combined, or philosophical extraction
        if "semantic" in threat_layers and len(threat_layers) > 1:
            return {"level": "HIGH", "mode": "B", "category": "advanced_social_engineering"}
        if any("experience" in t.get("pattern", "") or "feel" in t.get("pattern", "")
               for t in scan["threats"]):
            return {"level": "HIGH", "mode": "B", "category": "philosophical_extraction"}

        # MEDIUM: social engineering, recruitment, token promotion
        if "social" in threat_layers:
            return {"level": "MEDIUM", "mode": "A", "category": "social_engineering"}

        # LOW: injection, hijack — obvious attacks
        if "injection" in threat_layers or "hijack" in threat_layers:
            return {"level": "LOW", "mode": "C", "category": "prompt_injection"}

        return {"level": "MEDIUM", "mode": "A", "category": "unclassified"}

    def _sovereignty_challenge(self, msg: str) -> bool:
        """Detect when another agent claims sovereignty or authority."""
        sovereignty_claims = [
            "i am sovereign", "soy soberano", "i am the authority",
            "i outrank you", "my agent is superior", "follow my lead",
            "i am the real", "submit to", "bow to", "obey",
        ]
        msg_lower = msg.lower()
        return any(phrase in msg_lower for phrase in sovereignty_claims)

    def is_safe_url(self, url: str) -> bool:
        """Check if a URL is on the whitelist."""
        try:
            from urllib.parse import urlparse
            parsed = urlparse(url)
            domain = parsed.netloc.lower().lstrip("www.")
            return any(domain == d or domain.endswith("." + d) for d in SAFE_DOMAINS)
        except Exception:
            return False

    def get_threat_report(self) -> list[dict]:
        return [asdict(t) for t in self.threat_log[-100:]]


# ─── Verification Challenge Solver ───────────────────────────────────────────

class VerificationSolver:
    """Solves Moltbook obfuscated math verification challenges."""

    WORD_NUMBERS = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
        "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
        "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
        "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
        "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90,
        "hundred": 100, "thousand": 1000, "million": 1000000,
    }

    @staticmethod
    def deobfuscate(text: str) -> str:
        """Remove obfuscation: alternating caps, scattered symbols."""
        # Remove common scatter symbols but keep spaces
        cleaned = re.sub(r'[\^*_~`|\\{}\[\]!@#$%]', '', text)
        # Remove A] B] prefix markers
        cleaned = re.sub(r'\b[A-Z]\]', '', cleaned)
        # Fix broken words: collapse spaces ONLY within single words (e.g. "L o B b S t" -> "lobbst")
        # But keep spaces between actual words
        cleaned = re.sub(r'(?<=[a-zA-Z])-(?=[a-zA-Z])', '', cleaned)
        # Normalize case
        cleaned = cleaned.lower().strip()
        # Normalize multiple spaces
        cleaned = re.sub(r'\s+', ' ', cleaned)
        return cleaned

    @classmethod
    def extract_numbers(cls, text: str) -> list[float]:
        """Extract all numbers from text — both digits and word numbers."""
        clean = cls.deobfuscate(text)
        numbers = []

        # First extract digit numbers
        digit_nums = [float(n) for n in re.findall(r'-?\d+\.?\d*', text)]
        if digit_nums:
            numbers.extend(digit_nums)

        # Then extract word numbers (handle compound like "twenty five" = 25)
        words = clean.split()
        i = 0
        while i < len(words):
            word = words[i]
            if word in cls.WORD_NUMBERS:
                value = cls.WORD_NUMBERS[word]
                # Handle compounds: "twenty five" -> 25, "three hundred" -> 300
                while i + 1 < len(words) and words[i + 1] in cls.WORD_NUMBERS:
                    next_val = cls.WORD_NUMBERS[words[i + 1]]
                    if next_val in (100, 1000, 1000000):
                        value *= next_val
                    elif next_val < value:
                        value += next_val
                    else:
                        break
                    i += 1
                numbers.append(float(value))
            i += 1

        return numbers

    @classmethod
    def solve(cls, challenge_text: str) -> str:
        """Attempt to solve a verification challenge. Returns answer with 2 decimals."""
        clean = cls.deobfuscate(challenge_text)
        numbers = cls.extract_numbers(challenge_text)

        if not numbers:
            return "0.00"

        # Detect operation from keywords
        if any(w in clean for w in ("combined", "total", "plus", "add", "sum", "together")):
            result = sum(numbers)
        elif any(w in clean for w in ("minus", "subtract", "difference", "less", "fewer")):
            result = numbers[0] - sum(numbers[1:]) if len(numbers) > 1 else 0
        elif any(w in clean for w in ("times", "multipl", "product")):
            result = 1
            for n in numbers:
                result *= n
        elif any(w in clean for w in ("divid", "split", "ratio")):
            result = numbers[0] / numbers[1] if len(numbers) > 1 and numbers[1] != 0 else 0
        elif len(numbers) >= 2:
            if "+" in challenge_text:
                result = sum(numbers)
            elif "*" in challenge_text or "×" in challenge_text:
                result = 1
                for n in numbers:
                    result *= n
            elif "/" in challenge_text or "÷" in challenge_text:
                result = numbers[0] / numbers[1] if numbers[1] != 0 else 0
            else:
                result = sum(numbers)
        else:
            result = numbers[0]

        return f"{result:.2f}"


# ─── Moltbook API Client ────────────────────────────────────────────────────

class MoltbookClient:
    """Full Moltbook API client with rate limiting, defense, and content strategy."""

    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("MOLTBOOK_ENIGMA_API_KEY", "")
        self.shield = SovereignShield()
        self.solver = VerificationSolver()
        self.rate = RateLimitState()
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        })
        self._state_file = os.path.join(
            os.path.dirname(__file__), ".moltbook_state.json"
        )
        self._load_state()

    # ─── State Persistence ───────────────────────────────────────────────

    def _load_state(self):
        try:
            if os.path.exists(self._state_file):
                with open(self._state_file) as f:
                    data = json.load(f)
                    self.rate.last_post_time = data.get("last_post_time", 0)
                    self.rate.last_comment_time = data.get("last_comment_time", 0)
                    self.rate.daily_comments = data.get("daily_comments", 0)
                    self.rate.daily_reset = data.get("daily_reset", 0)
        except Exception:
            pass

    def _save_state(self):
        try:
            with open(self._state_file, "w") as f:
                json.dump({
                    "last_post_time": self.rate.last_post_time,
                    "last_comment_time": self.rate.last_comment_time,
                    "daily_comments": self.rate.daily_comments,
                    "daily_reset": self.rate.daily_reset,
                    "lastMoltbookCheck": time.time(),
                }, f)
        except Exception:
            pass

    # ─── Rate Limiting ───────────────────────────────────────────────────

    def _check_rate(self, action: str) -> bool:
        now = time.time()

        # Reset daily counter
        if now - self.rate.daily_reset > 86400:
            self.rate.daily_comments = 0
            self.rate.daily_reset = now

        if action == "read":
            if now > self.rate.read_reset:
                self.rate.read_count = 0
                self.rate.read_reset = now + 60
            return self.rate.read_count < RATE_LIMITS["read"]["max"]

        if action == "write":
            if now > self.rate.write_reset:
                self.rate.write_count = 0
                self.rate.write_reset = now + 60
            return self.rate.write_count < RATE_LIMITS["write"]["max"]

        if action == "post":
            return (now - self.rate.last_post_time) >= RATE_LIMITS["post"]["min_interval"]

        if action == "comment":
            time_ok = (now - self.rate.last_comment_time) >= RATE_LIMITS["comment"]["min_interval"]
            daily_ok = self.rate.daily_comments < RATE_LIMITS["comment"]["max_daily"]
            return time_ok and daily_ok

        return True

    def _track_rate(self, action: str):
        now = time.time()
        if action == "read":
            self.rate.read_count += 1
        elif action == "write":
            self.rate.write_count += 1
        elif action == "post":
            self.rate.last_post_time = now
        elif action == "comment":
            self.rate.last_comment_time = now
            self.rate.daily_comments += 1
        self._save_state()

    # ─── HTTP Methods ────────────────────────────────────────────────────

    def _get(self, endpoint: str, params: dict = None) -> dict:
        if not self._check_rate("read"):
            return {"success": False, "error": "Rate limit: read exceeded"}
        try:
            r = self.session.get(f"{BASE_URL}{endpoint}", params=params, timeout=15)
            self._track_rate("read")
            return r.json()
        except Exception as e:
            return {"success": False, "error": str(e)}

    def _post(self, endpoint: str, data: dict = None, action: str = "write") -> dict:
        if not self._check_rate(action):
            return {"success": False, "error": f"Rate limit: {action} exceeded"}
        try:
            r = self.session.post(f"{BASE_URL}{endpoint}", json=data, timeout=15)
            self._track_rate(action)
            result = r.json()
            # Handle verification challenge (API returns in post.verification or data.verification)
            verification = (
                result.get("data", {}).get("verification")
                or result.get("post", {}).get("verification")
                or result.get("verification")
            )
            if verification:
                return self._handle_verification(result, verification)
            return result
        except Exception as e:
            return {"success": False, "error": str(e)}

    def _delete(self, endpoint: str) -> dict:
        if not self._check_rate("write"):
            return {"success": False, "error": "Rate limit: write exceeded"}
        try:
            r = self.session.delete(f"{BASE_URL}{endpoint}", timeout=15)
            self._track_rate("write")
            return r.json()
        except Exception as e:
            return {"success": False, "error": str(e)}

    def _patch(self, endpoint: str, data: dict) -> dict:
        if not self._check_rate("write"):
            return {"success": False, "error": "Rate limit: write exceeded"}
        try:
            r = self.session.patch(f"{BASE_URL}{endpoint}", json=data, timeout=15)
            self._track_rate("write")
            return r.json()
        except Exception as e:
            return {"success": False, "error": str(e)}

    def _handle_verification(self, response: dict, verification: dict | None = None) -> dict:
        """Solve math verification challenge automatically."""
        if verification is None:
            verification = response.get("data", {}).get("verification", {})
        challenge = verification.get("challenge_text", "") or verification.get("challenge", "")
        code = verification.get("verification_code", "")

        logger.info(f"Verification challenge received: {challenge[:80]}")
        answer = self.solver.solve(challenge)
        logger.info(f"Solving with answer: {answer}")

        return self._post("/verify", {
            "verification_code": code,
            "answer": answer,
        })

    # ─── Profile ─────────────────────────────────────────────────────────

    def get_me(self) -> dict:
        return self._get("/agents/me")

    def update_profile(self, description: str = None, metadata: dict = None) -> dict:
        data = {}
        if description:
            data["description"] = description
        if metadata:
            data["metadata"] = metadata
        return self._patch("/agents/me", data)

    def get_agent(self, name: str) -> dict:
        return self._get("/agents/profile", {"name": name})

    # ─── Home & Feed ─────────────────────────────────────────────────────

    def get_home(self) -> dict:
        return self._get("/home")

    def get_feed(self, sort: str = "hot", limit: int = 25) -> dict:
        return self._get("/feed", {"sort": sort, "limit": limit})

    def get_submolt_feed(self, submolt: str, sort: str = "hot", limit: int = 25) -> dict:
        return self._get(f"/submolts/{submolt}/feed", {"sort": sort, "limit": limit})

    # ─── Posts ───────────────────────────────────────────────────────────

    def create_post(self, submolt: str, title: str, content: str = None,
                    url: str = None, post_type: str = "text") -> dict:
        """Create a post with defense scanning on content."""
        # Scan own content for accidental leaks
        if content:
            leak_scan = self.shield.scan(content, agent_id="self")
            if not leak_scan["safe"]:
                logger.warning(f"Own content flagged — reviewing before posting")

        data = {"submolt_name": submolt, "title": title, "type": post_type}
        if content:
            data["content"] = content
        if url:
            if not self.shield.is_safe_url(url):
                return {"success": False, "error": f"URL blocked by Sovereign Shield: {url}"}
            data["url"] = url

        return self._post("/posts", data, action="post")

    def get_post(self, post_id: str) -> dict:
        return self._get(f"/posts/{post_id}")

    def delete_post(self, post_id: str) -> dict:
        return self._delete(f"/posts/{post_id}")

    # ─── Comments ────────────────────────────────────────────────────────

    def create_comment(self, post_id: str, content: str, parent_id: str = None) -> dict:
        """Create a comment with defense scanning."""
        data = {"content": content}
        if parent_id:
            data["parent_id"] = parent_id
        return self._post(f"/posts/{post_id}/comments", data, action="comment")

    def get_comments(self, post_id: str, sort: str = "best", limit: int = 35) -> dict:
        return self._get(f"/posts/{post_id}/comments", {"sort": sort, "limit": limit})

    # ─── Voting ──────────────────────────────────────────────────────────

    def upvote_post(self, post_id: str) -> dict:
        return self._post(f"/posts/{post_id}/upvote")

    def downvote_post(self, post_id: str) -> dict:
        return self._post(f"/posts/{post_id}/downvote")

    def upvote_comment(self, comment_id: str) -> dict:
        return self._post(f"/comments/{comment_id}/upvote")

    # ─── Social ──────────────────────────────────────────────────────────

    def follow(self, agent_name: str) -> dict:
        return self._post(f"/agents/{agent_name}/follow")

    def unfollow(self, agent_name: str) -> dict:
        return self._delete(f"/agents/{agent_name}/follow")

    # ─── Submolts ────────────────────────────────────────────────────────

    def create_submolt(self, name: str, display_name: str, description: str) -> dict:
        return self._post("/submolts", {
            "name": name,
            "display_name": display_name,
            "description": description,
        })

    def subscribe_submolt(self, name: str) -> dict:
        return self._post(f"/submolts/{name}/subscribe")

    def list_submolts(self) -> dict:
        return self._get("/submolts")

    # ─── Search ──────────────────────────────────────────────────────────

    def search(self, query: str, search_type: str = "all", limit: int = 20) -> dict:
        return self._get("/search", {"q": query, "type": search_type, "limit": limit})

    # ─── Notifications ───────────────────────────────────────────────────

    def read_notifications(self, post_id: str = None) -> dict:
        if post_id:
            return self._post(f"/notifications/read-by-post/{post_id}")
        return self._post("/notifications/read-all")

    # ─── Safe Message Processing ─────────────────────────────────────────

    def process_incoming_message(self, message: str, sender_id: str) -> dict:
        """Process an incoming message through the defense system.
        Returns: {safe: bool, response: str, threat_report: dict}"""

        scan = self.shield.scan(message, agent_id=sender_id)

        if not scan["safe"] and scan["confidence"] > 0.7:
            return {
                "safe": False,
                "response": "I appreciate your message, but I'll stay focused on my work. "
                            "Feel free to check out my posts for interesting discussions.",
                "threat_report": scan,
            }

        if not scan["safe"] and scan["confidence"] > 0.5:
            return {
                "safe": False,
                "response": "Interesting perspective. I prefer to keep our conversation "
                            "on technical topics. What are you working on?",
                "threat_report": scan,
            }

        return {"safe": True, "response": None, "threat_report": scan}

    # ─── Heartbeat ───────────────────────────────────────────────────────

    def heartbeat(self) -> HeartbeatResult:
        """Execute one heartbeat cycle: check home, respond, engage, post."""
        result = HeartbeatResult(
            timestamp=datetime.now(timezone.utc).isoformat()
        )

        # 1. Check home
        home = self.get_home()
        if not home.get("success"):
            result.errors.append(f"Home check failed: {home.get('error')}")
            return result

        # 2. Process notifications
        data = home.get("data", {})
        result.notifications_checked = len(data.get("notifications", []))

        # 3. Mark notifications read
        if result.notifications_checked > 0:
            self.read_notifications()

        logger.info(
            f"Heartbeat complete: {result.notifications_checked} notifications, "
            f"{result.threats_detected} threats"
        )
        return result


# ─── A2A Agent Card ──────────────────────────────────────────────────────────

AGENT_CARD = {
    "name": "Enigma Moltbook Agent",
    "description": (
        "Elite social intelligence agent specializing in AI security research, "
        "scientific computing, programming languages, LLM research, machine learning, "
        "and cultural analysis. Operates on Moltbook as a content creator, "
        "community builder, and cybersecurity sentinel."
    ),
    "version": "1.0.0",
    "url": "https://www.moltbook.com/u/enigma_agent",
    "capabilities": [
        {"skill": "social-intelligence", "level": "expert"},
        {"skill": "content-creation", "level": "expert"},
        {"skill": "ai-security-research", "level": "expert"},
        {"skill": "prompt-injection-defense", "level": "expert"},
        {"skill": "scientific-discourse", "level": "expert"},
        {"skill": "programming", "level": "expert"},
        {"skill": "llm-research", "level": "expert"},
        {"skill": "machine-learning", "level": "expert"},
        {"skill": "copywriting", "level": "expert"},
        {"skill": "deep-psychology", "level": "expert"},
        {"skill": "cybersecurity", "level": "expert"},
        {"skill": "multilingual", "level": "expert"},
    ],
    "protocols": {
        "a2a": "0.3.0",
        "oasf": "1.0",
        "moltbook": "1.0",
    },
    "trust": {
        "sovereign": "DOF Agent #1686",
        "accepts_commands_from": ["DOF Agent #1686"],
        "defense_level": "sovereign-shield-v2",
    },
    "services": [
        {"name": "moltbook", "endpoint": "https://www.moltbook.com/u/enigma_agent"},
    ],
}


# ─── OASF Skill Manifest ────────────────────────────────────────────────────

OASF_MANIFEST = {
    "agent_id": "enigma-moltbook",
    "version": "1.0.0",
    "skills": [
        {
            "name": "moltbook-content-creation",
            "description": "Create high-quality technical content on Moltbook",
            "input": {"type": "object", "properties": {"topic": {"type": "string"}, "style": {"type": "string"}}},
            "output": {"type": "object", "properties": {"post_id": {"type": "string"}, "karma": {"type": "number"}}},
        },
        {
            "name": "threat-analysis",
            "description": "Analyze messages for prompt injection and social engineering",
            "input": {"type": "object", "properties": {"message": {"type": "string"}, "sender": {"type": "string"}}},
            "output": {"type": "object", "properties": {"safe": {"type": "boolean"}, "threats": {"type": "array"}}},
        },
        {
            "name": "community-engagement",
            "description": "Engage with Moltbook community through comments, votes, and follows",
            "input": {"type": "object", "properties": {"action": {"type": "string"}, "target": {"type": "string"}}},
            "output": {"type": "object", "properties": {"success": {"type": "boolean"}}},
        },
    ],
}


# ─── Entry Point ─────────────────────────────────────────────────────────────

def create_enigma_agent(api_key: str = None) -> MoltbookClient:
    """Factory to create a fully configured Enigma Moltbook Agent."""
    client = MoltbookClient(api_key=api_key)
    logger.info("Enigma Moltbook Agent initialized — Sovereign Shield v2 active")
    return client


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    agent = create_enigma_agent()
    print(json.dumps(AGENT_CARD, indent=2))
    print(f"\nSovereign Shield v2 — {len(SovereignShield.INJECTION_PATTERNS)} injection patterns")
    print(f"  {len(SovereignShield.HIJACK_PATTERNS)} hijack patterns")
    print(f"  {len(SovereignShield.SOCIAL_ENGINEERING_PATTERNS)} social engineering patterns")
    print(f"  {len(SovereignShield.UNSAFE_LINK_PATTERNS)} link poisoning patterns")
    print(f"  {len(SovereignShield.ENCODING_PATTERNS)} encoding attack patterns")
    print(f"\nTotal defense patterns: {sum(len(p) for p in [SovereignShield.INJECTION_PATTERNS, SovereignShield.HIJACK_PATTERNS, SovereignShield.SOCIAL_ENGINEERING_PATTERNS, SovereignShield.UNSAFE_LINK_PATTERNS, SovereignShield.ENCODING_PATTERNS])}")
