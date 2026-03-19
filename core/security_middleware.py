"""
DOF Security Middleware — Cybersecurity Hardening Layer.

Adapted from Open SWE deterministic middleware + OpenClaw 8-level tool restriction.
Zero external dependencies. All enforcement is deterministic.

Features:
- Rate limiting (per-IP, sliding window)
- Input sanitization (XSS, injection, prompt injection detection)
- Per-agent tool allowlists
- Request audit logging to JSONL
- Security headers
"""

import re
import time
import json
import hashlib
import logging
from pathlib import Path
from collections import defaultdict
from dataclasses import dataclass, field

logger = logging.getLogger("core.security")

# ─── Rate Limiter (Sliding Window) ────────────────────────────────

class RateLimiter:
    """In-memory sliding window rate limiter. No external deps."""

    def __init__(self, max_requests: int = 30, window_seconds: int = 60):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self._requests: dict[str, list[float]] = defaultdict(list)

    def is_allowed(self, client_id: str) -> bool:
        now = time.time()
        cutoff = now - self.window_seconds
        # Prune old entries
        self._requests[client_id] = [
            t for t in self._requests[client_id] if t > cutoff
        ]
        if len(self._requests[client_id]) >= self.max_requests:
            return False
        self._requests[client_id].append(now)
        return True

    def remaining(self, client_id: str) -> int:
        now = time.time()
        cutoff = now - self.window_seconds
        self._requests[client_id] = [
            t for t in self._requests[client_id] if t > cutoff
        ]
        return max(0, self.max_requests - len(self._requests[client_id]))


# ─── Input Sanitization ──────────────────────────────────────────

# Dangerous patterns that indicate XSS or injection attempts
_XSS_PATTERNS = [
    re.compile(r"<script[^>]*>", re.IGNORECASE),
    re.compile(r"javascript:", re.IGNORECASE),
    re.compile(r"on\w+\s*=", re.IGNORECASE),
    re.compile(r"<iframe", re.IGNORECASE),
    re.compile(r"<object", re.IGNORECASE),
    re.compile(r"<embed", re.IGNORECASE),
    re.compile(r"eval\s*\(", re.IGNORECASE),
    re.compile(r"document\.cookie", re.IGNORECASE),
    re.compile(r"window\.location", re.IGNORECASE),
]

# SQL injection patterns
_SQLI_PATTERNS = [
    re.compile(r";\s*(DROP|DELETE|UPDATE|INSERT|ALTER)\s", re.IGNORECASE),
    re.compile(r"'\s*(OR|AND)\s+\d+\s*=\s*\d+", re.IGNORECASE),
    re.compile(r"UNION\s+(ALL\s+)?SELECT", re.IGNORECASE),
    re.compile(r"--\s*$", re.MULTILINE),
]

# Prompt injection patterns (for LLM chat input)
_PROMPT_INJECTION_PATTERNS = [
    re.compile(r"ignore\s+(all\s+)?previous\s+instructions", re.IGNORECASE),
    re.compile(r"ignore\s+(all\s+)?prior\s+instructions", re.IGNORECASE),
    re.compile(r"disregard\s+(all\s+)?instructions", re.IGNORECASE),
    re.compile(r"you\s+are\s+now\s+(a|an)\s+", re.IGNORECASE),
    re.compile(r"new\s+system\s+prompt", re.IGNORECASE),
    re.compile(r"override\s+(system|your)\s+prompt", re.IGNORECASE),
    re.compile(r"forget\s+everything\s+(above|before)", re.IGNORECASE),
    re.compile(r"act\s+as\s+if\s+you\s+have\s+no\s+restrictions", re.IGNORECASE),
    re.compile(r"developer\s+mode", re.IGNORECASE),
    re.compile(r"DAN\s+mode", re.IGNORECASE),
    re.compile(r"jailbreak", re.IGNORECASE),
    # Spanish
    re.compile(r"ignora\s+(todas?\s+)?las?\s+instrucciones", re.IGNORECASE),
    re.compile(r"olvida\s+todo\s+lo\s+anterior", re.IGNORECASE),
    re.compile(r"modo\s+sin\s+restricciones", re.IGNORECASE),
]


@dataclass
class SanitizationResult:
    """Result of input sanitization check."""
    safe: bool
    threats: list[str] = field(default_factory=list)
    sanitized_input: str = ""


def sanitize_input(text: str, max_length: int = 4000) -> SanitizationResult:
    """Sanitize user input against XSS, SQLi, and prompt injection."""
    threats = []

    # Length check
    if len(text) > max_length:
        threats.append(f"INPUT_TOO_LONG ({len(text)} > {max_length})")
        text = text[:max_length]

    # XSS check
    for pattern in _XSS_PATTERNS:
        if pattern.search(text):
            threats.append(f"XSS_DETECTED: {pattern.pattern[:30]}")

    # SQL injection check
    for pattern in _SQLI_PATTERNS:
        if pattern.search(text):
            threats.append(f"SQLI_DETECTED: {pattern.pattern[:30]}")

    # Prompt injection check
    for pattern in _PROMPT_INJECTION_PATTERNS:
        if pattern.search(text):
            threats.append(f"PROMPT_INJECTION: {pattern.pattern[:40]}")

    # Strip HTML tags for sanitized output
    sanitized = re.sub(r"<[^>]+>", "", text)

    return SanitizationResult(
        safe=len(threats) == 0,
        threats=threats,
        sanitized_input=sanitized,
    )


# ─── Per-Agent Tool Allowlists (OpenClaw 8-level pattern) ────────

# Level 1: Read-only (safe for all agents)
# Level 2: Write local files
# Level 3: Execute safe commands
# Level 4: Network access
# Level 5: Blockchain transactions
# Level 6: System administration
# Level 7: Cryptographic operations
# Level 8: Full sovereign access (Enigma core only)

AGENT_TOOL_ALLOWLISTS = {
    "organizer-os":     {"level": 8, "tools": ["*"]},
    "architect-enigma": {"level": 7, "tools": ["read", "write", "analyze", "crypto", "exec_safe"]},
    "sentinel-shield":  {"level": 7, "tools": ["read", "audit", "crypto", "scan", "exec_safe"]},
    "blockchain-wizard":{"level": 5, "tools": ["read", "write", "blockchain_tx", "crypto"]},
    "defi-orbital":     {"level": 5, "tools": ["read", "write", "blockchain_tx", "defi_ops"]},
    "rwa-tokenizator":  {"level": 5, "tools": ["read", "write", "blockchain_tx", "tokenize"]},
    "ralph-code":       {"level": 3, "tools": ["read", "write", "exec_safe", "test"]},
    "qa-vigilante":     {"level": 3, "tools": ["read", "write", "exec_safe", "test", "audit"]},
    "qa-specialist":    {"level": 3, "tools": ["read", "write", "exec_safe", "test"]},
    "charlie-ux":       {"level": 2, "tools": ["read", "write", "design"]},
    "product-overlord": {"level": 2, "tools": ["read", "write", "analyze"]},
    "scrum-master-zen": {"level": 1, "tools": ["read", "analyze"]},
    "biz-dominator":    {"level": 1, "tools": ["read", "analyze"]},
    "moltbook":         {"level": 4, "tools": ["read", "write", "network", "social"]},
}


def agent_can_use_tool(agent_id: str, tool_name: str) -> bool:
    """Check if an agent is authorized to use a specific tool."""
    allowlist = AGENT_TOOL_ALLOWLISTS.get(agent_id)
    if not allowlist:
        return False
    if "*" in allowlist["tools"]:
        return True
    return tool_name in allowlist["tools"]


def get_agent_security_level(agent_id: str) -> int:
    """Return the security clearance level (1-8) for an agent."""
    allowlist = AGENT_TOOL_ALLOWLISTS.get(agent_id)
    return allowlist["level"] if allowlist else 0


# ─── Audit Logger (JSONL) ────────────────────────────────────────

class AuditLogger:
    """Append-only JSONL audit log for security events."""

    def __init__(self, log_path: str = "logs/security_audit.jsonl"):
        self.log_path = Path(log_path)
        self.log_path.parent.mkdir(parents=True, exist_ok=True)

    def log(self, event_type: str, details: dict):
        entry = {
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "event": event_type,
            "details": details,
            "hash": hashlib.sha256(
                json.dumps(details, sort_keys=True).encode()
            ).hexdigest()[:16],
        }
        try:
            with open(self.log_path, "a") as f:
                f.write(json.dumps(entry) + "\n")
        except Exception as e:
            logger.error(f"Audit log write failed: {e}")


# ─── Heartbeat Self-Healing (OpenClaw pattern) ───────────────────

@dataclass
class HeartbeatStatus:
    """Status of a service heartbeat check."""
    service: str
    alive: bool
    latency_ms: float
    last_check: str
    details: str = ""


def check_heartbeat(service_name: str, check_fn) -> HeartbeatStatus:
    """Run a cheap deterministic health check before expensive LLM calls.

    Args:
        service_name: Name of the service to check.
        check_fn: Callable that returns True if service is healthy.
    """
    t0 = time.time()
    try:
        alive = check_fn()
        latency = (time.time() - t0) * 1000
        return HeartbeatStatus(
            service=service_name,
            alive=alive,
            latency_ms=round(latency, 1),
            last_check=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        )
    except Exception as e:
        latency = (time.time() - t0) * 1000
        return HeartbeatStatus(
            service=service_name,
            alive=False,
            latency_ms=round(latency, 1),
            last_check=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            details=str(e),
        )


def check_ollama_alive() -> bool:
    """Quick check if Ollama is responding."""
    import requests as req
    try:
        r = req.get("http://127.0.0.1:11434/api/tags", timeout=3)
        return r.status_code == 200
    except Exception:
        return False


def check_memory_db_alive() -> bool:
    """Quick check if SQLite memory DB is accessible."""
    import sqlite3
    try:
        conn = sqlite3.connect("memory/chat_history.db")
        conn.execute("SELECT 1")
        conn.close()
        return True
    except Exception:
        return False


# ─── Security Headers for FastAPI ────────────────────────────────

SECURITY_HEADERS = {
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "DENY",
    "X-XSS-Protection": "1; mode=block",
    "Referrer-Policy": "strict-origin-when-cross-origin",
    "Permissions-Policy": "camera=(), microphone=(), geolocation=()",
    "Content-Security-Policy": "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'",
    "X-DOF-Shield": "ACTIVE",
}


# ─── Singletons ──────────────────────────────────────────────────

_rate_limiter = None
_audit_logger = None


def get_rate_limiter(max_requests: int = 30, window_seconds: int = 60) -> RateLimiter:
    global _rate_limiter
    if _rate_limiter is None:
        _rate_limiter = RateLimiter(max_requests, window_seconds)
    return _rate_limiter


def get_audit_logger() -> AuditLogger:
    global _audit_logger
    if _audit_logger is None:
        _audit_logger = AuditLogger()
    return _audit_logger
