import importlib.util
from skill_manager import SkillManager

def test_create_skill(tmp_path):
    sm = SkillManager(str(tmp_path))
    name = sm.create_skill_from_template("test")
    path = tmp_path / name
    assert path.exists()

    spec = importlib.util.spec_from_file_location("testskill", str(path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    assert hasattr(mod, "run")
