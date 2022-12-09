from nlp_demo.interface import Interface
from nlp_demo.model import SummarizationModel


def summarization_main():
    model = SummarizationModel()
    Interface(model)


if __name__ == "__main__":
    summarization_main()
