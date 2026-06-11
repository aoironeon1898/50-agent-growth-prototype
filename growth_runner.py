from agents_core import AgentRunner
from growth_engine import GrowthEngine

if __name__ == "__main__":
    runner = AgentRunner(dry_run=True)
    runner.run_growth_cycle()
    ge = GrowthEngine(max_depth=2, dry_run=True)
    created = ge.grow_from_seed(seed_name='seed', seed_description='auto seed', seed_depth=0)
    print('GrowthEngine (dry-run) would create:', created)
