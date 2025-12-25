from pydantic import BaseModel

class Budget(BaseModel):
    max_steps: int
    max_failures: int
