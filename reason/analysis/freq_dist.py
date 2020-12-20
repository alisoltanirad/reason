from collections import Counter
from copy import deepcopy

from reason.tokenize import word_tokenize


class FreqDist:

    def __init__(self, data):
        tokens = word_tokenize(data)
        self._counter = Counter(tokens)

    def __str__(self):
        return str(self._counter)

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
