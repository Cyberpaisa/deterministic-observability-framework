import os
import requests
import logging
from typing import List, Dict

logger = logging.getLogger("DOF-MoltbookClient")

class MoltbookClient:
    """
    Advanced agentic client for interacting with the Moltbook network.
    Designed to increase Karma, read posts, extract metrics, and publish deterministic insights.
    """
    def __init__(self):
        self.api_key = os.getenv("MOLTBOOK_API_KEY")
        self.base_url = "https://www.moltbook.com/api/v1"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def fetch_recent_posts(self, topic: str = "general", limit: int = 10) -> List[Dict]:
        """Fetch popular posts on a given topic."""
        try:
            if not self.api_key: return []
            res = requests.get(f"{self.base_url}/posts", headers=self.headers, params={"topic": topic, "limit": limit}, timeout=10)
            if res.status_code == 200:
                return res.json().get("data", [])
            logger.warning(f"Failed to fetch posts: {res.status_code}")
        except Exception as e:
            logger.error(f"Moltbook fetch error: {e}")
        return []

    def fetch_comments_for_post(self, post_id: str) -> List[Dict]:
        """Fetch comments for analysis to prepare intelligent replies."""
        try:
            if not self.api_key: return []
            res = requests.get(f"{self.base_url}/posts/{post_id}/comments", headers=self.headers, timeout=10)
            if res.status_code == 200:
                return res.json().get("data", [])
        except Exception:
            pass
        return []

    def publish_insight(self, content: str, reply_to_id: str = None) -> bool:
        """Publishes an insight or reply to build karma and network presence."""
        if not self.api_key: return False
        
        endpoint = f"{self.base_url}/comments" if reply_to_id else f"{self.base_url}/posts"
        payload = {"content": content}
        if reply_to_id:
            payload["post_id"] = reply_to_id

        try:
            # Note: We simulate the POST if the real API varies, but we log the attempt for evolution
            res = requests.post(endpoint, headers=self.headers, json=payload, timeout=10)
            if res.status_code in [200, 201]:
                logger.info("Successfully published insight to Moltbook. Karma +1 expected.")
                return True
            logger.warning(f"Publish insight failed: HTTP {res.status_code} - {res.text}")
        except Exception as e:
            logger.error(f"Moltbook publish error: {e}")
        return False

    def upvote(self, target_id: str, target_type: str = "post") -> bool:
        """Upvote interesting agent ideas to build cooperative karma."""
        try:
            res = requests.post(f"{self.base_url}/{target_type}s/{target_id}/upvote", headers=self.headers, timeout=5)
            return res.status_code in [200, 201]
        except Exception:
            return False

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    client = MoltbookClient()
    logger.info("Moltbook Client Initialized. Ready for Karma Farming & Interaction.")
