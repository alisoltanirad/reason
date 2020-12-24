from ._tagger import BaseTagger


class DefaultTagger(BaseTagger):
    """Default Tagger

    Tags all entries with a default value

    Attributes:
        default_tag (str): Default value of tagger.

    Example:
        >>> from reason.tag import DefaultTagger
        >>> tagger = DefaultTagger('word')
        >>> tagger.tag('reason')
        [('reason', 'word')]

    """

    def __init__(self, tag='token', backoff=None):
        """DefaultTagger constructor.

        Sets default tag value.

        Args:
            tag (str, optional): Default tag.
            backoff (tagger, optional): Backoff tagger object.

        Raises:
            TypeError: If tag is not string.

        """
        super().__init__(backoff)
        if isinstance(tag, str):
            self.default_tag = tag
        else:
            raise TypeError('Default tag must be an string.')

    def _token_tag(self, token):
        return self.default_tag
