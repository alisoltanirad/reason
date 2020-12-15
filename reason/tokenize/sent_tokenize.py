# -*- coding: utf-8 -*-
"""Sentence tokenize module.

API:
* *SentTokenizer* (class): For frequent sentence tokenizing use.
* *sent_tokenize* (function): For instant use.

"""
class SentTokenizer:
    """Sentence Tokenizer
    """

    def __init__(self):
        """SentTokenizer Constructor.
        """
        pass

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
        pass


def sent_tokenize(input):
    """Tokenize text function.

        Easy-to-use sentence tokenize function.

        Args:
            input (str or list of str): Text to tokenize.

        Returns:
            list: Tokens.

        """
    return SentTokenize().tokenize(input)