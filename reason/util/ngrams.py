from reason.tokenize import word_tokenize


def ngrams(input, n):
    if isinstance(input, str):
        data = word_tokenize(input)
    else:
        try:
            data = list(input)
        except TypeError:
            raise Exception('Input type is not supported.')

    ngrams = list()
    for i in range(len(data) - (n - 1)):
        ngram = tuple([token for token in data[i : (i + n)]])
        ngrams.append(ngram)

    return ngrams


def bigrams(input):
    return ngrams(input, 2)


def trigrams(input):
    return ngrams(input, 3)
