from app.models.state import AgentState

class StateMachine:
    def __init__(self):
        self.state = AgentState.IDLE

    def transition(self, new_state: AgentState):
        print(f"STATE: {self.state} -> {new_state}")
        self.state = new_state
