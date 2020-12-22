from .tokenize import sent_tokenize


def preprocess(text):
    tokens = sent_tokenize(text)
    return tokens
