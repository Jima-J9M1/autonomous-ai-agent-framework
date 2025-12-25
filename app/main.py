from fastapi import FastAPI

from app.agent.controller import AutonomousAgent

app = FastAPI()

agent = AutonomousAgent()

@app.get("/health")
def health():
    return {"status":"ok"}


@app.post("/run")
async def run_agent(goal: str):
    results = await agent.run(goal)
    return {"results": results}