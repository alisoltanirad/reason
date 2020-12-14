import re


re_collection = {
    'etc': r"[\.]{3}",
    'ideogram': r"[:;][\)\(\*\|o0]+|[\)\(\*\|o0][:;]+|[-@$\^\*]_[-@$\^\*]",
    'word': r"\w+(?:['\.]\w+)*",
    'non-alphanumeric': r"[^\w\s]",
 }

re_micro_collection = {
    'alpha': r"[A-Za-z]+(?:'[A-Za-z]+)?",
    'numeric': r"[0-9]+(?:,[0-9]+)*(?:\.[0-9]+)*",
}

re_pure_collection = {
    'alpha': r"[A-Za-z]+",
    'numeric': r"[0-9]+",
}

regex_patterns = {
    'default': '|'.join([re for re in re_collection.values()]),
    'word': re_collection['word'],
    'alphanumeric': re_collection['word'],
    'alpha': re_micro_collection['alpha'],
    'alpha-pure': re_pure_collection['alpha'],
    'numeric': re_micro_collection['numeric'],
    'numeric-pure': re_pure_collection['numeric'],
    'non-alphanumeric': re_collection['non-alphanumeric'],
    'ideogram': re_collection['ideogram'],
}


class WordTokenizer:

    def __init__(self, pattern=None):
        if pattern == None:
            self.pattern = regex_patterns['default']
        elif pattern in regex_patterns.keys():
            self.pattern = regex_patterns[pattern]
        else:
            try:
                re.compile(pattern)
                self.pattern = pattern
            except:
                raise Exception('Pattern is not valid.')

    def tokenize(self, input):
        if type(input) == str:
            text = input
        else:
            try:
                text = ' '.join(input)
            except TypeError:
                raise Exception(
                    'Tokenize input must be string or a list of strings.'
                )

        return re.findall(self.pattern, text)


def word_tokenize(corpus, pattern='default'):
    return WordTokenizer(pattern).tokenize(corpus)
