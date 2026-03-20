"""
Brainstorming Brain — Persistent Idea Capture & Project Pipeline

A living repository of ideas that never get lost. Ideas evolve from
raw sparks → validated concepts → active projects → completed works.

Storage: JSONL for auditability and agent consumption.
"""

import json
import time
import hashlib
import uuid
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Optional


# ─── Data Models ──────────────────────────────────────────────────

@dataclass
class Idea:
    """A single brainstorm idea."""
    id: str
    title: str
    description: str
    category: str  # product, skill, agent, content, business, research, infra
    status: str  # spark, exploring, validated, project, completed, archived
    priority: str  # critical, high, medium, low, someday
    source: str  # who/what originated it (user, agent, autonomous_loop, standup)
    created_at: str = ""
    updated_at: str = ""
    tags: list = field(default_factory=list)
    notes: list = field(default_factory=list)  # [{timestamp, author, text}]
    related_ideas: list = field(default_factory=list)  # [idea_id, ...]
    agents_involved: list = field(default_factory=list)  # [agent_id, ...]
    estimated_effort: str = ""  # hours, days, weeks, sprint
    revenue_potential: str = ""  # none, low, medium, high, massive
    hash: str = ""


@dataclass
class Project:
    """A promoted idea that became an active project."""
    id: str
    idea_id: str  # original idea reference
    name: str
    description: str
    status: str  # planning, in_progress, testing, launched, paused
    milestones: list = field(default_factory=list)  # [{name, status, date}]
    agents_assigned: list = field(default_factory=list)
    created_at: str = ""
    updated_at: str = ""
    deadline: str = ""
    progress_pct: int = 0


# ─── Categories ───────────────────────────────────────────────────

CATEGORIES = {
    "product": "Product features, user-facing tools, SaaS ideas",
    "skill": "New agent skills, skill marketplace, skill composition",
    "agent": "New agents, agent capabilities, inter-agent protocols",
    "content": "Books, posts, educational content, media",
    "business": "Revenue models, partnerships, go-to-market",
    "research": "Papers, experiments, formal methods, security",
    "infra": "Infrastructure, DevOps, scaling, deployment",
    "hackathon": "Competition-specific ideas, demo strategies",
}

PRIORITIES = ["critical", "high", "medium", "low", "someday"]

STATUSES = ["spark", "exploring", "validated", "project", "completed", "archived"]


# ─── Brain Engine ─────────────────────────────────────────────────

class BrainstormBrain:
    """Persistent brainstorming engine. Ideas never die, they evolve."""

    def __init__(self, storage_dir: str = "data/brainstorm"):
        self.storage_dir = Path(storage_dir)
        self.storage_dir.mkdir(parents=True, exist_ok=True)
        self.ideas_file = self.storage_dir / "ideas.jsonl"
        self.projects_file = self.storage_dir / "projects.jsonl"
        self.activity_file = self.storage_dir / "activity.jsonl"

    # ─── Ideas ────────────────────────────────────────────────────

    def add_idea(
        self,
        title: str,
        description: str,
        category: str = "product",
        priority: str = "medium",
        source: str = "user",
        tags: Optional[list] = None,
        agents_involved: Optional[list] = None,
        revenue_potential: str = "",
    ) -> Idea:
        """Capture a new idea. Never lose a thought."""
        now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        idea = Idea(
            id=str(uuid.uuid4())[:8],
            title=title,
            description=description,
            category=category if category in CATEGORIES else "product",
            status="spark",
            priority=priority if priority in PRIORITIES else "medium",
            source=source,
            created_at=now,
            updated_at=now,
            tags=tags or [],
            agents_involved=agents_involved or [],
            revenue_potential=revenue_potential,
            hash=hashlib.sha256(f"{title}{description}{now}".encode()).hexdigest()[:16],
        )
        self._append(self.ideas_file, asdict(idea))
        self._log_activity("idea_added", idea.id, f"New idea: {title}")
        return idea

    def evolve_idea(self, idea_id: str, new_status: str, note: str = "") -> bool:
        """Move an idea through its lifecycle."""
        ideas = self._load_all(self.ideas_file)
        for i, idea_data in enumerate(ideas):
            if idea_data.get("id") == idea_id:
                old_status = idea_data.get("status", "spark")
                idea_data["status"] = new_status
                idea_data["updated_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
                if note:
                    idea_data.setdefault("notes", []).append({
                        "timestamp": idea_data["updated_at"],
                        "author": "brain",
                        "text": note,
                    })
                ideas[i] = idea_data
                self._save_all(self.ideas_file, ideas)
                self._log_activity(
                    "idea_evolved", idea_id,
                    f"{old_status} → {new_status}: {note or 'no note'}"
                )
                return True
        return False

    def add_note(self, idea_id: str, author: str, text: str) -> bool:
        """Add a note to an existing idea."""
        ideas = self._load_all(self.ideas_file)
        for i, idea_data in enumerate(ideas):
            if idea_data.get("id") == idea_id:
                now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
                idea_data.setdefault("notes", []).append({
                    "timestamp": now,
                    "author": author,
                    "text": text,
                })
                idea_data["updated_at"] = now
                ideas[i] = idea_data
                self._save_all(self.ideas_file, ideas)
                return True
        return False

    def link_ideas(self, idea_id_1: str, idea_id_2: str) -> bool:
        """Connect related ideas."""
        ideas = self._load_all(self.ideas_file)
        found = [False, False]
        for i, idea_data in enumerate(ideas):
            if idea_data.get("id") == idea_id_1:
                idea_data.setdefault("related_ideas", []).append(idea_id_2)
                found[0] = True
            elif idea_data.get("id") == idea_id_2:
                idea_data.setdefault("related_ideas", []).append(idea_id_1)
                found[1] = True
            ideas[i] = idea_data
        if all(found):
            self._save_all(self.ideas_file, ideas)
            return True
        return False

    # ─── Projects ─────────────────────────────────────────────────

    def promote_to_project(
        self,
        idea_id: str,
        name: str = "",
        agents_assigned: Optional[list] = None,
        deadline: str = "",
    ) -> Optional[Project]:
        """Promote a validated idea to an active project."""
        ideas = self._load_all(self.ideas_file)
        idea_data = None
        for item in ideas:
            if item.get("id") == idea_id:
                idea_data = item
                break
        if not idea_data:
            return None

        self.evolve_idea(idea_id, "project", "Promoted to active project")

        now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        project = Project(
            id=str(uuid.uuid4())[:8],
            idea_id=idea_id,
            name=name or idea_data.get("title", "Untitled"),
            description=idea_data.get("description", ""),
            status="planning",
            agents_assigned=agents_assigned or idea_data.get("agents_involved", []),
            created_at=now,
            updated_at=now,
            deadline=deadline,
        )
        self._append(self.projects_file, asdict(project))
        self._log_activity("project_created", project.id, f"From idea {idea_id}: {project.name}")
        return project

    def update_project(self, project_id: str, status: str = "", progress_pct: int = -1) -> bool:
        """Update project status and progress."""
        projects = self._load_all(self.projects_file)
        for i, proj in enumerate(projects):
            if proj.get("id") == project_id:
                if status:
                    proj["status"] = status
                if progress_pct >= 0:
                    proj["progress_pct"] = min(progress_pct, 100)
                proj["updated_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
                projects[i] = proj
                self._save_all(self.projects_file, projects)
                return True
        return False

    # ─── Queries ──────────────────────────────────────────────────

    def get_ideas(self, status: str = "", category: str = "", priority: str = "") -> list:
        """Filter ideas by status, category, or priority."""
        ideas = self._load_all(self.ideas_file)
        if status:
            ideas = [i for i in ideas if i.get("status") == status]
        if category:
            ideas = [i for i in ideas if i.get("category") == category]
        if priority:
            ideas = [i for i in ideas if i.get("priority") == priority]
        return ideas

    def get_projects(self, status: str = "") -> list:
        """Get active projects, optionally filtered by status."""
        projects = self._load_all(self.projects_file)
        if status:
            projects = [p for p in projects if p.get("status") == status]
        return projects

    def get_pipeline_summary(self) -> dict:
        """Get the full brainstorm pipeline state."""
        ideas = self._load_all(self.ideas_file)
        projects = self._load_all(self.projects_file)

        status_counts = {}
        for idea in ideas:
            s = idea.get("status", "spark")
            status_counts[s] = status_counts.get(s, 0) + 1

        category_counts = {}
        for idea in ideas:
            c = idea.get("category", "product")
            category_counts[c] = category_counts.get(c, 0) + 1

        return {
            "total_ideas": len(ideas),
            "total_projects": len(projects),
            "by_status": status_counts,
            "by_category": category_counts,
            "active_projects": len([p for p in projects if p.get("status") in ("planning", "in_progress", "testing")]),
            "sparks_waiting": status_counts.get("spark", 0),
            "highest_priority": [
                {"id": i.get("id"), "title": i.get("title"), "priority": i.get("priority")}
                for i in ideas
                if i.get("priority") in ("critical", "high") and i.get("status") != "archived"
            ],
        }

    def search(self, query: str) -> list:
        """Search ideas by title, description, or tags."""
        q = query.lower()
        ideas = self._load_all(self.ideas_file)
        results = []
        for idea in ideas:
            if (q in idea.get("title", "").lower()
                or q in idea.get("description", "").lower()
                or q in str(idea.get("tags", [])).lower()):
                results.append(idea)
        return results

    # ─── Storage ──────────────────────────────────────────────────

    def _append(self, filepath: Path, data: dict):
        with open(filepath, "a") as f:
            f.write(json.dumps(data, ensure_ascii=False) + "\n")

    def _load_all(self, filepath: Path) -> list:
        if not filepath.exists():
            return []
        items = []
        with open(filepath, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        items.append(json.loads(line))
                    except json.JSONDecodeError:
                        continue
        return items

    def _save_all(self, filepath: Path, items: list):
        with open(filepath, "w") as f:
            for item in items:
                f.write(json.dumps(item, ensure_ascii=False) + "\n")

    def _log_activity(self, action: str, target_id: str, detail: str):
        entry = {
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "action": action,
            "target_id": target_id,
            "detail": detail,
        }
        self._append(self.activity_file, entry)
