# -*- coding: utf-8 -*-
"""Sentence tokenize module.

API:
* *SentTokenizer* (class): For frequent sentence tokenizing use.
* *sent_tokenize* (function): For instant use.

"""
import pickle

from nltk import NaiveBayesClassifier

from ._sent_classify import punc_features
from .word_tokenize import WordTokenizer


class SentTokenizer:
    """Sentence Tokenizer
    """

    def __init__(self):
        """SentTokenizer Constructor.
        """
        with open('sent_classifier.pickle', 'rb') as f:
            self._classifier = pickle.load(f)

    def tokenize(self, input):
        """Tokenize text method.

        Tokenize input text

        Args:
            input (str or list of str): Text to tokenize.

        Returns:
            list: Tokens.

        Raises:
            Exception: If input is not string or a list of strings.

        """
        wt = WordTokenizer()
        if type(input) == str:
            tokens = wt.tokenize(input)
        else:
            try:
                tokens = wt.tokenize(' '.join(input))
            except TypeError:
                raise Exception(
                    'Tokenize input must be string or a list of strings.'
                )

        start = 0
        sents = list()

        for i, token in enumerate(tokens):
            if token in '.?!' and self._classifier.classify(
                    punc_features(tokens, i)
            ) == True:
                sents.append(tokens[start : i + 1])
                start = i + 1

        if start < len(tokens):
            sents.append(tokens[start:])

        return sents


def sent_tokenize(input):
    """Tokenize text function.

        Easy-to-use sentence tokenize function.

        Args:
            input (str or list of str): Text to tokenize.

        Returns:
            list: Tokens.

        """
    return SentTokenizer().tokenize(input)


if __name__ == '__main__':
    sent_tokenize('Hi. I am Ali.')