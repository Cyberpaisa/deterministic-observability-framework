import sqlite3
import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any

class LocalMemory:
    def __init__(self, db_path: str = "memory/chat_history.db"):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS messages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    role TEXT NOT NULL,
                    content TEXT NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    metadata TEXT
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS agent_status (
                    agent_id TEXT PRIMARY KEY,
                    status TEXT NOT NULL,
                    last_seen DATETIME DEFAULT CURRENT_TIMESTAMP,
                    metrics TEXT
                )
            """)
            conn.commit()

    async def add_message(self, role: str, content: str, metadata: Dict = None):
        meta_json = json.dumps(metadata) if metadata else None
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "INSERT INTO messages (role, content, metadata) VALUES (?, ?, ?)",
                (role, content, meta_json)
            )
            conn.commit()

    async def get_recent_messages(self, limit: int = 20) -> List[Dict[str, Any]]:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute(
                "SELECT role, content, timestamp, metadata FROM messages ORDER BY id DESC LIMIT ?",
                (limit,)
            )
            rows = cursor.fetchall()
            messages = []
            for row in reversed(rows):
                messages.append({
                    "role": row["role"],
                    "content": row["content"],
                    "timestamp": row["timestamp"],
                    "metadata": json.loads(row["metadata"]) if row["metadata"] else {}
                })
            return messages

    async def update_agent_status(self, agent_id: str, status: str, metrics: Dict = None):
        metrics_json = json.dumps(metrics) if metrics else None
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                INSERT OR REPLACE INTO agent_status (agent_id, status, last_seen, metrics)
                VALUES (?, ?, CURRENT_TIMESTAMP, ?)
            """, (agent_id, status, metrics_json))
            conn.commit()

    async def get_all_agent_status(self) -> List[Dict[str, Any]]:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute("SELECT agent_id, status, last_seen, metrics FROM agent_status")
            rows = cursor.fetchall()
            return [dict(row) for row in rows]

# Singleton instance
_instance = None
def get_local_memory():
    global _instance
    if _instance is None:
        _instance = LocalMemory()
    return _instance
