from pydantic import BaseModel

class EscalationRequest(BaseModel):
    reason: str
    context: dict
