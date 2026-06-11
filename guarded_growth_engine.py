"""guarded_growth_engine.py - Growth engine with safety guardrails"""

from intelligent_growth_engine import IntelligentGrowthEngine
from safety_guardian import SafetyGuardian, RateLimiter

class GuardedGrowthEngine(IntelligentGrowthEngine):
    """IntelligentGrowthEngine with safety constraints."""
    
    def __init__(self, skill_dir=None, max_depth=3, dry_run=True, llm_adapter=None, 
                 max_disk_mb=100, max_runtime_sec=300, max_files=1000):
        super().__init__(skill_dir, max_depth, dry_run, llm_adapter)
        self.guardian = SafetyGuardian(max_disk_mb, max_runtime_sec, max_files)
        self.rate_limiter = RateLimiter(max_per_minute=60, max_per_hour=1000)
        self.blocked_creations = 0

    def grow_with_strategy(self, initial_context=None, max_generations=2):
        """Grow with safety checks."""
        self.guardian.start_session()
        
        if not self.guardian.can_proceed(self.skill_dir):
            print("Safety guardrails triggered:")
            for violation in self.guardian.get_violations():
                print(f"  - {violation}")
            return self.created
        
        for gen in range(max_generations):
            if not self.guardian.can_proceed(self.skill_dir):
                print("Growth interrupted by safety constraints.")
                break
            
            if not self.strategy.should_continue_growth(gen, len(self.created), self.max_depth):
                break
            
            ideas = self.strategy.plan_generation(context=initial_context, max_skills=3)
            
            for name, capability, description in ideas:
                can_create, reason = self.rate_limiter.can_create()
                if not can_create:
                    print(f"Rate limit hit: {reason}")
                    self.blocked_creations += 1
                    continue
                
                meta = self.gen.create_with_metadata(
                    name=f"gen{gen}_{name}",
                    description=description,
                    capability=capability,
                    parent=f"gen{gen-1}" if gen > 0 else None,
                    depth=gen
                )
                result = self.validator.validate_skill(meta["file"])
                if result["valid"]:
                    self.created.append(meta)
                    meta["validation"] = result
                    self.rate_limiter.record_creation()
        
        return self.created

    def get_growth_summary(self):
        summary = super().get_growth_summary()
        summary["blocked_creations"] = self.blocked_creations
        summary["safety_violations"] = self.guardian.get_violations()
        return summary
