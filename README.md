# Recursive-Growth Agent Prototype

A controlled prototype for self-extending agents that recursively generate and validate skills.

## Architecture

### Core Modules
- **agents_core.py**: AgentRunner — discovers and loads skill modules
- **skill_manager.py**: SkillManager — creates skill files with metadata
- **growth_engine.py**: GrowthEngine — basic recursive skill generation (depth-limited)

### Enhanced Modules
- **skill_generator.py**: SkillGenerator — generates skills with capabilities and examples
- **skill_validator.py**: SkillValidator — validates skill syntax and executes run()
- **growth_metrics.py**: GrowthMetrics — tracks creation statistics and history
- **advanced_growth_engine.py**: AdvancedGrowthEngine — multi-generation with validation

### Intelligent Modules
- **llm_adapter.py**: LLMAdapter — abstraction for LLM-guided generation (mock)
- **intelligent_growth_engine.py**: IntelligentGrowthEngine — strategy-guided growth

### Safety Modules
- **safety_guardian.py**: SafetyGuardian & RateLimiter — enforce constraints
- **guarded_growth_engine.py**: GuardedGrowthEngine — growth with safety checks

## Skill Format

Each generated skill is a Python module:
```python
# skill_1.py
NAME = "skill_1"

def run(context=None):
    return {"result": "...", "capability": "parse"}
```

## Usage

### Basic Growth
```python
from growth_engine import GrowthEngine

ge = GrowthEngine(max_depth=2, dry_run=False, max_new=5)
created = ge.grow_from_seed(seed_name="root", seed_depth=0)
print(f"Created: {len(created)} skills")
```

### With Safety
```python
from guarded_growth_engine import GuardedGrowthEngine

ge = GuardedGrowthEngine(
    max_depth=2,
    max_disk_mb=100,
    max_runtime_sec=300,
    max_files=1000
)
created = ge.grow_with_strategy()
print(ge.get_growth_summary())
```

## Safety Constraints

- **Depth**: max_depth (default 3)
- **Disk**: max_disk_mb (default 100MB)
- **Runtime**: max_runtime_sec (default 300s)
- **Files**: max_files (default 1000)
- **Rate**: max_per_minute (default 60), max_per_hour (default 1000)

## Configuration

`growth_config.json`:
```json
{
  "enabled": false,
  "max_depth": 2,
  "max_new": 3,
  "branch_prefix": "auto/growth"
}
```

Set `enabled: true` to allow auto-growth workflow to commit changes.

## Workflow

### Local Development
```bash
python -m pytest test_*.py -v
python growth_runner.py
```

### Automatic Growth (GitHub Actions)
- `.github/workflows/pytest.yml`: Runs tests on push/PR
- `.github/workflows/auto-grow.yml`: Scheduled daily growth (configurable)

## Design Principles

1. **Dry-run by default**: Set dry_run=False explicitly to commit changes
2. **Validation**: All generated skills pass syntax and execution checks
3. **Metrics**: Track growth history, success rates, and timelines
4. **Safety first**: Hard limits on resources, rate limiting, progress monitoring
5. **Extensibility**: Pluggable LLM adapters, skill generators, validators

## Future Enhancements

- Real LLM integration (OpenAI, Claude, etc.)
- Skill dependencies and composition
- Performance profiling and optimization
- Distributed growth across multiple agents
- Skill marketplace and versioning

## License

MIT
