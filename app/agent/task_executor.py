import asyncio
import random
from app.models.task import Task

class TaskExecutor:
    async def execute_task(self, task: Task) -> Task:
        task.status = "running"

        # async sleep for 1 second
        await asyncio.sleep(1)

        # Simulate failure
        if random.random() < 0.3:
            task.status = "failed"
            task.retries += 1
            task.result = "Execution failed"
            return task

        task.status = "completed"
        task.result = f"Executed task: {task.description}"
        return task

    async def execute_tasks(self, tasks: list[Task]):
        pending_tasks = {t.id: t for t in tasks}
        results = []
        while pending_tasks:
            ready = [t for t in pending_tasks.values() if all(dep in [r.id for r in results] for dep in t.depends_on)]
            
            if not ready:
                raise RuntimeError("Circular depedency detected!")

            # Excuted ready tasks concurrenlty
            coros = [self.execute_task(t) for t in ready]
            done_tasks = await asyncio.gather(*coros)
            print(">>>>>>>> done_tasks >>>>>", done_tasks)
            results.extend(done_tasks)

            for t in done_tasks:
                pending_tasks.pop(t.id)

        print(">>>>>>>> pending_tasks >>>>>", pending_tasks)
        return results

