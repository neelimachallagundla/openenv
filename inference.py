# inference.py

def reset():
    return {
        "observation": "initial state",
        "reward": 0,
        "done": False,
        "info": {}
    }


def step(action):
    return {
        "observation": f"received: {action}",
        "reward": 1.0,
        "done": True,
        "info": {}
    }
