import os
from growth_engine import GrowthEngine

def test_growth(tmp_path):
    ge = GrowthEngine(skill_dir=str(tmp_path), max_depth=2, dry_run=False, max_new=5)
    created = ge.grow_from_seed(seed_name="root", seed_description="seed", seed_depth=0)
    assert len(created) >= 1
    for fname in created:
        p = tmp_path / fname
        assert p.exists()
        text = p.read_text(encoding='utf-8')
        assert 'NAME' in text
