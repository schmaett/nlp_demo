from nlp_demo.model import QAModel
from nlp_demo.interface import Interface

def qa_main():
    model = QAModel()
    Interface(model)


if __name__=="__main__":
    qa_main()