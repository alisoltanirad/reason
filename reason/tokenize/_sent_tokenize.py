from reason.classify import NaiveBayesClassifier
from ._treebank import get_sents
from ._word_tokenize import WordTokenizer


class SentTokenizer:
    """Sentence Tokenizer

    Example:
        >>> from reason.tokenize import sent_tokenize
        >>> text = "Hey, what's up? I love using Reason library!"
        >>> sents = sent_tokenize(text)
        >>> for sent in sents:
        ...     print(sent)
        Hey, what's up?
        I love using Reason library!

    """

    def __init__(self):
        """SentTokenizer Constructor.

        Creates and utilises a naive bayes classifier. SentTokenizer class
        recognizes sentences using this classifier.

        """
        self._classifier = NaiveBayesClassifier()
        x, y = self._get_dataset()
        self._classifier.fit(x, y)

    def tokenize(self, corpus):
        """Tokenize text method.

        Tokenize input text

        Args:
            corpus (str or list of str): Text to tokenize.

        Returns:
            list: Tokens.

        Raises:
            TypeError: If input is not string or a list of strings.

        """
        words, sents, input_type = self._preprocess_tokenize_input(corpus)
        position, start = 0, 0

        for i, token in enumerate(words):
            try:
                if token in '.?!' and self._classifier.predict(
                    self._punc_features(words, i)
                ) == True:
                    if input_type == 'str':
                        text = sents.pop(-1)
                        sent, rest = text[: position + 1], text[position + 1 :]
                        sents.append(sent.strip())
                        sents.append(rest.strip())
                        position = 0
                    else:
                        sents.append(words[start : i + 1])
                        start = i + 1

                if input_type == 'str':
                    position += len(token)
                    if sents[-1][position] == ' ':
                        position += 1

            except IndexError:
                break

        if input_type == 'list' and start < len(words):
            sents.append(words[start:])

        return sents

    def _preprocess_tokenize_input(self, corpus):
        wt = WordTokenizer()
        if type(corpus) == str:
            words = wt.tokenize(corpus)
            sents = [corpus]
            input_type = 'str'
        else:
            try:
                words = wt.tokenize(' '.join(corpus))
                sents = list()
                input_type = 'list'
            except TypeError:
                raise TypeError(
                    'Tokenize input must be string or a list of strings.'
                )

        return words, sents, input_type

    def _punc_features(self, tokens, i):
        return {
            'next_word_capitalized': tokens[i + 1][0].isupper(),
            'punctuation': tokens[i],
            'prev_word': tokens[i - 1].lower(),
            'prev_word_is_one_char': len(tokens[i - 1]) == 1,
        }

    def _get_dataset(self):
        sents = get_sents()
        tokens = list()
        boundaries = set()
        offset = 0

        for sent in sents:
            tokens.extend(sent)
            offset += len(sent)
            boundaries.add(offset - 1)

        featuresets, labels = list(), list()

        for i in range(1, len(tokens) - 1):
            if tokens[i] in '.?!':
                featuresets.append(
                    self._punc_features(tokens, i)
                )
                labels.append(
                    (i in boundaries)
                )


        return featuresets, labels


def sent_tokenize(input):
    """Tokenize text function.

        Easy-to-use sentence tokenize function.

        Args:
            input (str or list of str): Text to tokenize.

        Returns:
            list: Tokens.

        """
    return SentTokenizer().tokenize(input)
