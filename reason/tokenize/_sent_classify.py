
from nltk.corpus import treebank_raw


from reason.classify import NaiveBayesClassifier


def train_classifier():
    dataset = _get_dataset()
    classifier = NaiveBayesClassifier.train(dataset)
    #with open('sent_classifier.pickle', 'wb') as f:
    #    pickle.dump(classifier, f)


def _evaluate_classifier():
    dataset = _get_dataset()
    size = int(len(dataset) * 0.1)
    train_set, test_set = dataset[size:], dataset[:size]

    classifier = NaiveBayesClassifier()
    classifier.train(train_set)

    print(classifier.classify(test_set[0][0]))


def _get_dataset():
    sents = treebank_raw.sents()
    tokens = list()
    boundaries = set()
    offset = 0

    for sent in sents:
        tokens.extend(sent)
        offset += len(sent)
        boundaries.add(offset - 1)

    feature_sets = [
        (punc_features(tokens, i), (i in boundaries))
        for i in range(1, len(tokens) - 1)
        if tokens[i] in '.?!'
    ]

    return feature_sets


def punc_features(tokens, i):
    return {
        'next_word_capitalized': tokens[i+1][0].isupper(),
        'punctuation': tokens[i],
        'prev_word': tokens[i - 1].lower(),
        'prev_word_is_one_char': len(tokens[i-1]) == 1,
    }


if __name__ == '__main__':
    _evaluate_classifier()
