

class EscalationHandler:
    def escalate(self, reason: str, context: dict):
        print("ESCALATION REQUIRED")
        print("Reason:", reason)
        print("Context:", context)
        return {
            "status": "paused",
            "reason": reason,
            "context": context
        }
