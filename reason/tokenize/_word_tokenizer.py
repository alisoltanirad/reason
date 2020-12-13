import re


regex_patterns = {
    'default': r"[\.]+|\w+(?:['.,]\w+)*|[^\w\s]",
    'alphanumeric': r"\w+(?:['.,]\w+)*",
    'alpha': r"[A-Za-z]+(?:'[A-Za-z]+)?",
    'alpha-pure': r"[A-Za-z]+",
    'numeric': r"[0-9]+(?:,[0-9]+)*(?:\.[0-9]+)*",
    'numeric-pure': r"[0-9]+",
}


class WordTokenizer:

    def __init__(self, pattern=None):
        if pattern == None:
            self.pattern = regex_patterns['default']
        elif pattern in regex_patterns.keys():
            self.pattern = regex_patterns[pattern]
        else:
            raise Exception('Pattern is not valid.')

    def tokenize(self, input):
        try:
            text = str(input)
        except:
            raise Exception('Input must be string.')

        return re.findall(self.pattern, text)


def word_tokenize(text, pattern='default'):
    return WordTokenizer(pattern).tokenize(text)