from nltk.corpus import treebank

from reason.metrics import accuracy
from reason.tag import POSTagger


def _evaluate_pos_tagger():
    words, real_tags = _get_data()
    tagger = POSTagger()
    _w, pred_tags = _split_tagged_words(tagger.tag(words))
    for i in range(100):
        print(words[i], real_tags[i], pred_tags[i])
    return accuracy(real_tags, pred_tags)


def _get_data():
    return _split_tagged_words(treebank.tagged_words())


def _split_tagged_words(tagged_words):
    words, tags = list(), list()
    for (word, tag) in tagged_words:
        words.append(word)
        tags.append(tag)
    return words, tags


if __name__ == '__main__':
    accuracy = _evaluate_pos_tagger()
    print('Accuracy: {}%'.format(accuracy * 100))
