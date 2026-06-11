"""intelligent_growth_engine.py - Growth engine guided by LLM insights"""

import os
from skill_generator import SkillGenerator
from skill_validator import SkillValidator
from growth_metrics import GrowthMetrics
from llm_adapter import LLMAdapter, SmartGrowthStrategy

class IntelligentGrowthEngine:
    def __init__(self, skill_dir=None, max_depth=3, dry_run=True, llm_adapter=None):
        self.skill_dir = skill_dir
        self.gen = SkillGenerator(skill_dir)
        self.validator = SkillValidator()
        self.metrics = GrowthMetrics()
        self.llm = llm_adapter or LLMAdapter("mock")
        self.strategy = SmartGrowthStrategy(self.llm)
        self.max_depth = max_depth
        self.dry_run = dry_run
        self.created = []

    def grow_with_strategy(self, initial_context=None, max_generations=2):
        """
        Grow skills guided by LLM strategy.
        """
        for gen in range(max_generations):
            if not self.strategy.should_continue_growth(gen, len(self.created), self.max_depth):
                break
            
            ideas = self.strategy.plan_generation(context=initial_context, max_skills=3)
            
            for name, capability, description in ideas:
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
        
        return self.created

    def get_growth_summary(self):
        """Return summary of growth."""
        return {
            "total_created": len(self.created),
            "valid_skills": len([m for m in self.created if m.get("validation", {}).get("valid", False)]),
            "ideas_explored": len(self.strategy.idea_history),
            "metrics": self.metrics.get_summary()
        }
