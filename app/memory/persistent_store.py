import json
import os

class PersistentStore:
    def __init__(self, path="agent_state.json"):
        self.path = path

    def save(self, data: dict):
        with open(self.path, "w") as f:
            json.dump(data, f, indent=2)

    def load(self) -> dict | None:
        if not os.path.exists(self.path):
            return None
        with open(self.path, "r") as f:
            return json.load(f)
