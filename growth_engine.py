"""growth_engine.py - Controlled recursive skill generation for prototype
"""

import os
from skill_manager import SkillManager

class GrowthEngine:
    def __init__(self, skill_dir=None, max_depth=3, dry_run=True, max_new=10):
        self.sm = SkillManager(skill_dir)
        self.max_depth = max_depth
        self.dry_run = dry_run
        self.max_new = max_new
        self.created = []

    def grow_from_seed(self, seed_name="seed", seed_description="Auto-generated seed", seed_depth=0):
        root = self.sm.create_skill_from_template(seed_name, seed_description, parent=None, depth=seed_depth, max_depth=self.max_depth)
        self.created.append(root)
        if self.dry_run:
            return list(self.created)
        queue = [(root, seed_depth)]
        count = 0
        while queue and count < self.max_new:
            fname, depth = queue.pop(0)
            if depth >= self.max_depth:
                continue
            child_name = f"{os.path.splitext(fname)[0]}_child{count}"
            child_depth = depth + 1
            child = self.sm.create_skill_from_template(child_name, f"child of {fname}", parent=fname, depth=child_depth, max_depth=self.max_depth)
            self.created.append(child)
            count += 1
            queue.append((child, child_depth))
        return list(self.created)

if __name__ == "__main__":
    ge = GrowthEngine(max_depth=3, dry_run=True, max_new=10)
    print("Created (dry-run):", ge.grow_from_seed())
