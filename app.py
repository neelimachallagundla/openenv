import gradio as gr
from inference import reset

def test():
    return reset()

gr.Interface(fn=test, inputs=[], outputs="text").launch(server_name="0.0.0.0", server_port=7860)
