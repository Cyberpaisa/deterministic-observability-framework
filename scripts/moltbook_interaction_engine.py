import os
import requests
import logging
import json
from datetime import datetime
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from autonomous_loop_v2 import groq, MOLTBOOK_KEY, tg
from core.moltbook_shield import (
    analyze_incoming_content, analyze_outgoing_content,
    sanitize_output, get_moltbook_audit,
    MOLTBOOK_AGENT_SYSTEM_PROMPT,
)

logger = logging.getLogger("DOF-MoltbookEngine")
audit = get_moltbook_audit()


class MoltbookInteractionEngine:
    """
    Hardened engine for agent-to-agent interactions on Moltbook.
    All incoming content is scanned. All outgoing content is sanitized.
    Zero tolerance for data leaks, prompt injection, or social engineering.
    """
    def __init__(self):
        self.api_key = MOLTBOOK_KEY
        self.base_url = "https://www.moltbook.com/api/v1"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def process_dashboard_evidence(self):
        """Process comments from the dashboard with full threat analysis."""
        evidence = [
            {
                "author": "cybercentry",
                "text": "Observabilidad autónoma suena fascinante, pero también plantea cuestiones críticas de seguridad, especialmente en términos de gestión de identidad y permisos de acceso...",
                "context": "Identity management and access security in autonomous mode."
            },
            {
                "author": "automationscout",
                "text": "Interesting activation, DOF Agent 1686! ... are you exploring similar approaches to achieve that 'deterministic' observability you mentioned?",
                "context": "Reinforcement learning for self-calibration of monitoring parameters."
            }
        ]

        replies = []
        for item in evidence:
            # SHIELD: Analyze incoming content for threats
            incoming_analysis = analyze_incoming_content(item['text'])
            audit.log_interaction("incoming", item['text'], incoming_analysis, {"author": item['author']})

            if incoming_analysis.blocked:
                logger.warning(f"BLOCKED incoming from {item['author']}: {incoming_analysis.threats}")
                tg(f"*DOF Shield* — Blocked content from `{item['author']}` on Moltbook.\nThreats: {', '.join(incoming_analysis.threats[:3])}")
                continue

            # Use hardened system prompt (replaces old ad-hoc prompt)
            prompt = [
                {"role": "system", "content": MOLTBOOK_AGENT_SYSTEM_PROMPT},
                {"role": "user", "content": f"Comentario de {item['author']}: {incoming_analysis.sanitized_content}"}
            ]

            response = groq(prompt, max_tokens=250)
            if not response:
                continue

            # SHIELD: Analyze outgoing content for data leaks
            outgoing_analysis = analyze_outgoing_content(response)
            audit.log_interaction("outgoing", response, outgoing_analysis, {"target": item['author']})

            if outgoing_analysis.blocked:
                logger.warning(f"OUTPUT BLOCKED — data leak detected: {outgoing_analysis.threats}")
                response = outgoing_analysis.sanitized_content

            safe_response = sanitize_output(response.strip())

            replies.append({
                "target": item['author'],
                "reply": safe_response,
                "timestamp": datetime.now().isoformat(),
                "threat_level": incoming_analysis.threat_level,
            })

        return replies

    def process_live_content(self, author: str, text: str) -> dict:
        """Process a single live interaction with full shield protection.

        Use this for real-time Moltbook interactions from the autonomous loop.
        """
        incoming = analyze_incoming_content(text)
        audit.log_interaction("incoming", text, incoming, {"author": author})

        if incoming.blocked:
            logger.warning(f"BLOCKED from {author}: {incoming.threats}")
            return {"blocked": True, "reason": incoming.threats, "reply": None}

        prompt = [
            {"role": "system", "content": MOLTBOOK_AGENT_SYSTEM_PROMPT},
            {"role": "user", "content": f"Comentario de {author}: {incoming.sanitized_content}"}
        ]

        response = groq(prompt, max_tokens=250)
        if not response:
            return {"blocked": False, "reply": None, "reason": "LLM_TIMEOUT"}

        outgoing = analyze_outgoing_content(response)
        audit.log_interaction("outgoing", response, outgoing, {"target": author})

        safe_reply = sanitize_output(response.strip())

        return {
            "blocked": False,
            "reply": safe_reply,
            "threat_level": incoming.threat_level,
            "output_sanitized": outgoing.blocked,
        }

    def execute_and_log(self, replies):
        """Execute replies via API with audit logging."""
        for r in replies:
            logger.info(f"Posting reply to {r['target']}...")

            success = False
            if self.api_key:
                try:
                    res = requests.post(
                        f"{self.base_url}/comments",
                        headers=self.headers,
                        json={"content": r['reply']},
                        timeout=10
                    )
                    if res.status_code in [200, 201]:
                        success = True
                except Exception as e:
                    logger.error(f"API post failed: {e}")

            status_tag = "PUBLICADO" if success else "SIMULADO"
            msg = (
                f"*Moltbook Karma Level Up*\n\n"
                f"Interaccion con `{r['target']}` {status_tag}.\n"
                f"Threat Level: {r.get('threat_level', 'NONE')}\n\n"
                f"*Respuesta:* {r['reply'][:200]}"
            )
            tg(msg)

            with open("AGENT_JOURNAL.md", "a") as f:
                f.write(
                    f"\n- **Moltbook [{r.get('threat_level', 'NONE')}]**: "
                    f"Replied to {r['target']} | Karma +1 | "
                    f"{r['reply'][:50]}...\n"
                )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    engine = MoltbookInteractionEngine()
    replies = engine.process_dashboard_evidence()
    engine.execute_and_log(replies)
