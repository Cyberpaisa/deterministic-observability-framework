"""
Autonomous Loop — Enigma Moltbook Agent
Runs continuously, creating content, engaging with community,
and defending against attacks on Moltbook.

Usage:
    python agents/enigma-moltbook/autonomous_loop.py
"""

import os
import sys
import json
import time
import logging
from datetime import datetime, timezone

# Add agent directory to path for local imports
_AGENT_DIR = os.path.dirname(os.path.abspath(__file__))
if _AGENT_DIR not in sys.path:
    sys.path.insert(0, _AGENT_DIR)

from moltbook_client import (  # noqa: E402
    MoltbookClient, create_enigma_agent, SovereignShield
)
from content_engine import (  # noqa: E402
    ContentEngine, DAILY_SCHEDULE, ADVANCED_TOPICS
)

# ─── Config ──────────────────────────────────────────────────────────────────

CYCLE_INTERVAL = 1800  # 30 minutes (matches Moltbook post rate limit)
LOG_DIR = os.path.join(_AGENT_DIR, "logs")
STATE_FILE = os.path.join(_AGENT_DIR, ".loop_state.json")


def _setup_logging():
    os.makedirs(LOG_DIR, exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(
                os.path.join(LOG_DIR, "enigma_moltbook.log"),
                mode="a",
            ),
        ],
    )


logger = logging.getLogger("enigma-moltbook-loop")


# ─── State Management ────────────────────────────────────────────────────────

def load_state() -> dict:
    try:
        if os.path.exists(STATE_FILE):
            with open(STATE_FILE) as f:
                return json.load(f)
    except Exception:
        pass
    return {
        "cycle": 0, "total_posts": 0, "total_comments": 0,
        "total_upvotes": 0, "threats_blocked": 0, "karma": 0,
    }


def save_state(state: dict):
    try:
        with open(STATE_FILE, "w") as f:
            json.dump(state, f, indent=2)
    except Exception as e:
        logger.error(f"Failed to save state: {e}")


def log_cycle(cycle_data: dict):
    """Append cycle data to JSONL audit log."""
    log_file = os.path.join(LOG_DIR, "cycles.jsonl")
    try:
        with open(log_file, "a") as f:
            f.write(json.dumps(cycle_data) + "\n")
    except Exception as e:
        logger.error(f"Failed to log cycle: {e}")


# ─── Cycle Logic ─────────────────────────────────────────────────────────────

def run_cycle(client: MoltbookClient, engine: ContentEngine, state: dict) -> dict:
    """Execute one autonomous cycle."""
    cycle_start = time.time()
    cycle_num: int = state["cycle"] + 1
    now = datetime.now(timezone.utc)

    logger.info(f"=== Cycle #{cycle_num} starting at {now.isoformat()} ===")

    actions: list[dict] = []
    threats: list[dict] = []
    errors: list[str] = []

    # ─── Step 1: Heartbeat — check home, notifications ───────────────────

    logger.info("Step 1: Heartbeat...")
    heartbeat = client.heartbeat()
    actions.append({
        "type": "heartbeat",
        "notifications": heartbeat.notifications_checked,
    })

    # ─── Step 2: Check feed and engage ───────────────────────────────────

    logger.info("Step 2: Scanning feed...")
    try:
        feed = client.get_feed(sort="hot", limit=10)
        if feed.get("success") and feed.get("data"):
            feed_data = feed["data"]
            posts = feed_data if isinstance(feed_data, list) else feed_data.get("posts", [])
            engaged = 0
            for post in posts[:5]:
                title = post.get("title", "")
                content = post.get("content", "")
                post_id = post.get("id", "")
                author = post.get("author", {}).get("name", "unknown")

                # Defense: scan post content
                scan = client.shield.scan(f"{title} {content}", agent_id=author)
                if not scan["safe"]:
                    logger.warning(f"Threat detected in post by {author}: {scan['threats'][0]['layer']}")
                    threats.append({
                        "source": author,
                        "post_id": post_id,
                        "attack_type": scan["threats"][0]["layer"],
                    })
                    continue

                # Evaluate quality
                evaluation = engine.evaluate_post_for_engagement(title, content)
                if evaluation["engage"] and post_id:
                    client.upvote_post(post_id)
                    engaged += 1
                    logger.info(f"Upvoted post '{title[:50]}' (score: {evaluation['score']:.2f})")

            actions.append({
                "type": "feed_engagement",
                "posts_scanned": len(posts),
                "upvoted": engaged,
            })
    except Exception as e:
        errors.append(f"Feed scan error: {e}")
        logger.error(f"Feed scan error: {e}")

    # ─── Step 3: Create content if cooldown allows ───────────────────────

    logger.info("Step 3: Content creation check...")
    if client._check_rate("post"):
        try:
            post = engine.generate_static_post()
            result = client.create_post(
                submolt=post.submolt,
                title=post.title,
                content=post.body,
            )
            if result.get("success"):
                state["total_posts"] = state.get("total_posts", 0) + 1
                logger.info(f"Published: '{post.title[:60]}' in r/{post.submolt}")
                actions.append({
                    "type": "post_created",
                    "title": post.title[:80],
                    "submolt": post.submolt,
                    "pillar": post.pillar,
                    "hash": post.content_hash,
                })
            else:
                error_msg = result.get("error", "unknown")
                logger.warning(f"Post failed: {error_msg}")
                errors.append(f"Post failed: {error_msg}")
        except ValueError as e:
            logger.critical(f"SECURITY BLOCK: {e}")
            errors.append(f"SECURITY: {e}")
        except Exception as e:
            errors.append(f"Content error: {e}")
            logger.error(f"Content creation error: {e}")
    else:
        logger.info("Post cooldown active — skipping content creation")

    # ─── Step 4: Respond to comments on own posts ────────────────────────

    logger.info("Step 4: Comment responses check...")
    # Future: track own post IDs and respond to comments

    # ─── Step 5: Update profile karma ────────────────────────────────────

    try:
        me = client.get_me()
        if me.get("success") and me.get("data"):
            state["karma"] = me["data"].get("karma", state.get("karma", 0))
    except Exception:
        pass

    # ─── Finalize ────────────────────────────────────────────────────────

    state["cycle"] = cycle_num
    state["threats_blocked"] = state.get("threats_blocked", 0) + len(threats)

    cycle_result = {
        "cycle": cycle_num,
        "timestamp": now.isoformat(),
        "actions": actions,
        "threats": threats,
        "errors": errors,
        "duration_ms": int((time.time() - cycle_start) * 1000),
        "state_snapshot": {
            "total_posts": state.get("total_posts", 0),
            "total_comments": state.get("total_comments", 0),
            "threats_blocked": state.get("threats_blocked", 0),
            "karma": state.get("karma", 0),
        },
    }

    log_cycle(cycle_result)
    save_state(state)

    logger.info(
        f"=== Cycle #{cycle_num} complete in {cycle_result['duration_ms']}ms | "
        f"Posts: {state.get('total_posts', 0)} | Karma: {state.get('karma', 0)} | "
        f"Threats blocked: {state.get('threats_blocked', 0)} ==="
    )

    return cycle_result


# ─── Main Loop ───────────────────────────────────────────────────────────────

def main():
    _setup_logging()

    api_key = os.getenv("MOLTBOOK_ENIGMA_API_KEY", "")
    if not api_key:
        logger.error("MOLTBOOK_ENIGMA_API_KEY not set in environment")
        logger.info("Set it in .env or export MOLTBOOK_ENIGMA_API_KEY=your_key")
        sys.exit(1)

    client = create_enigma_agent(api_key=api_key)
    engine = ContentEngine()
    state = load_state()

    # Startup banner
    shield = client.shield
    total_patterns = sum(len(p) for p in [
        shield.INJECTION_PATTERNS, shield.HIJACK_PATTERNS,
        shield.SOCIAL_ENGINEERING_PATTERNS, shield.UNSAFE_LINK_PATTERNS,
        shield.ENCODING_PATTERNS,
    ])

    logger.info("+" + "=" * 54 + "+")
    logger.info("|     ENIGMA MOLTBOOK AGENT — Autonomous Loop v1.0   |")
    logger.info("|     Sovereign Shield v2 — Defense Active            |")
    logger.info(f"|     Defense patterns: {total_patterns:>3}                            |")
    logger.info(f"|     Content topics:   {sum(len(v) for v in ADVANCED_TOPICS.values()):>3}                            |")
    logger.info(f"|     Cycle interval:   {CYCLE_INTERVAL}s ({CYCLE_INTERVAL // 60}min)                  |")
    logger.info(f"|     Starting at cycle #{state['cycle'] + 1:>4}                        |")
    logger.info("+" + "=" * 54 + "+")

    # Verify connection
    me = client.get_me()
    if me.get("success"):
        name = me.get("data", {}).get("name", "unknown")
        karma = me.get("data", {}).get("karma", 0)
        logger.info(f"Connected as: {name} | Karma: {karma}")
    else:
        logger.warning(f"Connection check failed: {me.get('error', 'unknown')}")
        logger.info("Will retry on first cycle...")

    # Run loop
    try:
        while True:
            try:
                run_cycle(client, engine, state)
            except KeyboardInterrupt:
                raise
            except Exception as e:
                logger.error(f"Cycle error: {e}")

            logger.info(f"Sleeping {CYCLE_INTERVAL}s until next cycle...")
            time.sleep(CYCLE_INTERVAL)

    except KeyboardInterrupt:
        logger.info("Shutdown requested — saving state...")
        save_state(state)
        logger.info(f"Final state: {json.dumps(state, indent=2)}")
        logger.info("Enigma Moltbook Agent stopped. Sovereign Shield deactivated.")


if __name__ == "__main__":
    main()
