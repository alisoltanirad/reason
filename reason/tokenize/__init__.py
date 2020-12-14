# -*- coding: utf-8 -*-
"""Tokenize package.

API:
* *WordTokenizer* class: For frequent word tokenizing use with an specific
regex pattern.
* *word_tokenize* function: For instant word tokenizing use.

Example:
    Tokenize an string:

        >>> from reason.tokenize import word_tokenize

        >>> sentence = "Testing reason0.1.0, (on: 127.0.0.1). Cool stuff..."
        >>> word_tokenize(sentence, 'alphanumeric')
        ['Testing', 'reason0.1.0', 'on', '127.0.0.1', 'Cool', 'stuff']

"""

from .word_tokenize import WordTokenizer, word_tokenize
