# inference.py

def reset():
    return {"status": "ok", "message": "reset successful"}

def step(action):
    return {
        "observation": {"text": "hello"},
        "reward": 1.0,
        "done": True,
        "info": {}
    }

def main():
    print("Inference loaded")

if __name__ == "__main__":
    main()
