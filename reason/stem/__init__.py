# -*- coding: utf-8 -*-
"""stem package.

Word lemmatization and stemming.

API:

* PorterStemmer (class): Uses porter algorithm to find word stems.
* porter_stem (function): For instant stemming a word using porter algorithm.
* RegexStemmer (class): Uses regex pattern to find word stems.
* regex_stem (function): For instant stemming a word using regex pattern.

"""

from ._porter import PorterStemmer, porter_stem
from ._regex import RegexStemmer, regex_stem
