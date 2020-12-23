# -*- coding: utf-8 -*-
"""Porter stemmer module.

API:
* *PorterStemmer* (class): For finding stems of the words of a string or list.
* *porter_stem* (function): For single word instant use.

Example:


"""
import re

from ._stemmer import BaseStemmer


class PorterStemmer(BaseStemmer):
    """Porter stemmer

    Uses porter algorithm to find word stems.

    """

    def _token_stem(self, token):
        assert isinstance(token, str), 'Token must be string.'

def porter_stem(word):
    """Porter stem function.

    Easy-to-use porter stem function.

    Args:
        word (str): Single word.

    Returns:
        str: Stem.

    Raises:
        Exception: If input word is not string.

    """
    if not isinstance(word, str):
        raise TypeError('Input word must be string.')
    token = word.split(' ')[0]
    return PorterStemmer().stem(token)[0]
