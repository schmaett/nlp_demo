import gradio as gr


class Interface:
    def __init__(self, model):
        self.interface = gr.Interface.from_pipeline(model.pipe)
        self.interface.launch()
