import pytest
from safety_guardian import SafetyGuardian, RateLimiter
from guarded_growth_engine import GuardedGrowthEngine

def test_safety_guardian():
    sg = SafetyGuardian(max_disk_mb=100, max_runtime_sec=300, max_files=1000)
    sg.start_session()
    assert sg.check_runtime()

def test_rate_limiter():
    rl = RateLimiter(max_per_minute=60)
    can_create, reason = rl.can_create()
    assert can_create
    rl.record_creation()

def test_guarded_growth(tmp_path):
    gge = GuardedGrowthEngine(
        skill_dir=str(tmp_path),
        max_depth=2,
        dry_run=True,
        max_disk_mb=100,
        max_runtime_sec=300
    )
    summary = gge.get_growth_summary()
    assert "blocked_creations" in summary
    assert "safety_violations" in summary
