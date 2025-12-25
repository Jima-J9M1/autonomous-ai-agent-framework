from pydantic import BaseModel

class Goal(BaseModel):
    id: str
    description: str
