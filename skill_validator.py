"""skill_validator.py - Validate and test generated skills"""

import importlib.util
import traceback

class SkillValidator:
    def __init__(self):
        self.results = []

    def load_skill(self, path):
        """Load a skill module."""
        try:
            name = path.split('/')[-1].replace('.py', '')
            spec = importlib.util.spec_from_file_location(name, path)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            return mod
        except Exception as e:
            traceback.print_exc()
            return None

    def validate_skill(self, path):
        """Check if skill is valid."""
        mod = self.load_skill(path)
        if not mod:
            return {"valid": False, "error": "Failed to load module"}
        
        checks = {
            "has_name": hasattr(mod, "NAME"),
            "has_run": hasattr(mod, "run"),
            "name_is_str": isinstance(getattr(mod, "NAME", None), str),
            "run_callable": callable(getattr(mod, "run", None))
        }
        
        try:
            result = mod.run()
            checks["run_executes"] = result is not None
            checks["result_type"] = type(result).__name__
        except Exception as e:
            checks["run_executes"] = False
            checks["error"] = str(e)
        
        valid = all([checks["has_name"], checks["has_run"], checks["run_callable"], checks.get("run_executes", False)])
        return {"valid": valid, "checks": checks}
