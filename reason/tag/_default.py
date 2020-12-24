from ._tagger import BaseTagger


class DefaultTagger(BaseTagger):
    """Default Tagger

    Tags all entries with a default value

    """

    def __init__(self, tag='token'):
        """DefaultTagger constructor.

        Sets default tag value.

        Args:
            tag (str, optional): Default tag.

        Raises:
            TypeError: If tag is not string.

        """
        if isinstance(tag, str):
            self.default_tag = tag
        else:
            raise TypeError('Default tag must be an string.')

    def _word_tag(self, token):
        return self.default_tag
