"""skill_generator.py - Generate skills with metadata and optional LLM integration"""

import json
from datetime import datetime
from skill_manager import SkillManager

class SkillGenerator:
    def __init__(self, skill_dir=None):
        self.sm = SkillManager(skill_dir)

    def generate_skill_code(self, name, description, capability, examples=None):
        """Generate skill code with context."""
        ex_str = ""
        if examples:
            ex_str = "\n# Examples:\n"
            for ex in examples:
                ex_str += f"#   {ex}\n"
        code = f'''# {description}
# capability: {capability}
# generated: {datetime.now().isoformat()}
{ex_str}
NAME = "skill_{name}"

def run(context=None):
    """Auto-generated skill."""
    return {{
        "result": "Hello from {name}",
        "capability": "{capability}",
        "ready": True
    }}
'''
        return code

    def create_with_metadata(self, name, description, capability, examples=None, parent=None, depth=0):
        """Create skill file and return metadata."""
        code = self.generate_skill_code(name, description, capability, examples)
        path = self.sm.next_skill_path()
        with open(path, "w", encoding="utf-8") as f:
            f.write(code)
        
        metadata = {
            "name": name,
            "file": path,
            "description": description,
            "capability": capability,
            "parent": parent,
            "depth": depth,
            "created_at": datetime.now().isoformat()
        }
        return metadata
