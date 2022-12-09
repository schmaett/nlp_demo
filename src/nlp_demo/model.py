from transformers import AutoModelForQuestionAnswering
from transformers import AutoModelForSeq2SeqLM
from transformers import AutoTokenizer
from transformers import pipeline


class QAModel:

    model_name = "deepset/gelectra-large-germanquad"
    task = "question-answering"

    def __init__(self):
        tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        model = AutoModelForQuestionAnswering.from_pretrained(self.model_name)
        self.pipe = pipeline(self.task, model=model, tokenizer=tokenizer)

    def apply(self, context, question):
        result = self.pipe(context=context, question=question)
        return result["answer"]


class SummarizationModel:

    model_name = "Einmalumdiewelt/T5-Base_GNAD"
    task = "summarization"

    def __init__(self):
        tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name)
        self.pipe = pipeline(self.task, model=model, tokenizer=tokenizer)

    def apply(self, text):
        result = self.pipe(text)
        return result["summary_text"]
