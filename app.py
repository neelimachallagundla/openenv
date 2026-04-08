import gradio as gr
from run_baseline import main as run_baseline


# ----------------------------
# Run full simulation
# ----------------------------
def run_full_simulation():
    try:
        result = run_baseline()
        return f"✅ Simulation Completed\n\n{result}"
    except Exception as e:
        return f"❌ Error occurred:\n{str(e)}"


# ----------------------------
# Simple demo explanation
# ----------------------------
def show_info():
    return """
    🚀 OpenEnv Real-World Task Simulation

    This system evaluates AI agents on structured tasks:

    🟢 Email Triage (classification)
    🟡 Data Cleaning (preprocessing)
    🔴 Code Review (bug detection)

    The baseline agent runs all tasks and returns a total reward score.
    """


# ----------------------------
# Gradio UI
# ----------------------------
with gr.Blocks(title="OpenEnv Hackathon Demo") as demo:

    gr.Markdown("# 🚀 OpenEnv Real-World Task Simulation")
    gr.Markdown("Evaluate AI agents on structured real-world workflows")

    with gr.Tab("📌 Overview"):
        gr.Markdown(show_info())

    with gr.Tab("▶ Run Simulation"):
        run_btn = gr.Button("Run Baseline Agent")
        output_box = gr.Textbox(label="Output", lines=10)

        run_btn.click(
            fn=run_full_simulation,
            inputs=None,
            outputs=output_box
        )

    with gr.Tab("📊 About Tasks"):
        gr.Markdown("""
        ### 🟢 Email Triage
        - Classifies emails into categories

        ### 🟡 Data Cleaning
        - Handles missing values & duplicates

        ### 🔴 Code Review
        - Detects bugs in code snippets
        """)

demo.launch()
