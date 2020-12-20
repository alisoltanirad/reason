import pandas as pd

from reason.classify import NaiveBayesClassifier


def test_object_creation():
    NaiveBayesClassifier()

def test_train_featureset():
    x = [{'feature': True, }]
    y = [True]
    classifier = NaiveBayesClassifier()
    classifier.train(x, y)

def test_train_dataframe():
    data = {
        'feature1': [True],
        'feature2'
        'label': [True],
    }
    df = pd.DataFrame(data=data)
    classifier = NaiveBayesClassifier()
    classifier.train(df[:, :-1], df['label'])

def test_classify_dict():
    x = [{'feature': True, }]
    y = [True]
    classifier = NaiveBayesClassifier()
    classifier.train(x, y)
    new = {'feature': True, }
    assert classifier.classify(new) == True

def test_classify_featuresets():
    x = [{'feature': True, }]
    y = [True]
    classifier = NaiveBayesClassifier()
    classifier.train(x, y)
    new = [
        {'feature': True, }
    ]
    assert classifier.classify(new) == [True]

def test_classify_seires():
    x = [{'feature': True, }]
    y = [True]
    classifier = NaiveBayesClassifier()
    classifier.train(x, y)
    new = {'feature': [True], }
    dataframe = pd.DataFrame(data=new)
    assert classifier.classify(dataframe) == [True]

def test_classify_dataframe():
    x = [{'feature': True, }]
    y = [True]
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
