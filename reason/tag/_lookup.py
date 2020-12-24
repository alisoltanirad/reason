from ._tagger import BaseTagger


class LookupTagger(BaseTagger):
    """Lookup tagger

    """

    def __init__(self, data, backoff=None):
        """LookupTagger Constructor.

        Sets a lookup dictionary for tagging.

        Args:
            data (dict): Tokens + tags.
            backoff (tagger, optional): Backoff tagger object.

        Raises:
            ValueError: If lookup data is not a dictionary.

        """
        super().__init__(backoff)

        if isinstance(data, dict):
            self._lookup = data
        else:
            raise TypeError('Lookup data must be a dictionary.')

    def _token_tag(self, token):
        if token in self._lookup.keys():
            return self._lookup[token]

        return None