from app.models.task import Task
import uuid

class GoalDecomposer:
    def decompose(self, goal: str) -> list[Task]:
        """
        Very simple decomposition for now.
        """
        return [
            Task(id=str(uuid.uuid4()), description=goal)
        ]
