"""main.py - Production entry point for recursive growth agent"""

import argparse
import json
import sys
from pathlib import Path
from guarded_growth_engine import GuardedGrowthEngine
from llm_adapter import LLMAdapter

def load_config(config_file="growth_config.json"):
    """Load configuration from file."""
    if Path(config_file).exists():
        with open(config_file, "r") as f:
            return json.load(f)
    return {
        "enabled": False,
        "max_depth": 2,
        "max_new": 3,
        "branch_prefix": "auto/growth",
        "max_disk_mb": 100,
        "max_runtime_sec": 300,
        "max_files": 1000
    }

def main():
    parser = argparse.ArgumentParser(description="Recursive Growth Agent")
    parser.add_argument("--config", default="growth_config.json", help="Config file path")
    parser.add_argument("--skill-dir", default=".", help="Skill directory")
    parser.add_argument("--dry-run", action="store_true", default=True, help="Dry run (default)")
    parser.add_argument("--commit", action="store_true", help="Actually commit changes")
    parser.add_argument("--generations", type=int, default=1, help="Number of generations")
    parser.add_argument("--llm", default="mock", help="LLM model name")
    args = parser.parse_args()

    config = load_config(args.config)
    enabled = args.commit or config.get("enabled", False)
    dry_run = not enabled

    llm = LLMAdapter(model_name=args.llm)
    
    engine = GuardedGrowthEngine(
        skill_dir=args.skill_dir,
        max_depth=config.get("max_depth", 2),
        dry_run=dry_run,
        llm_adapter=llm,
        max_disk_mb=config.get("max_disk_mb", 100),
        max_runtime_sec=config.get("max_runtime_sec", 300),
        max_files=config.get("max_files", 1000)
    )

    print(f"Starting growth engine (dry_run={dry_run})...")
    created = engine.grow_with_strategy(
        initial_context="production",
        max_generations=args.generations
    )

    summary = engine.get_growth_summary()
    print("\nGrowth Summary:")
    print(json.dumps(summary, indent=2, default=str))

    if summary["safety_violations"]:
        print("\n[WARNING] Safety violations detected:")
        for violation in summary["safety_violations"]:
            print(f"  - {violation}")
        return 1

    print(f"\nCreated {summary['total_created']} skills ({summary['valid_skills']} valid)")
    if dry_run:
        print("(Dry run - no files were actually written)")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
