# inference.py

def reset():
    """
    Must always return simple JSON-safe dict
    """
    return {
        "observation": "reset state",
        "info": {},
        "done": False
    }


def step(action):
    """
    OpenEnv-compatible step function
    """
    return (
        {"observation": f"received: {action}"},
        1.0,
        True,
        {}
    )


def main():
    print("Inference module loaded successfully")


if __name__ == "__main__":
    main()
