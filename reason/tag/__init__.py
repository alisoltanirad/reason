# -*- coding: utf-8 -*-
"""tag package.

Word tagging with part-of-speech tagging support.

API:

* POSTagger (class): Part-of-speech tagger.
* DefaultTagger (class): Tags each token to the given default value.
* LookupTagger (class): Tags using lookup data.
* RegexTagger (class): Tags using regex patterns.

"""

from ._pos import POSTagger
from ._default import DefaultTagger
from ._lookup import LookupTagger
from ._regex import RegexTagger
