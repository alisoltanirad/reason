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

Tokenize text:
```python
>>> from reason.tokenize import word_tokenize

>>> text = "Testing reason0.1.0, (on: 127.0.0.1). Cool stuff..."
>>> word_tokenize(text, 'alphanumeric')
['Testing', 'reason0.1.0', 'on', '127.0.0.1', 'Cool', 'stuff']
```

## License

MIT -- See [LICENSE](https://github.com/alisoltanirad/Reason/blob/main/LICENSE) 
for details.
