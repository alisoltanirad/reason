import re

from ._stemmer import BaseStemmer


class PorterStemmer(BaseStemmer):
    """Porter stemmer

    Uses porter algorithm to find word stems.

    Example:
        >>> from reason.stem import PorterStemmer
        >>> text = 'watched birds flying'
        >>> stemmer = PorterStemmer()
        >>> stemmer.stem(text)
        ['watch', 'bird', 'fly']

    """

    def _word_stem(self, word):
        assert isinstance(word, str), 'Token must be string.'
        porter = _PorterAlgorithm(word)
        return porter.stem()


class _PorterAlgorithm:
    _vowels = frozenset(['a', 'e', 'i', 'o', 'u'])

    def __init__(self, word):
        self.word = word

    def stem(self, step=None):

        self._step1a()
        self._step1b()
        self._step1c()
        if step == 1:
            return self.word

        self._step2()
        if step == 2:
            return self.word

        self._step3()
        if step == 3:
            return self.word

        self._step4()
        if step == 4:
            return self.word

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

        elif (
            (self.word.endswith('ed') and self._contains_vowel(self.word[:-2]))
            or
            (self.word.endswith('ing') and self._contains_vowel(self.word[:-3]))
        ):
            self.word = re.sub('ed|ing$', '', self.word)

            if self.word[-2:] in ['at', 'bl', 'iz']:
                self.word += 'e'

            elif (
                self.word[-2] == self.word[-1] and
                self.word[-1] not in ['l', 's', 'z']
            ):
                self.word = self.word[:-1]

            elif self._ends_cvc(self.word) and self._measure(self.word) == 1:
                self.word += 'e'

    def _step1c(self):

        if self.word[-1] == 'y' and self._contains_vowel(self.word[:-1]):
            self.word = self.word[:-1] + 'i'

    def _step2(self):

        if self._measure(self.word[:-7]) > 0:

            if self.word[-7:] in ['iveness', 'fulness', 'ousness']:
                self.word = self.word[:-4]

            elif self.word[-7:] in ['ational', 'ization']:
                self.word = self.word[:-5] + 'e'

        if self._measure(self.word[:-6]) > 0:

            if self.word.endswith('tional'):
                self.word = self.word[:-2]

            elif self.word.endswith('biliti'):
                self.word = self.word[:-5] + 'le'

        if self._measure(self.word[:-5]) > 0:

            if self.word[-5:] in ['entli', 'ousli']:
                self.word = self.word[:-2]

            elif self.word[-5:] in ['alism', 'aliti']:
                self.word = self.word[:-3]

            elif self.word[-5:] in ['ation', 'iviti']:
                self.word = self.word[:-3] + 'e'

        if self._measure(self.word[:-4]) > 0:

            if self.word.endswith('izer'):
                self.word = self.word[:-1]

            elif self.word[-4:] in ['enci', 'anci', 'abli']:
                self.word = self.word[:-1] + 'e'

            elif self.word.endswith('alli'):
                self.word = self.word[:-2]

            elif self.word.endswith('ator'):
                self.word = self.word[:-2] + 'e'

        if self._measure(self.word[:-3]) > 0 and self.word.endswith('eli'):
            self.word = self.word[:-2]

    def _step3(self):

        if self._measure(self.word[:-5]) > 0:

            if self.word[-5:] in ['icate', 'alize', 'iciti']:
                self.word = self.word[:-3]

            elif self.word.endswith('ative'):
                self.word = self.word[:-5]

        if self._measure(self.word[:-4]) > 0:

            if self.word.endswith('ical'):
                self.word = self.word[:-2]

            elif self.word.endswith('ness'):
                self.word = self.word[:-4]

        if self._measure(self.word[:-3]) > 0 and self.word.endswith('ful'):
            self.word = self.word[:-3]

    def _step4(self):

        if self._measure(self.word[:-5]) > 1 and self.word.endswith('ement'):
            self.word = self.word[:-5]

        if (
            self._measure(self.word[:-4]) > 1 and
            self.word[-4:] in ['ance', 'ence', 'able', 'ible', 'ment']
        ):
            self.word = self.word[:-4]

        if (
            self._measure(self.word[:-3]) > 1 and (
                self.word[-3:] in [
                    'ant', 'ent', 'ism', 'ate', 'iti', 'ous', 'ive', 'ize'
                ] or
                self.word.endswith('ion') and self.word[-4] in ['s', 't']
            )
        ):
            self.word = self.word[:-3]

        if (
            self._measure(self.word[:-2]) > 1 and
            self.word[-2:] in ['al', 'er', 'ic', 'ou']
        ):
            self.word = self.word[:-2]

    def _step5a(self):

        if (
            self.word[-1] == 'e' and (
                self._measure(self.word[:-1]) > 1 or (
                    self._measure(self.word[:-1]) == 1 and
                    not self._ends_cvc(self.word[:-1])
                )
            )
        ):
            self.word = self.word[:-1]

    def _step5b(self):

        if (
            self.word[-1] == 'l' and
            self.word[-2] == self.word[-1] and
            self._measure(self.word[:-2])
        ):
            self.word = self.word[:-1]

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
        TypeError: If input word is not string.

    """
    if not isinstance(word, str):
        raise TypeError('Porter_stem function input word must be string.')
    token = word.split(' ')[0]
    return PorterStemmer().stem(token)[0]
