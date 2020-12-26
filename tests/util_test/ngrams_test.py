import pytest

from reason.util import ngrams, bigrams, trigrams


@pytest.fixture
def input_value():
    input_value = 'Reason is easy to use'
    return input_value


def test_bigrams(input_value):
    output = [('Reason', 'is'), ('is', 'easy'), ('easy', 'to'), ('to', 'use')]
    assert bigrams(input_value) == output

def test_trigrams(input_value):
    output = [('Reason', 'is', 'easy'), ('is', 'easy', 'to'),
              ('easy', 'to', 'use')]
    assert trigrams(input_value) == output

def test_ngrams(input_value):
    output = [('Reason',), ('is',), ('easy',), ('to',), ('use',)]
    assert ngrams(input_value) == output

def test_ngrams_with_n(input_value):
    output = [('Reason', 'is', 'easy', 'to'), ('is', 'easy', 'to', 'use')]
    assert ngrams(input_value, 4) == output
