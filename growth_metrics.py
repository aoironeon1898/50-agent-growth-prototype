"""growth_metrics.py - Track growth statistics"""

import json
from datetime import datetime
from pathlib import Path

class GrowthMetrics:
    def __init__(self, state_file="growth_state.json"):
        self.state_file = state_file
        self.state = self._load_state()

    def _load_state(self):
        if Path(self.state_file).exists():
            with open(self.state_file, "r") as f:
                return json.load(f)
        return {
            "total_skills": 0,
            "total_cycles": 0,
            "max_depth_reached": 0,
            "generations": []
        }

    def record_cycle(self, num_created, max_depth, duration_ms):
        """Record a growth cycle."""
        self.state["total_skills"] += num_created
        self.state["total_cycles"] += 1
        self.state["max_depth_reached"] = max(self.state["max_depth_reached"], max_depth)
        self.state["generations"].append({
            "cycle": self.state["total_cycles"],
            "created": num_created,
            "depth": max_depth,
            "duration_ms": duration_ms,
            "timestamp": datetime.now().isoformat()
        })
        self._save_state()

    def _save_state(self):
        with open(self.state_file, "w") as f:
            json.dump(self.state, f, indent=2)

    def get_summary(self):
        return {
            "total_skills": self.state["total_skills"],
            "total_cycles": self.state["total_cycles"],
            "max_depth": self.state["max_depth_reached"],
            "cycles": len(self.state["generations"])
        }
