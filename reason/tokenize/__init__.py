# -*- coding: utf-8 -*-
"""tokenize package.

Word and sentence tokenization.

API:

* WordTokenizer (class): For frequent word tokenizing use with an specific
regex pattern.
* word_tokenize (function): For instant word tokenizing use.
* SentTokenizer (class): For frequent sentence tokenizing use.
* sent_tokenize (function): For instant use.

"""

from ._word_tokenize import WordTokenizer, word_tokenize
from ._sent_tokenize import SentTokenizer, sent_tokenize
