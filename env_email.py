from pydantic import BaseModel

class Observation(BaseModel):
    emails: list

class Action(BaseModel):
    action_type: str
    target: str

class EmailEnv:
    def __init__(self):
        self.emails = []

    def reset(self):
        self.emails = [
            "URGENT: Server down",
            "Meeting at 3PM",
            "Spam offer"
        ]
        return Observation(emails=self.emails)

    def step(self, action: Action):
        reward = 0

        if action.action_type == "mark_urgent" and "URGENT" in action.target:
            reward += 0.5
        elif action.action_type == "delete" and "Spam" in action.target:
            reward += 0.3
        else:
            reward -= 0.2

        done = False
        return Observation(emails=self.emails), reward, done, {}

    def state(self):
        return self.emails
