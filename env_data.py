from pydantic import BaseModel

class Observation(BaseModel):
    data: list

class Action(BaseModel):
    cleaned_data: list

class DataEnv:
    def __init__(self):
        self.data = []

    def reset(self):
        self.data = [1, 2, 2, None]
        return Observation(data=self.data)

    def step(self, action: Action):
        reward = 0

        if len(action.cleaned_data) == len(set(action.cleaned_data)):
            reward += 0.5

        if None not in action.cleaned_data:
            reward += 0.5

        done = True
        return Observation(data=action.cleaned_data), reward, done, {}

    def state(self):
        return self.data
