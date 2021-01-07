import re


re_collection = {
    'etc': r"[\.]{3}",
    'ideogram': r"[:;][\)\(\*\|o0]+|[\)\(\*\|o0][:;]+|[-@$\^\*]_[-@$\^\*]",
    'abbr': r"(?:[A-Z]\.)+",
    'decimal': r"\$?\d+(?:,\d+)*(?:\.\d+)*%?",
    'word': r"\w+(?:['\.]\w+)*",
    'other': r"[^\w\s]",
}

re_micro_collection = {
    'alpha': r"[A-Za-z]+(?:'[A-Za-z]+)?",
    'numeric': r"\d+(?:,\d+)*(?:\.\d+)*",
}

re_pure_collection = {
    'alpha': r"[A-Za-z]+",
    'numeric': r"\d+",
}

regex_patterns = {
    'default': '|'.join([re for re in re_collection.values()]),
    'word': re_collection['word'],
    'ideogram': re_collection['ideogram'],
    'alphanumeric': re_collection['word'],
    'alpha': re_micro_collection['alpha'],
    'alpha-pure': re_pure_collection['alpha'],
    'numeric': re_micro_collection['numeric'],
    'numeric-pure': re_pure_collection['numeric'],
    'non-alphanumeric': '|'.join([
        re_collection['etc'], re_collection['ideogram'], re_collection['other']
    ]),
}


class WordTokenizer:
    """Regex Word Tokenizer

    Attributes:
        pattern (str): Regex pattern for tokenizing.

    Example:
        >>> from reason.tokenize import word_tokenize
        >>> sentence = "Testing reason0.1.0, (on: 127.0.0.1). Cool stuff..."
        >>> word_tokenize(sentence, 'alphanumeric')
        ['Testing', 'reason0.1.0', 'on', '127.0.0.1', 'Cool', 'stuff']

    """

    def __init__(self, pattern=None):
        """WordTokenizer Constructor.

        Sets a regex pattern for tokenizing.

        Ready-to-use choices for pattern are: 'default', 'word', 'ideogram',
        'alphanumeric', 'alpha', 'alpha-pure', 'numeric', 'numeric-pure',
        'non-alphanumeric'.

        You can also define your own regex pattern in the format of string.

        Args:
            pattern (str, optional): Regex pattern to use for tokenizing

        Raises:
            TypeError: If pattern is not a valid regex.

        """
        if pattern == None:
            self.pattern = regex_patterns['default']
        elif pattern in regex_patterns.keys():
            self.pattern = regex_patterns[pattern]
        else:
            try:
                re.compile(pattern)
                self.pattern = pattern
            except TypeError:
                raise TypeError(
                    'Pattern must be string or compiled regex pattern.'
                )

    def tokenize(self, input):
        """Tokenize text method.

        Tokenize input text

        Args:
            input (str or list of str): Text to tokenize.

        Returns:
            list: Tokens.

        Raises:
            TypeError: If input is not string or a list of strings.

        """
        if type(input) == str:
            text = input
        else:
            try:
                text = ' '.join(input)
            except TypeError:
                raise TypeError(
                    'Tokenize input must be string or a list of strings.'
                )

        return re.findall(self.pattern, text)


def word_tokenize(input, pattern='default'):
    """Tokenize text function.

    Easy-to-use word tokenize function.

    Args:
        input (str or list of str): Text to tokenize.
        pattern (str, optional): Regex pattern to use for tokenizing.

    Returns:
        list: Tokens.

    """
    return WordTokenizer(pattern).tokenize(input)
