# -*- coding: utf-8 -*-
"""util package.

Language processing utilities.

API:

* *ngrams* (function): Get input ngrams using given n.
* *bigrams* (function): Get input bigrams (ngrams with n=2).
* *trigrams* (function): Get input trigrams (ngrams with n=3).

"""

from ._ngrams import ngrams, bigrams, trigrams
