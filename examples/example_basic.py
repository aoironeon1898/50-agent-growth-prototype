"""example_basic.py - Basic usage example"""

from growth_engine import GrowthEngine

print("Example 1: Basic Growth")
print("=" * 40)
ge = GrowthEngine(max_depth=1, dry_run=True, max_new=3)
created = ge.grow_from_seed(seed_name="basic", seed_description="Basic seed")
print(f"Dry-run: would create {len(created)} skills")
print()
