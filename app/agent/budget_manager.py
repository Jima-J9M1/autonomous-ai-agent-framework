class BudgetManager:
    def __init__(self, budget):
        self.budget = budget
        self.steps_used = 0
        self.failures = 0

    def record_step(self):
        self.steps_used += 1
        if self.steps_used > self.budget.max_steps:
            raise RuntimeError("Step budget exceeded")

    def record_failure(self):
        self.failures += 1
        if self.failures > self.budget.max_failures:
            raise RuntimeError("Failure budget exceeded")
