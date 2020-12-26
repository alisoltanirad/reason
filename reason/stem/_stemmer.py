from reason.tokenize import word_tokenize


class BaseStemmer:
    """Base Stemmer

    Base class for stemmers

    """

    def stem(self, corpus):
        """Stem finding method.

        Tokenize input text, then finds token stems.

        Args:
            corpus (str or list of str): Text.

        Returns:
            list: Stems.

        Raises:
            TypeError: If input is not string or a list of strings.

        """
        try:
            tokens = word_tokenize(corpus)
        except TypeError:
            raise TypeError(
                'Stemmer input must be string or a list of strings.'
            )
        stems = list()
        for token in tokens:
            if token.isalpha():
                stems.append(self._word_stem(token.lower()))
            else:
                stems.append(token.lower())
        return stems
