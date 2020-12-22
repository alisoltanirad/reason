import re

from reason.tokenize import word_tokenize


class RegexStemmer:
    _pattern = r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$'

    def stem(self, input):
        try:
            tokens = word_tokenize(input)
        except TypeError:
            raise Exception(
                'Stemmer input must be string or a list of strings.'
            )
        stems = list()
        for token in tokens:
            stems.append(
                self._token_stem(token)
            )
        return stems

    def _token_stem(self, token):
        assert isinstance(token, str), 'Token must be string.'
        stem, suffix = re.findall(self._pattern, token)[0]
        return stem

def regex_stem(word):
    if not isinstance(word, str):
        raise Exception('Input word must be string.')
    token = word.split(' ')[0]
    return RegexStemmer().stem(token)[0]
