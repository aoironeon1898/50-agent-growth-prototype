"""example_guarded.py - Growth with safety guardrails"""

from guarded_growth_engine import GuardedGrowthEngine

print("Example 3: Guarded Growth (with safety)")
print("=" * 40)
ge = GuardedGrowthEngine(
    max_depth=1,
    dry_run=True,
    max_disk_mb=50,
    max_runtime_sec=60,
    max_files=100
)
created = ge.grow_with_strategy(initial_context="example", max_generations=1)
summary = ge.get_growth_summary()
print(f"Summary: {summary['total_created']} created, "
      f"{summary['blocked_creations']} blocked")
if summary['safety_violations']:
    print("Violations:")
    for v in summary['safety_violations']:
        print(f"  - {v}")
print()
