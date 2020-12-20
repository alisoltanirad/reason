# Reason

[![License](https://img.shields.io/pypi/l/reason.svg)](https://github.com/alisoltanirad/Reason/blob/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/reason.svg)](https://pypi.org/project/reason/)
[![Downloads](https://img.shields.io/pypi/dw/reason)](https://pypi.org/project/reason/)
[![Lines](https://img.shields.io/tokei/lines/github/alisoltanirad/reason)](https://github.com/alisoltanirad/Reason/)
[![Activity](https://img.shields.io/github/last-commit/alisoltanirad/reason)](https://github.com/alisoltanirad/Reason/)

Python easy-to-use natural language processing toolbox.

## Install

Install latest stable version using pip:
```
pip install reason
```

## Quick-Start

Classification:

```python
>>> from reason.classify import NaiveBayesClassifier
>>> classifier = NaiveBayesClassifier(train_set)
>>> y_pred = classifier.classify(new_data)

>>> from reason.metrics import accuracy
>>> accuracy(y_true, y_pred)
0.9358
```

Tokenization:

```python
>>> from reason.tokenize import word_tokenize

>>> text = "Testing reason0.1.0, (on: 127.0.0.1). Cool stuff..."
>>> word_tokenize(text, 'alphanumeric')
['Testing', 'reason0.1.0', 'on', '127.0.0.1', 'Cool', 'stuff']
```

```python
>>> from reason.tokenize import sent_tokenize

>>> text = "Hey, what's up? I love using Reason library!"
>>> sents = sent_tokenize(text)
>>> for sent in sents:
...     print(sent)
Hey, what's up?
I love using Reason library!
```

Frequency Distribution:

```python
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
```

Ngrams:

```python
>>> sent = 'Reason is easy to use'

>>> from reason.util import bigrams
>>> bigrams(sent)
[('Reason', 'is'), ('is', 'easy'), ('easy', 'to'), ('to', 'use')]

>>> from reason.util import trigrams
>>> trigrams(sent)
[('Reason', 'is', 'easy'), ('is', 'easy', 'to'), ('easy', 'to', 'use')]

>>> from reason.util import ngrams
>>> ngrams(sent, 4)
[('Reason', 'is', 'easy', 'to'), ('is', 'easy', 'to', 'use')]
```

## Dependencies

- [NumPy](https://numpy.org)
Used to handle data
- [Pandas](https://pandas.pydata.org)
Used in classify package

Keep in mind *NumPy* will be automatically installed with *Reason*.

## License

MIT -- See [LICENSE](https://github.com/alisoltanirad/Reason/blob/main/LICENSE)
for details.
