import re

from ._tagger import BaseTagger


class RegexTagger(BaseTagger):
    """Regex tagger

    Attributes:
        pattern (str): Regex pattern for finding word stem.

    """

    def __init__(self, patterns=None, backoff=None):
        """RegexTagger Constructor.

        Sets regex patterns and their tags.

        Patterns must be a dictionary with regex pattern keys and tag values.
        Patterns example: patterns = {r'\d+': 'Digits', r'\w+': 'Word'}

        Args:
            patterns (list of tuple, optional): Regex patterns + pattern tags.
            backoff (tagger, optional): Backoff tagger object.

        Raises:
            ValueError: If some patterns are not valid regex patterns.

        """
        super().__init__(backoff)

        if patterns == None:
            self.patterns = {r'.*': 'token',}
        else:
            try:
                for pattern in patterns.keys():
                    re.compile(pattern)
                self.patterns = patterns
            except:
                raise ValueError('Patterns are not valid.')

    def _token_tag(self, token):
        for pattern, tag in self.patterns.items():
            if re.findall(pattern, token) != []:
                return tag

        return None