# inference.py

import os
from openai import OpenAI

# Environment variables
API_BASE_URL = os.getenv("API_BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")
HF_TOKEN = os.getenv("HF_TOKEN")

def main():
    print("START")

    # Your actual logic (calling baseline for now)
    from run_baseline import main as run_main
    run_main()

    print("END")

if __name__ == "__main__":
    main()
