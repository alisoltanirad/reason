import pandas as pd

from reason.classify import NaiveBayesClassifier


def test_object_creation():
    NaiveBayesClassifier()

def test_train_init():
    data = [({'feature': True,}, True)]
    NaiveBayesClassifier(data)

def test_train_pair():
    data = [
        ({'feature': True,}, True)
    ]
    classifier = NaiveBayesClassifier()
    classifier.train(data)

def test_train_dataframe():
    data = [
        ({'feature': True,}, True)
    ]
    df = pd.DataFrame(data=data)
    classifier = NaiveBayesClassifier()
    classifier.train(df)

def test_get_labels():
    data = [
        ({'feature': True, }, True),
        ({'feature': True, }, False),
        ({'feature': False, }, True),
    ]
    df = pd.DataFrame(data=data)
    classifier = NaiveBayesClassifier()
    classifier.train(df)
    assert classifier.get_labels() == [True, False]

def test_get_features():
    data = [
        ({'feature1': True, 'feature2': 1,}, True),
        ({'feature1': True, 'feature2': 2,}, False),
        ({'feature1': False, 'feature2': 3,}, True),
    ]
    df = pd.DataFrame(data=data)
    classifier = NaiveBayesClassifier()
    classifier.train(df)
    assert classifier.get_features() == ['feature1', 'feature2']
