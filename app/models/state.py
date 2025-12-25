from enum import Enum

class AgentState(str, Enum):
    IDLE = "idle"
    PLANNING = "planning"
    EXECUTING = "executing"
    WAITING = "waiting"
    FAILED = "failed"
    COMPLETED = "completed"
