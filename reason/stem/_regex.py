# -*- coding: utf-8 -*-
"""Regex stemmer module.

API:
* *RegexStemmer* (class): For finding stems of the words of a string or list.
* *regex_stem* (function): For single word instant use.

Example:


"""
import re

from ._stemmer import BaseStemmer


class RegexStemmer(BaseStemmer):
    """Regex word stemmer

    Attributes:
        pattern (str): Regex pattern for finding word stem.

    """

    def __init__(self, pattern=None):
        """RegexStemmer Constructor.

        Sets a regex pattern for finding stem.

        You can define your own regex pattern in the format of string. If no
        pattern is given, sets a default pattern.

        Args:
            pattern (str, optional): Regex pattern to use for finding stems.

        Raises:
            Exception: If pattern is not a valid regex.

        """
        if pattern == None:
            self.pattern = r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment|ful)?$'
        else:
            try:
                re.compile(pattern)
                self.pattern = pattern
            except:
                raise ValueError('Pattern is not valid.')

    def _token_stem(self, token):
        assert isinstance(token, str), 'Token must be string.'
        stem, suffix = re.findall(self.pattern, token)[0]
        return stem

def regex_stem(word):
    """Regex stem function.

    Easy-to-use regex stem function.

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
    return RegexStemmer().stem(token)[0]
