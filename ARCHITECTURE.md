# Architecture & Design Decisions

## Design Overview

```
┌─────────────────────────────────────────┐
│  GuardedGrowthEngine (safety layer)    │
│  ├─ IntelligentGrowthEngine            │
│  │  ├─ AdvancedGrowthEngine            │
│  │  │  ├─ GrowthEngine (basic)         │
│  │  │  └─ SkillValidator               │
│  │  ├─ LLMAdapter (mock/real)          │
│  │  └─ SmartGrowthStrategy             │
│  ├─ SafetyGuardian (limits)            │
│  └─ RateLimiter (per-minute/hour)      │
│                                         │
│  Supporting Modules:                    │
│  ├─ SkillManager (file operations)      │
│  ├─ SkillGenerator (code generation)    │
│  ├─ GrowthMetrics (statistics)          │
│  └─ SkillValidator (syntax/runtime)     │
└─────────────────────────────────────────┘
```

## Key Design Decisions

### 1. Layered Architecture
- **Layer 1 (Core)**: SkillManager, GrowthEngine — basic generation
- **Layer 2 (Intelligence)**: SkillValidator, SkillGenerator, AdvancedGrowthEngine — improved quality
- **Layer 3 (Guidance)**: LLMAdapter, IntelligentGrowthEngine — strategic decisions
- **Layer 4 (Safety)**: SafetyGuardian, GuardedGrowthEngine — constraints and limits

### 2. Dry-Run First
All growth engines default to `dry_run=True`. This logs what *would* be created without committing changes. Users explicitly enable real generation.

### 3. Validation Pipeline
Every skill is validated:
1. **Syntax**: Python module loads without errors
2. **Interface**: Has NAME attribute and run() callable
3. **Execution**: run() executes and returns a dict

### 4. Resource Constraints
Multiple independent limits prevent runaway growth:
- Time-based: max_runtime_sec
- Space-based: max_disk_mb, max_files
- Rate-based: max_per_minute, max_per_hour

### 5. Pluggable LLM
LLMAdapter is an abstraction:
- Mock implementation for testing/demo
- Real implementations (OpenAI, Claude) inherit interface
- Strategy can be swapped without changing growth logic

## Recursion Strategy

**Problem**: Prevent infinite expansion

**Solution**:
- Depth-first generation per generation
- Each generation shares same depth limit
- Breadth (max_new) limits siblings per generation
- Total capped by min(max_depth, max_files / avg_per_gen)

**Example** (max_depth=2, max_new=3):
```
Gen 0: seed (1 total)
Gen 1: 3 children (4 total)
Gen 2: up to 9 grandchildren (13 total, if not constrained)
```

## Safety-First Philosophy

1. **Fail closed**: Violations halt growth, don't silently ignore
2. **Monitor always**: Metrics track every cycle for analysis
3. **Rate limit**: Prevent DOS-like scenarios
4. **Audit trail**: growth_state.json logs all decisions

## Future Considerations

### Distributed Growth
- Multiple agents generating in parallel
- Conflict resolution via version control
- Centralized metrics aggregation

### Evolutionary Pressure
- Fitness function on skill utility
- Pruning: Remove low-value skills
- Crossover: Combine successful skill patterns

### Dynamic Strategies
- Monitor and adapt to success rates
- Learn from validation feedback
- Adjust generation parameters per generation
