from pydantic import BaseModel
from typing import Optional

class Task(BaseModel):
    id: str
    description: str
    status: str = "pending"
    result: Optional[str] = None
    retries: int = 0
    depends_on: Optional[list[str]] = []