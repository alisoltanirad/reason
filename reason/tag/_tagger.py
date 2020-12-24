from reason.tokenize import word_tokenize


class BaseTagger:
    """Base Tagger

    Base class for taggers.

    """
    def __init__(self, backoff=None):
        if backoff is None:
            self._taggers = [self]
        else:
            self._taggers = [self] + backoff._taggers

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
        token_tags = list()
        for token in tokens:
            tag = ''
            for tagger in self._taggers:
                token_tag = tagger._token_tag(token)
                if token_tag is not None:
                    tag = token_tag
                    break
            token_tags.append(
                (token, tag)
            )

        return token_tags
