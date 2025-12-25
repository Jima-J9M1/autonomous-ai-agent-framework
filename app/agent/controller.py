import asyncio
from uuid import MAX
from app.agent.escalation_handler import EscalationHandler
from app.agent.goal_decomposer import GoalDecomposer
from app.agent.task_executor import TaskExecutor
from app.agent.state_machine import StateMachine
from app.evaluation.step_evaluator import StepEvaluator
from app.memory.persistent_store import PersistentStore
from app.models.state import AgentState

MAX_RETRIES = 2

# The brain of the agent.
class AutonomousAgent:
    def __init__(self):
        self.decomposer = GoalDecomposer()
        self.executor = TaskExecutor()
        self.state_machine = StateMachine()
        self.store = PersistentStore()
        self.evaluator = StepEvaluator()
        self.escalation = EscalationHandler()

    async def run(self, goal: str):
        self.state_machine.transition(AgentState.PLANNING)

        tasks = self.decomposer.decompose(goal)

        self.state_machine.transition(AgentState.EXECUTING)
        
        results = []

        try:
            executed_tasks = await self.executor.execute_tasks(tasks)
            print(">>>>>>>> executed >>>>>", executed_tasks)
            for task in executed_tasks:
                evaluation = self.evaluator.evaluate(task)
                results.append({**task.model_dump(), "evaluation":evaluation})

                if task.status == 'failed' and task.retries <= MAX_RETRIES:
                    executed_tasks = await self.executor.execute_tasks([task]) 
                
                if task.retries > MAX_RETRIES:
                    return self.escalation.escalate(
                   reason="Task failed repeatedly",
                   context=task.model_dump()
                    )
        except Exception as e:
            self.state_machine.transition(AgentState.FAILED)
            return {'error':str(e)}

        self.state_machine.transition(AgentState.COMPLETED)
        return results


    def resume(self):
        data = self.store.load()
        if not data:
            return None

        print("Resuming from saved state:", data)
        return data
