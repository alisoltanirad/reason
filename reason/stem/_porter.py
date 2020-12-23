# -*- coding: utf-8 -*-
"""Porter stemmer module.

API:
* *PorterStemmer* (class): For finding stems of the words of a string or list.
* *porter_stem* (function): For single word instant use.

Example:


"""
import re

from ._stemmer import BaseStemmer

cons = '[^aeiou]'
vowels = '[aeiouy]'
cons_seq = '[^aeiouy]+'
vowels_seq = '[aeiou]+'


class PorterStemmer(BaseStemmer):
    """Porter stemmer

    Uses porter algorithm to find word stems.

    """

    def _word_stem(self, word):
        assert isinstance(word, str), 'Token must be string.'
        porter = _PorterAlgorithm(word)
        return porter.stem()


class _PorterAlgorithm:
    _vowels = frozenset(['a', 'e', 'i', 'o', 'u'])

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
                return
            elif self.word.endswith('ies') or self.word.endswith('sses'):
                self.word = self.word[:-2]
            else:
                self.word = self.word[:-1]


    def _step1b(self):
        if self.word.endswith('eed'):
            if self._measure(self.word[:-3]) > 0:
                self.word = self.word[:-1]

        elif self.word.endswith('ed') and self._contains_vowel(self.word[:-2]) \
                or self.word.endswith('ing') and \
                self._contains_vowel(self.word[:-3]):

            self.word = re.sub('ed|ing$', '', self.word)

            if self.word[-2:] in ['at', 'bl', 'iz']:
                self.word += 'e'

            elif self.word[-2] == self.word[-1]:
                if self.word[-1] not in ['l', 's', 'z']:
                    self.word = self.word[:-1]

            elif self._ends_cvc(self.word) and self._measure(self.word) == 1:
                self.word += 'e'

    def _step1c(self):
        if self.word[-1] == 'y' and self._contains_vowel(self.word[:-1]):
            self.word = self.word[:-1] + 'i'

    def _step2(self):
        if self._measure(self.word[:-7]) > 0:

            if self.word.endswith('iveness') or self.word.endswith('fulness') \
                    or self.word.endswith('ousness'):
                self.word = self.word[:-4]

            elif self.word.endswith('ational') or self.word.endswith('ization'):
                self.word = self.word[:-5] + 'e'

        if self._measure(self.word[:-6]) > 0:

            if self.word.endswith('tional'):
                self.word = self.word[:-2]

            elif self.word.endswith('biliti'):
                self.word = self.word[:-5] + 'le'

        if self._measure(self.word[:-5]) > 0:

            if self.word.endswith('entli') or self.word.endswith('ousli'):
                self.word = self.word[:-2]

            elif self.word.endswith('alism') or self.word.endswith('aliti'):
                self.word = self.word[:-3]

            elif self.word.endswith('ation') or self.word.endswith('iviti'):
                self.word = self.word[:-3] + 'e'

        if self._measure(self.word[:-4]) > 0:

            if self.word.endswith('izer'):
                self.word = self.word[:-1]

            elif self.word.endswith('enci') or self.word.endswith('anci') or \
                self.word.endswith('abli'):
                self.word = self.word[:-1] + 'e'

            elif self.word.endswith('alli'):
                self.word = self.word[:-2]

            elif self.word.endswith('ator'):
                self.word = self.word[:-2] + 'e'

        if self._measure(self.word[:-3]) > 0 and self.word.endswith('eli'):
            self.word = self.word[:-2]

    def _step3(self):
        pass

    def _step4(self):
        pass

    def _step5a(self):
        pass

    def _step5b(self):
        pass

    def _measure(self, stem):
        cv_sequence = ''

        for i in range(len(stem)):
            if self._is_consonant(stem, i):
                cv_sequence += 'c'
            else:
                cv_sequence += 'v'

        return cv_sequence.count('vc')

    def _is_consonant(self, word, i):
        if word[i] in self._vowels:
            return False

        if word[i] == 'y':
            if i == 0:
                return True
            else:
                return not self._is_consonant(word, i - 1)

        return True

    def _contains_vowel(self, word):
        for i in range(len(word)):
            if not self._is_consonant(word, i):
                return True

        return False

    def _ends_cvc(self, word):
        return (
            len(word) >= 3 and
            self._is_consonant(word, len(word) - 3) and
            not self._is_consonant(word, len(word) - 2) and
            self._is_consonant(word, len(word) - 1) and
            word[-1] not in ['w', 'x', 'y']
        )


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
