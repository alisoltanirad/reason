from ._tagger import BaseTagger


class DefaultTagger(BaseTagger):
    """Default Tagger

    Tags all entries with a default value

    """

    def __init__(self, tag='token', backoff=None):
        """DefaultTagger constructor.

        Sets default tag value.

        Args:
            tag (str, optional): Default tag.
            backoff (class, optional): Default tagger won't set backoffs.

        Raises:
            TypeError: If tag is not string.

        """
        if isinstance(tag, str):
            self._taggers = [self]
            self.default_tag = tag
        else:
            raise TypeError('Default tag must be an string.')

    def _token_tag(self, token):
        return self.default_tag
