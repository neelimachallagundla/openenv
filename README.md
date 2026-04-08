## 🔗 Submission Notes

This repository is submitted as part of the project evaluation.

### ✔ Requirements Followed

* Uses OpenAI client (`from openai import OpenAI`)
* Uses environment variables:

  * API_BASE_URL
  * MODEL_NAME
  * HF_TOKEN
* Implements structured logging:
  START
  STEP
  END

### ⚙️ Environment Variables Setup

Set the following environment variables before running:

```bash
export API_BASE_URL="your_api_base_url"
export MODEL_NAME="your_model_name"
export HF_TOKEN="your_huggingface_token"
```

For Windows (PowerShell):

```powershell
setx API_BASE_URL "your_api_base_url"
setx MODEL_NAME "your_model_name"
setx HF_TOKEN "your_huggingface_token"
```

### ▶️ Run the Project

```bash
# For most systems
python run_baseline.py

# For Windows (if python doesn't work)
py run_baseline.py
```

### 🚀 Deployment

The project is deployed on Hugging Face Spaces.

---

# 🚀 OpenEnv Real-World Task Simulation

## 📌 Overview

This project implements an **OpenEnv-compliant environment** that simulates real-world human workflows.
The goal is to evaluate how well AI agents can perform structured tasks with clear objectives, feedback, and measurable outcomes.

---

## 🎯 Problem Statement

Modern AI models often struggle with **structured real-world workflows** such as:

* Email triage
* Data cleaning
* Code review

These tasks require step-by-step reasoning, decision-making, and correctness verification.

---

## 💡 Our Solution

We designed a modular environment following the **OpenEnv specification**, including:

* Standardized `reset()`, `step()`, and `state()` methods
* Typed observation, action, and reward models
* Deterministic evaluation using programmatic graders
* Incremental reward system for better agent feedback

---

## 🧪 Tasks Implemented

### 🟢 1. Email Triage (Easy)

* Classifies emails into categories (urgent, spam, normal)
* Rewards correct classification
* Penalizes incorrect actions

---

### 🟡 2. Data Cleaning (Medium)

* Removes duplicate entries
* Handles missing values (`None`)
* Rewards fully cleaned datasets

---

### 🔴 3. Code Review (Hard)

* Identifies bugs in a given code snippet
* Matches detected issues with expected ones
* Partial rewards for partially correct answers

---

## ⚙️ OpenEnv Compliance

This project fully follows OpenEnv standards:

* ✔ `step(action)` → returns `(observation, reward, done, info)`
* ✔ `reset()` → initializes environment
* ✔ `state()` → returns current state
* ✔ `openenv.yaml` included
* ✔ Typed models using Pydantic

---

## 🏆 Reward Design

* Provides **incremental feedback** during execution
* Encourages correct actions
* Penalizes incorrect or irrelevant actions
* Ensures deterministic scoring

---

## 🤖 Baseline Agent

A baseline script (`run_baseline.py`) is included:

* Executes all tasks sequentially
* Produces a reproducible reward score

### ▶️ Run the project

```bash
# For most systems
python run_baseline.py

# For Windows
py run_baseline.py
```

### 📊 Sample Output

```
Total Reward: 2.16
```

---

## 📂 Project Structure

```
Openenv/
├── env_code.py
├── env_data.py
├── env_email.py
├── graders.py
├── openenv.yaml
├── README.md
└── run_baseline.py
```

---

## 🚀 Key Highlights

* Real-world task simulation (non-toy problems)
* Multi-task environment with increasing difficulty
* Deterministic and reproducible evaluation
* Clean and modular design

---

## 📈 Future Improvements

* Add more complex workflows
* Introduce dynamic task variations
* Improve agent intelligence for better performance

---

## 🧠 Conclusion

This project demonstrates how AI agents can be evaluated in structured environments that reflect **real-world applications**, moving beyond simple benchmarks toward practical usability.

