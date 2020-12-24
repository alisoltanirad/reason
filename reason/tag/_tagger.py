from reason.tokenize import word_tokenize


class BaseTagger:
    """Base Tagger

    Base class for taggers.

    """

    def tag(self, corpus):
        """Tagging method.

        First tokenize input text, then finds tags and returns (word, tag)
        tuples.

        Args:
            corpus (str or list of str): Text.

        Returns:
            list: Tokens + tags.

        Raises:
            TypeError: If input is not string or a list of strings.

        """
        try:
            tokens = word_tokenize(corpus)
        except TypeError:
            raise TypeError(
                'Tagger input must be string or a list of strings.'
            )
        word_tags = list()
        for token in tokens:
            word_tags.append(
                (token, self._word_tag(token))
            )
        return word_tags
