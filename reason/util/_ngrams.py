from reason.tokenize import word_tokenize


def ngrams(input, n=1):
    """Ngrams function.

    Args:
        input (str or list of str): Text or corpus.
        n (int): Number.

    Returns:
        list of tuple: Ngrams.

    Raises:
        TypeError: If input type is not valid.

    Example:
        >>> sent = 'Reason is easy to use'
        >>> from reason.util import ngrams
        >>> ngrams(sent, 4)
        [('Reason', 'is', 'easy', 'to'), ('is', 'easy', 'to', 'use')]

    """
    try:
        data = word_tokenize(input)
    except TypeError:
        raise TypeError('Input type must be string or list of strings.')

    ngrams = list()
    for i in range(len(data) - (n - 1)):
        ngram = tuple([token for token in data[i : (i + n)]])
        ngrams.append(ngram)

    return ngrams


def bigrams(input):
    """Bigrams function.

    Uses Ngrams with n = 2.

    Args:
        input (str or list of str): Text or corpus.

    Returns:
        list of tuple: Bigrams.

    Example:
        >>> sent = 'Reason is easy to use'
        >>> from reason.util import bigrams
        >>> bigrams(sent)
        [('Reason', 'is'), ('is', 'easy'), ('easy', 'to'), ('to', 'use')]

    """
    return ngrams(input, 2)


def trigrams(input):
    """Trigrams function.

    Uses Ngrams with n = 3.

    Args:
        input (str or list of str): Text or corpus.

    Returns:
        list of tuple: Trigrams.

    Example:
        >>> sent = 'Reason is easy to use'
        >>> from reason.util import trigrams
        >>> trigrams(sent)
        [('Reason', 'is', 'easy'), ('is', 'easy', 'to'), ('easy', 'to', 'use')]

    """
    return ngrams(input, 3)
