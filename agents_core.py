"""
agents_core.py - Minimal prototype for a self-extending agent.
"""

import os
import importlib.util
import traceback

class AgentRunner:
    def __init__(self, skill_dir=None, max_depth=3, dry_run=True):
        self.skill_dir = os.path.abspath(skill_dir) if skill_dir else os.path.abspath(os.path.dirname(__file__))
        self.max_depth = max_depth
        self.dry_run = dry_run
        self.registry = {}

    def discover_skill_files(self):
        try:
            return sorted([os.path.join(self.skill_dir, f) for f in os.listdir(self.skill_dir)
                           if f.startswith("skill_") and f.endswith(".py")])
        except Exception:
            return []

    def load_skill_from_path(self, path):
        name = os.path.splitext(os.path.basename(path))[0]
        try:
            spec = importlib.util.spec_from_file_location(name, path)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            return mod
        except Exception:
            traceback.print_exc()
            return None

    def register_skill(self, mod):
        name = getattr(mod, "NAME", getattr(mod, "__name__", None))
        if name and name not in self.registry:
            self.registry[name] = mod
            return True
        return False

    def run_growth_cycle(self):
        # load existing skills
        for p in self.discover_skill_files():
            mod = self.load_skill_from_path(p)
            if mod:
                self.register_skill(mod)
        if not self.registry:
            print("No skills found.")
            if self.dry_run:
                print("(dry-run) would create a starter skill using SkillManager.")
            else:
                try:
                    from skill_manager import SkillManager
                    sm = SkillManager(self.skill_dir)
                    new = sm.create_skill_from_template("starter")
                    print("Created", new)
                    mod = self.load_skill_from_path(os.path.join(self.skill_dir, new))
                    if mod:
                        self.register_skill(mod)
                except Exception as e:
                    print("Failed to create starter skill:", e)

if __name__ == "__main__":
    runner = AgentRunner(dry_run=True)
    runner.run_growth_cycle()
