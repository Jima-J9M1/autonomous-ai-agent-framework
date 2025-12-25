
from app.models.task import Task


class StepEvaluator:
    def evaluate(self, task: Task) -> dict:
        score = 1.0 if task.status == "completed" else 0.0
        hallucination = 0.0

        return {
            "task_id":task.id,
            "status":task.status,
            "score":score,
            "hallucination_risk": hallucination
        }
