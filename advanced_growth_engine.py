"""advanced_growth_engine.py - Enhanced growth with validation and metrics"""

import os
import time
from skill_generator import SkillGenerator
from skill_validator import SkillValidator
from growth_metrics import GrowthMetrics

class AdvancedGrowthEngine:
    def __init__(self, skill_dir=None, max_depth=3, dry_run=True, max_new=10, validate=True):
        self.skill_dir = skill_dir
        self.gen = SkillGenerator(skill_dir)
        self.validator = SkillValidator() if validate else None
        self.metrics = GrowthMetrics()
        self.max_depth = max_depth
        self.dry_run = dry_run
        self.max_new = max_new
        self.created = []
        self.valid_count = 0

    def grow_generation(self, gen_num=1, seed_name="auto", capabilities=None):
        """Generate and validate a generation of skills."""
        start = time.time()
        capabilities = capabilities or ["parse", "transform", "analyze", "synthesize"]
        
        for i in range(min(self.max_new, len(capabilities))):
            cap = capabilities[i % len(capabilities)]
            name = f"gen{gen_num}_skill{i}"
            desc = f"Auto-generated skill with {cap} capability"
            
            meta = self.gen.create_with_metadata(
                name=name,
                description=desc,
                capability=cap,
                parent=seed_name,
                depth=gen_num
            )
            self.created.append(meta)
            
            if self.validator:
                result = self.validator.validate_skill(meta["file"])
                if result["valid"]:
                    self.valid_count += 1
        
        duration_ms = (time.time() - start) * 1000
        if not self.dry_run:
            self.metrics.record_cycle(len(self.created), gen_num, duration_ms)
        
        return self.created

    def recursive_grow(self, num_generations=2):
        """Recursively grow multiple generations."""
        for gen in range(1, num_generations + 1):
            if gen > self.max_depth:
                break
            self.grow_generation(gen)
        return self.created
