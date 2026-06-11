import os
import glob

class SkillManager:
    def __init__(self, skill_dir=None):
        self.skill_dir = os.path.abspath(skill_dir) if skill_dir else os.path.abspath(os.path.dirname(__file__))

    def next_skill_path(self, base="skill"):
        existing = glob.glob(os.path.join(self.skill_dir, "skill_*.py"))
        n = len(existing) + 1
        path = os.path.join(self.skill_dir, f"skill_{n}.py")
        while os.path.exists(path):
            n += 1
            path = os.path.join(self.skill_dir, f"skill_{n}.py")
        return path

    def create_skill_from_template(self, name="auto", description="Auto-generated skill", parent=None, depth=0, max_depth=3):
        path = self.next_skill_path()
        meta = f"""# {description}
# parent={parent}
# depth={depth}
# max_depth={max_depth}
"""
        code = f'''{meta}
NAME = "skill_{name}"
def run(context=None):
    """Example skill entrypoint."""
    return {{"result": "Hello from {name}", "parent": {repr(parent)}, "depth": {depth}}}
'''
        with open(path, "w", encoding="utf-8") as f:
            f.write(code)
        return os.path.basename(path)
