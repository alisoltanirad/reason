# -*- coding: utf-8 -*-
"""Frequency distribution module.

API:
* *FreqDist* (class): Frequency distribution.

Example:
    Find word frequencies:
        >>> from reason.analysis import FreqDist

        >>> words = ['hey', 'hey', 'oh', 'oh', 'oh', 'yeah']
        >>> fd = FreqDist(words)

        >>> fd
        Frequency Distribution
        Most-Common: [('oh', 3), ('hey', 2), ('yeah', 1)]
        >>> fd.most_common(2)
        [('oh', 3), ('hey', 2)]
        >>> fd['yeah']
        1

"""
from collections import Counter
from copy import deepcopy

from reason.tokenize import word_tokenize


class FreqDist:

    def __init__(self, data):
        tokens = word_tokenize(data)
        self._counter = Counter(tokens)

    def __str__(self):
        return 'Frequency Distribution\n' + 'Most-Common: ' + \
            str(self.most_common(10))

    def __getitem__(self, key):
        return self._counter[key]

    def __setitem__(self, key, value):
        self._counter[key] = value

    def __delitem__(self, key):
        del self._counter[key]

    def most_common(self, n=1):
        return self._counter.most_common(n)

    def copy(self):
        return deepcopy(self)
