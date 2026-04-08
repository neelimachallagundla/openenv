from pydantic import BaseModel

class Observation(BaseModel):
    code: str

class Action(BaseModel):
    issues: list

class CodeEnv:
    def __init__(self):
        self.code = ""

    def reset(self):
        self.code = "buggy code"
        return Observation(code=self.code)

    def step(self, action: Action):
        expected = {"null_pointer", "unused_variable", "off_by_one"}
        found = set(action.issues)

        reward = len(expected & found) / len(expected)

        done = True
        return Observation(code=self.code), reward, done, {}

    def state(self):
        return self.code
