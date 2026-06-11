"""example_advanced.py - Advanced growth with validation"""

from advanced_growth_engine import AdvancedGrowthEngine

print("Example 2: Advanced Growth with Validation")
print("=" * 40)
age = AdvancedGrowthEngine(max_depth=2, dry_run=True, max_new=2, validate=True)
created = age.recursive_grow(num_generations=2)
print(f"Dry-run: would create {len(created)} skills")
if created:
    print(f"First skill: {created[0]['name']}")
print()
