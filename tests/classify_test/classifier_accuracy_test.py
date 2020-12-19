from nltk.corpus import treebank_raw

from reason.classify import NaiveBayesClassifier
from reason.metrics import accuracy


def classifier_accuracy_test():
    return {
        'Naive-Bayes': _evaluate_classifier(NaiveBayesClassifier),
    }


def _evaluate_classifier(name):
    train_set, test_x, test_y = _get_data()
    classifier = name(train_set)
    y_pred = classifier.classify(test_x)
    return accuracy(test_y, y_pred)


def _get_data():
    dataset = _get_dataset()
    size = int(len(dataset) * 0.1)
    train_set, test_set = dataset[size:], dataset[:size]
    test_x, test_y = [], []
    for t in test_set:
        test_x.append(t[0])
        test_y.append(t[1])

    return train_set, test_x, test_y


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
    data = classifier_accuracy_test()
    for key, value in data.items():
        print('{name}: {accuracy}%'.format(name=key, accuracy=value*100))
