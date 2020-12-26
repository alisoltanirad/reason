from ._tagger import BaseTagger


class LookupTagger(BaseTagger):
    """Lookup tagger

    Example:
        >>> from reason.tag import LookupTagger
        >>> lookup_data = {'cat': 'animal', 'black': 'color'}
        >>> tagger = LookupTagger(lookup_data)
        >>> tagger.tag('a black cat')
        [('a', ''), ('black', 'color'), ('cat', 'animal')]

    """

    def __init__(self, data, backoff=None):
        """LookupTagger Constructor.

        Sets a lookup dictionary for tagging.

        Args:
            data (dict): Tokens + tags.
            backoff (tagger, optional): Backoff tagger object.

        Raises:
            TypeError: If lookup data is not a dictionary.

        """
        super().__init__(backoff)

        if isinstance(data, dict):
            self._lookup = data
        else:
            raise TypeError('Lookup data must be python dictionary.')

    def _token_tag(self, token):
        if token in self._lookup.keys():
            return self._lookup[token]

        return None
