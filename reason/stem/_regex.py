import re

from ._stemmer import BaseStemmer


class RegexStemmer(BaseStemmer):
    """Regex word stemmer

    Attributes:
        pattern (str): Regex pattern for finding word stem.

    Example:
        >>> from reason.stem import regex_stem
        >>> regex_pattern = r'^(.*?)(ous)?$'
        >>> regex_stem('dangerous', regex_pattern)
        danger

    """

    def __init__(self, pattern=None):
        """RegexStemmer Constructor.

        Sets a regex pattern for finding stem.

        You can define your own regex pattern in the format of string. If no
        pattern is given, sets a default pattern.

        Args:
            pattern (str, optional): Regex pattern to use for finding stems.

        Raises:
            TypeError: If pattern is not a valid regex.

        """
        if pattern == None:
            self.pattern = r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment|ful)?$'
        else:
            try:
                re.compile(pattern)
                self.pattern = pattern
            except TypeError:
                raise TypeError(
                    'Pattern must be string or compiled regex pattern.'
                )

    def _word_stem(self, word):
        assert isinstance(word, str), 'Token must be string.'
        stem, suffix = re.findall(self.pattern, word)[0]
        return stem

def regex_stem(word, pattern=None):
    """Regex stem function.

    Easy-to-use regex stem function.

    Args:
        word (str): Single word.
        pattern (str, optional): Regex pattern.

    Returns:
        str: Stem.

    Raises:
        TypeError: If input word is not string.

    """
    if not isinstance(word, str):
        raise TypeError('Input word must be string.')
    token = word.split(' ')[0]
    return RegexStemmer(pattern).stem(token)[0]
