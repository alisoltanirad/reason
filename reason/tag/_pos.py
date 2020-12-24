import re

from reason.tokenize import word_tokenize
from ._tagger import BaseTagger
from ._default import DefaultTagger
from ._regex import RegexTagger
from ._lookup import LookupTagger
from ._pos_tagger_data import get_re_collection, get_freq_100


class POSTagger(BaseTagger):
    """POS tagger

    Part of speech tagger. Uses lookup, regex and default taggers for tagging.

    """

    def __init__(self, backoff=None):
        """RegexTagger Constructor.

        Sets tagger.

        Args:
            backoff (tagger, optional): Backoff tagger object.

        """
        super().__init__(backoff)

        default_tagger = DefaultTagger('NN')
        re_collection = get_re_collection()
        regex_tagger = RegexTagger(re_collection, backoff=default_tagger)
        lookup_data = get_freq_100()
        lookup_tagger = LookupTagger(lookup_data, backoff=regex_tagger)
        self._tagger = lookup_tagger


    def _token_tag(self, token):
        if word_tokenize(token, 'alphanumeric') != []:
            return self._tagger.tag(token)[0][1]

        return token
