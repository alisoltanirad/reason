# -*- coding: utf-8 -*-
"""Word tokenize module.

API:
* *WordTokenizer* class: For frequent use with an specific regex pattern.
* *word_tokenize* function: For instant use.

Example:
    Tokenize an string:

        >>> from reason.tokenize import word_tokenize

        >>> sentence = "Testing reason0.1.0, (on: 127.0.0.1). Cool stuff..."
        >>> word_tokenize(sentence, 'alphanumeric')
        ['Testing', 'reason0.1.0', 'on', '127.0.0.1', 'Cool', 'stuff']

"""
import re


re_collection = {
    'etc': r"[\.]{3}",
    'ideogram': r"[:;][\)\(\*\|o0]+|[\)\(\*\|o0][:;]+|[-@$\^\*]_[-@$\^\*]",
    'word': r"\w+(?:['\.]\w+)*",
    'other': r"[^\w\s]",
}
"""dict: General regex collection.
"""

re_micro_collection = {
    'alpha': r"[A-Za-z]+(?:'[A-Za-z]+)?",
    'numeric': r"[0-9]+(?:,[0-9]+)*(?:\.[0-9]+)*",
}
"""dict: Alpha and numeric regex collection.
"""

re_pure_collection = {
    'alpha': r"[A-Za-z]+",
    'numeric': r"[0-9]+",
}
"""dict: Pure alpha and numeric regex collection.
"""

regex_patterns = {
    'default': '|'.join([re for re in re_collection.values()]),
    'word': re_collection['word'],
    'ideogram': re_collection['ideogram'],
    'alphanumeric': re_collection['word'],
    'alpha': re_micro_collection['alpha'],
    'alpha-pure': re_pure_collection['alpha'],
    'numeric': re_micro_collection['numeric'],
    'numeric-pure': re_pure_collection['numeric'],
    'non-alphanumeric': '|'.join([
        re_collection['etc'], re_collection['ideogram'], re_collection['other']
    ]),
}
"""dict: Regex patterns used for tokenizing.
"""


class WordTokenizer:
    """Regex Word Tokenizer

    Attributes:
        pattern (str): Regex pattern for tokenizing.

    """

    def __init__(self, pattern=None):
        """WordTokenizer Constructor.

        Sets a regex pattern for tokenizing.

        Ready-to-use choices for pattern are: 'default', 'word', 'ideogram',
        'alphanumeric', 'alpha', 'alpha-pure', 'numeric', 'numeric-pure',
        'non-alphanumeric'.

        You can also define your own regex pattern in the format of string.

        Args:
            pattern (str, optional): Regex pattern to use for tokenizing

        Raises:
            Exception: If pattern is not a valid regex.

        """
        if pattern == None:
            self.pattern = regex_patterns['default']
        elif pattern in regex_patterns.keys():
            self.pattern = regex_patterns[pattern]
        else:
            try:
                re.compile(pattern)
                self.pattern = pattern
            except:
                raise Exception('Pattern is not valid.')

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
        if type(input) == str:
            text = input
        else:
            try:
                text = ' '.join(input)
            except TypeError:
                raise Exception(
                    'Tokenize input must be string or a list of strings.'
                )

        return re.findall(self.pattern, text)


def word_tokenize(input, pattern='default'):
    """Tokenize text function.

    Easy-to-use word tokenize function.

    Args:
        input (str or list of str): Text to tokenize.
        pattern (str, optional): Regex pattern to use for tokenizing.

    Returns:
        list: Tokens.

    """
    return WordTokenizer(pattern).tokenize(input)