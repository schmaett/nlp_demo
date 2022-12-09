# nlp_demo
This is a minimal example of an NLP-demo site for BFH. It implements text summarization and question answering, and relies for Huggingface for inference, and Gradio for the interface.

## Installation
This project uses the poetry package manager: https://python-poetry.org/. It can be installed with pip: 
`pip install poetry`

Then, you can install the virtual environment used for this project using:
`poetry install`
And you're ready to go!

## Running the code
For text summarization:
`poetry run python src/nlp_demo/summarization.py`

For QA:
`poetry run python src/nlp_demo/question_answering.py`
