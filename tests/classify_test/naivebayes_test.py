import pytest
import pandas as pd

from reason.classify import NaiveBayesClassifier


@pytest.fixture
def x():
    x = [{'feature': True,}]
    return x

@pytest.fixture
def y():
    y = [True]
    return y


def test_object_creation():
    NaiveBayesClassifier()

def test_train_featureset(x, y):
    classifier = NaiveBayesClassifier()
    classifier.train(x, y)

def test_train_dataframe():
    data = {
        'feature1': [True],
        'feature2': [False],
        'label': [True],
    }
    df = pd.DataFrame(data=data)
    classifier = NaiveBayesClassifier()
    classifier.train(df.iloc[:, :-1], df['label'])

def test_classify_dict(x, y):
    classifier = NaiveBayesClassifier()
    classifier.train(x, y)
    new = {'feature': True, }
    assert classifier.classify(new) == True

def test_classify_featuresets(x, y):
    classifier = NaiveBayesClassifier()
    classifier.train(x, y)
    new = [
        {'feature': True, }
    ]
    assert classifier.classify(new) == [True]

def test_classify_seires(x, y):
    classifier = NaiveBayesClassifier()
    classifier.train(x, y)
    new = {'feature': [True], }
    dataframe = pd.DataFrame(data=new)
    assert classifier.classify(dataframe) == [True]

def test_classify_dataframe(x, y):
    classifier = NaiveBayesClassifier()
    classifier.train(x, y)
    new = {'feature': True, }
    series = pd.Series(data=new)
    assert classifier.classify(series) == True

def test_get_labels():
    x = [
        {'feature': True, },
        {'feature': True, },
        {'feature': False, },
    ]
    y = [True, False, True]
    classifier = NaiveBayesClassifier()
    classifier.train(x, y)
    assert classifier.get_labels() == [True, False]

def test_get_features():
    x = [
        {'feature1': True, 'feature2': 1,},
        {'feature1': True, 'feature2': 2,},
        {'feature1': False, 'feature2': 3,},
    ]
    y = [True, False, True]
    classifier = NaiveBayesClassifier()
    classifier.train(x, y)
    assert classifier.get_features() == ['feature1', 'feature2']
