from collections import Counter

from reason.tokenize import word_tokenize


class FreqDist:

    def __init__(self, data):
        tokens = word_tokenize(data)
        self._counter = Counter(tokens)

    def __str__(self):
        return str(self._counter)

    def most_common(self, n=1):
        return self._counter.most_common(n)

