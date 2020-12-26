# -*- coding: utf-8 -*-
"""Preprocess module.

API:
* *preprocess* (function): Easy-to-use preprocessing tool.

"""
from .tokenize import sent_tokenize, word_tokenize
from .stem import PorterStemmer


def preprocess(corpus):
    """Preprocess function.

    Tokenize input corpus to sentences and words, then finds token stems
    using porter stemmer.

    Args:
        corpus (str or list of str): Text.

    Returns:
        list: Preprocessed text.

    Raises:
        TypeError: If input is not string or a list of strings.

    Example:
        >>> from reason import preprocess
        >>> text = "What's up? I love using Reason library!"
        >>> preprocess(text)
        [["what's", 'up', '?'], ['i', 'love', 'us', 'reason', 'librari', '!']]

    """
    try:
        sents = sent_tokenize(corpus)
    except TypeError:
        raise TypeError(
            'Preprocess input must be string or a list of strings.'
        )

    stemmer = PorterStemmer()
    output = list()
    for sent in sents:
        stems = list()
        for token in word_tokenize(sent):
            stems += stemmer.stem(token)
        output.append(stems)

    return output
