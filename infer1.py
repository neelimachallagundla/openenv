def reset():
    return {
        "observation": "reset state",
        "reward": 0,
        "done": False,
        "info": {}
    }

def step(action):
    return {
        "observation": f"action received: {action}",
        "reward": 1.0,
        "done": True,
        "info": {}
    }
