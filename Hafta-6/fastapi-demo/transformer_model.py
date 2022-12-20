from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

class Sentiment_Analyser:
    def __init__(self):
        model = AutoModelForSequenceClassification.from_pretrained('azizbarank/distilbert-base-turkish-cased-sentiment')
        tokenizer = AutoTokenizer.from_pretrained('azizbarank/distilbert-base-turkish-cased-sentiment')
        self.pipeline = pipeline("sentiment-analysis", tokenizer=tokenizer, model=model)
        self.text_labels = {'LABEL_1':'positive', 'LABEL_0':'negative'}
    
    def predict(self, text):
        res = self.pipeline(text)[0]
        res['label'] = self.text_labels[res['label']]
        return res