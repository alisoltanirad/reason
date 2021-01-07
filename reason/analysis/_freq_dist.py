from collections import Counter
from copy import deepcopy

from reason.tokenize import word_tokenize


class FreqDist:
    """Frequency Distribution

    Counts token frequencies.

    Example:
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
    def __init__(self, data):
        """FreqDist Constructor

        Tokenize input data and creates a counter dictionary.

        Args:
            data (str or list of str): Text or corpus.

        Raises:
            TypeError: If data is not valid.

        """
        try:
            tokens = word_tokenize(data)
        except TypeError:
            raise TypeError('FreqDist input must be string or list of strings.')

        self._counter = Counter(tokens)

    def __repr__(self):
        return 'Frequency Distribution\n' + 'Most-Common: ' + \
            str(self.most_common(10))

    def __getitem__(self, key):
        return self._counter[key]

    def __setitem__(self, key, value):
        self._counter[key] = value

    def __delitem__(self, key):
        del self._counter[key]

    def get_data(self):
        """Get data method

        Converts items to tuples then returns them in a list.

        Returns:
            list of tuple: Tokens + frequencies

        """
        return [
            (key, value) for key, value in self._counter.items()
        ]

    def most_common(self, n=1):
        """Most common method

        Most common tokens and their frequencies. if n is not specified, returns
        one token.

        Args:
            n (int, optional): Number of tokens.

        Returns:
            list: Most common tokens + frequencies

        Raises:
            TypeError: If n is not an integer.

        """
        if isinstance(n, int):
            return self._counter.most_common(n)
        else:
            raise TypeError('N must be an integer.')

    def copy(self):
        """FreqDist Copy

        Recursively makes a deep copy of itself.

        Returns:
            FreqDist: A copy of self object

        """
        return deepcopy(self)


class ConditionalFreqDist:
    """Conditional Frequency Distribution

    Counts token frequencies with given conditions.

    """
    def __init__(self, data):
        """ConditionalFreqDist Constructor

        Checks if data is valid then creates a counter dictionary.

        Args:
            data (list of tuple): Tuples (word + condition)

        Raises:
            TypeError: If data is not valid.

        """
        try:
            pairs = list(data)
            assert all(isinstance(i, tuple) for i in pairs)
        except AssertionError:
            raise ValueError(
                'Input data must be list of tuples (word, condition).'
            )

        self._counter = Counter(pairs)

    def __repr__(self):
        return 'Frequency Distribution\n' + 'Most-Common: ' + \
            str(self.most_common(10))

    def __getitem__(self, key):
        return self._counter[key]

    def __setitem__(self, key, value):
        self._counter[key] = value

    def __delitem__(self, key):
        del self._counter[key]

    def get_data(self):
        """Get data method

        Converts items to tuples then returns them in a list.

        Returns:
            list of tuple: Tokens + frequencies

        """
        return [
            (key, value) for key, value in self._counter.items()
        ]
