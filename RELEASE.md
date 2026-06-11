# Recursive Growth Agent v0.1.0

## Release Summary

A fully-featured controlled recursive-growth agent prototype with:
- **Layered architecture** (Core → Intelligence → Guidance → Safety)
- **Validation pipeline** (syntax, interface, execution)
- **Safety guardrails** (resource limits, rate limiting)
- **Pluggable LLM integration** (mock + extensible)
- **Production CLI** with dry-run by default
- **Comprehensive documentation** and examples

## Quick Start

```bash
# Dry-run (no files written)
python main.py --dry-run --generations 1

# With validation & metrics
python -c "from advanced_growth_engine import AdvancedGrowthEngine; \
  age = AdvancedGrowthEngine(dry_run=True); \
  print(age.recursive_grow(2))"

# With safety guardrails
python -c "from guarded_growth_engine import GuardedGrowthEngine; \
  ge = GuardedGrowthEngine(max_disk_mb=100); \
  print(ge.get_growth_summary())"
```

## Features Implemented

✅ Basic recursive skill generation  
✅ Multi-generation growth with breadth/depth control  
✅ Skill validation (syntax, interface, execution)  
✅ Metrics tracking (creation history, statistics)  
✅ LLM-guided strategy (mock + pluggable)  
✅ Safety constraints (disk, runtime, file count)  
✅ Rate limiting (per-minute, per-hour)  
✅ Production CLI with configuration  
✅ GitHub Actions CI/CD workflows  
✅ Comprehensive docs and examples  

## Architecture

```python
GuardedGrowthEngine
  ├── Safety: SafetyGuardian + RateLimiter
  └── IntelligentGrowthEngine
      ├── LLMAdapter (strategy guidance)
      └── AdvancedGrowthEngine
          ├── SkillValidator
          ├── GrowthMetrics
          └── GrowthEngine (basic recursion)
```

## Configuration

```json
{
  "enabled": false,
  "max_depth": 2,
  "max_new": 3,
  "max_disk_mb": 100,
  "max_runtime_sec": 300,
  "max_files": 1000
}
```

## Files

**Core**:
- `agents_core.py` - Agent runner
- `skill_manager.py` - File operations
- `growth_engine.py` - Basic recursion

**Intelligence**:
- `skill_generator.py` - Code generation with metadata
- `skill_validator.py` - Validation pipeline
- `advanced_growth_engine.py` - Multi-generation with validation
- `growth_metrics.py` - Statistics tracking

**Guidance**:
- `llm_adapter.py` - LLM abstraction (mock)
- `intelligent_growth_engine.py` - Strategy-guided growth

**Safety**:
- `safety_guardian.py` - Resource limits + rate limiting
- `guarded_growth_engine.py` - Growth with constraints

**Production**:
- `main.py` - CLI entry point
- `setup.py` - Package configuration

**Tests**:
- `test_*.py` - Pytest suite

**Docs**:
- `README.md` - Getting started
- `ARCHITECTURE.md` - Design deep-dive
- `CONTRIBUTING.md` - Development guide
- `CHANGELOG.md` - Version history
- `examples/` - Usage examples

## Next Steps

1. **Real LLM Integration**: Replace mock with OpenAI/Claude
2. **Skill Dependencies**: Allow skills to depend on other skills
3. **Performance Profiling**: Measure and optimize generation speed
4. **Distributed Growth**: Run multiple agents in parallel
5. **Evolutionary Algorithms**: Fitness-based pruning and crossover
6. **Skill Versioning**: Track skill evolution over time

## Links

- **Repository**: https://github.com/aoironeon1898/50-agent-growth-prototype
- **Issues & Roadmap**: Use GitHub Issues to track feature requests

---

**Built with Copilot** 🤖  
MIT License © 2026
