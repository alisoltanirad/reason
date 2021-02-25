# Reason

[![License](https://img.shields.io/pypi/l/reason.svg)](https://github.com/alisoltanirad/Reason/blob/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/reason.svg)](https://pypi.org/project/reason/)
[![Downloads](https://pepy.tech/badge/reason)](https://pepy.tech/project/reason)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=alisoltanirad_reason&metric=ncloc)](https://sonarcloud.io/dashboard?id=alisoltanirad_reason)
[![Activity](https://img.shields.io/github/last-commit/alisoltanirad/reason)](https://github.com/alisoltanirad/Reason/)

Python easy-to-use natural language processing toolbox with powerful integrated
machine learning packages.


## Packages

- **classify**  
Naive bayes classifier
- **cluster**  
Kmeans++ and DBSCAN clusterer, elbow method
- **metrics**  
Confusion matrix, accuracy
- **tag**  
POS tagger, regex, lookup and default tagging tools
- **tokenize**  
Regex word and sentence tokenizer
- **stem**  
Porter and regex stemmer
- **analysis**  
Frequency distribution
- **util**  
Bigrams, trigrams and ngrams


## Install

Install latest stable version using pip:
```
pip install reason
```


## Dependencies

- [NumPy](https://numpy.org)  
Used to handle data
- [Pandas](https://pandas.pydata.org)  
Used in classify and cluster packages

Keep in mind *NumPy* will be automatically installed with *Reason*.


## License

MIT -- See [LICENSE](https://github.com/alisoltanirad/Reason/blob/main/LICENSE)
for details.
