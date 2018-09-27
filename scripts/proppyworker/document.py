class Document(object):
    def __init__(self, text, prediction_prob_1=0.0):
        self.text = text
        self.prediction_prob_1 = prediction_prob_1
