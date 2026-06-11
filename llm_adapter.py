"""llm_adapter.py - LLM abstraction layer for skill generation ideas"""

class LLMAdapter:
    """Abstract LLM interface for generating skill ideas."""
    
    def __init__(self, model_name=None):
        self.model_name = model_name or "mock"

    def generate_skill_ideas(self, context=None, count=3):
        """
        Generate skill ideas based on context.
        Returns list of (name, capability, description) tuples.
        """
        if self.model_name == "mock":
            return self._mock_ideas(count)
        raise NotImplementedError(f"Model {self.model_name} not implemented")

    def _mock_ideas(self, count=3):
        ideas = [
            ("parser", "parse", "Extract structure from unstructured data"),
            ("aggregator", "aggregate", "Combine multiple data sources"),
            ("validator", "validate", "Check data integrity and consistency"),
            ("transformer", "transform", "Convert between data formats"),
            ("analyzer", "analyze", "Compute statistics and patterns"),
        ]
        return ideas[:count]

    def evaluate_skill(self, name, code):
        """Evaluate if a skill is useful (mock implementation)."""
        return {"score": 0.7, "reason": "mock evaluation"}

class SmartGrowthStrategy:
    """Strategy for intelligent growth using LLM guidance."""
    
    def __init__(self, llm_adapter=None):
        self.llm = llm_adapter or LLMAdapter("mock")
        self.idea_history = []

    def plan_generation(self, context=None, max_skills=5):
        """Plan which skills to generate."""
        ideas = self.llm.generate_skill_ideas(context=context, count=max_skills)
        self.idea_history.append({"context": context, "ideas": ideas})
        return ideas

    def should_continue_growth(self, depth, total_skills, max_depth):
        """Decide whether to continue growing."""
        if depth >= max_depth:
            return False
        if total_skills > 100:
            return False
        return True
