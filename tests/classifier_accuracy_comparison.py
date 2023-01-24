from nltk.corpus import treebank_raw

from reason.classify import NaiveBayesClassifier
from reason.metrics import accuracy


def classifier_accuracy_test():
    return {
        "Naive-Bayes": _evaluate_classifier(NaiveBayesClassifier),
    }


def _evaluate_classifier(name):
    x_train, y_train, x_test, y_test = _get_data()
    classifier = name()
    classifier.train(x_train, y_train)
    y_pred = classifier.classify(x_test)
    return accuracy(y_test, y_pred)


def _get_data():
    sents = treebank_raw.sents()
    tokens = list()
    boundaries = set()
    offset = 0

    for sent in sents:
        tokens.extend(sent)
        offset += len(sent)
        boundaries.add(offset - 1)

    featuresets, labels = list(), list()

    for i in range(1, len(tokens) - 1):
        if tokens[i] in ".?!":
            featuresets.append(_punc_features(tokens, i))
            labels.append((i in boundaries))

    test_size = int(len(labels) * 0.1)
    x_train, x_test = featuresets[test_size:], featuresets[:test_size]
    y_train, y_test = labels[test_size:], labels[:test_size]

    return x_train, y_train, x_test, y_test


def _punc_features(tokens, i):
    return {
        "next_word_capitalized": tokens[i + 1][0].isupper(),
        "punctuation": tokens[i],
        "prev_word": tokens[i - 1].lower(),
        "prev_word_is_one_char": len(tokens[i - 1]) == 1,
    }


if __name__ == "__main__":
    data = classifier_accuracy_test()
    for key, value in data.items():
        print("{name}: {accuracy}%".format(name=key, accuracy=value * 100))
