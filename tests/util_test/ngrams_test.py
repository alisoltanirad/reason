from reason.util import ngrams, bigrams, trigrams


def test_bigrams():
    input = 'Reason is easy to use'
    output = [('Reason', 'is'), ('is', 'easy'), ('easy', 'to'), ('to', 'use')]
    assert bigrams(input) == output

def test_trigrams():
    input = 'Reason is easy to use'
    output = [('Reason', 'is', 'easy'), ('is', 'easy', 'to'),
              ('easy', 'to', 'use')]
    assert trigrams(input) == output

def test_ngrams():
    input = 'Reason is easy to use'
    output = [('Reason',), ('is',), ('easy',), ('to',), ('use',)]
    assert ngrams(input) == output

def test_ngrams_with_n():
    input = 'Reason is easy to use'
    output = [('Reason', 'is', 'easy', 'to'), ('is', 'easy', 'to', 'use')]
    assert ngrams(input, 4) == output
