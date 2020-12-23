# -*- coding: utf-8 -*-
"""Porter stemmer module.

API:
* *PorterStemmer* (class): For finding stems of the words of a string or list.
* *porter_stem* (function): For single word instant use.

Example:


"""
import re

from ._stemmer import BaseStemmer


vowels = '[aeiouy]'


class PorterStemmer(BaseStemmer):
    """Porter stemmer

    Uses porter algorithm to find word stems.

    """

    def _word_stem(self, word):
        assert isinstance(word, str), 'Token must be string.'
        porter = _PorterAlgorithm(word)
        return porter.stem()


class _PorterAlgorithm:

    def __init__(self, word):
        self.word = word

    def stem(self):

        self._step1a()
        self._step1b()
        self._step1c()
        self._step2()
        self._step3()
        self._step4()
        self._step5a()
        self._step5b()

        return self.word

    def _step1a(self):
        if self.word.endswith('s'):
            if self.word.endswith('ss'):
                pass
            elif self.word.endswith('ies') or self.word.endswith('sses'):
                self.word = self.word[:-2]
            else:
                self.word = self.word[:-1]


    def _step1b(self):
        pass

    def _step1c(self):
        pass

    def _step2(self):
        pass

    def _step3(self):
        pass

    def _step4(self):
        pass

    def _step5a(self):
        pass

    def _step5b(self):
        pass


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
