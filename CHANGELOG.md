# Changelog

## [0.1.0] - 2026-06-11

### Added
- Core architecture: AgentRunner, SkillManager, GrowthEngine
- Skill generation with metadata and validation
- Metrics tracking and history logging
- LLM adapter abstraction (mock implementation)
- Safety guardrails: resource limits, rate limiting
- Comprehensive documentation (README, ARCHITECTURE, CONTRIBUTING)
- GitHub Actions workflows (pytest, auto-grow)
- Production-ready CLI (main.py)

### Design Highlights
- Layered architecture: Core → Intelligence → Guidance → Safety
- Dry-run by default for safety
- Validation pipeline: syntax, interface, execution
- Multiple independent resource constraints
- Pluggable LLM integration

### Safety
- Max depth, disk, runtime, file count limits
- Per-minute and per-hour rate limiting
- Violation logging and halt-on-violation behavior

### Future Roadmap
- Real LLM integration (OpenAI, Claude, etc.)
- Skill dependencies and composition
- Distributed growth across multiple agents
- Skill marketplace and versioning
- Evolutionary algorithms (fitness, pruning, crossover)
