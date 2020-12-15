# -*- coding: utf-8 -*-
"""Tokenize package.

API:

* *WordTokenizer* (class): For frequent word tokenizing use with an specific
regex pattern.
* *word_tokenize* (function): For instant word tokenizing use.

* *SentTokenizer* (class): For frequent sentence tokenizing use.
* *sent_tokenize* (function): For instant use.

"""

from .word_tokenize import WordTokenizer, word_tokenize
from .sent_tokenize import SentTokenizer, sent_tokenize
