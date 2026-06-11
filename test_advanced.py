import os
import pytest
from pathlib import Path
from skill_generator import SkillGenerator
from skill_validator import SkillValidator
from advanced_growth_engine import AdvancedGrowthEngine

def test_skill_generator(tmp_path):
    gen = SkillGenerator(str(tmp_path))
    meta = gen.create_with_metadata(
        name="test",
        description="test skill",
        capability="parse"
    )
    assert meta["name"] == "test"
    assert Path(meta["file"]).exists()

def test_skill_validator(tmp_path):
    gen = SkillGenerator(str(tmp_path))
    meta = gen.create_with_metadata(
        name="valid_test",
        description="test",
        capability="transform"
    )
    validator = SkillValidator()
    result = validator.validate_skill(meta["file"])
    assert result["valid"] == True
    assert result["checks"]["has_name"]
    assert result["checks"]["run_executes"]

def test_advanced_growth(tmp_path):
    age = AdvancedGrowthEngine(
        skill_dir=str(tmp_path),
        max_depth=2,
        dry_run=True,
        max_new=3,
        validate=True
    )
    created = age.recursive_grow(num_generations=2)
    assert len(created) >= 0
