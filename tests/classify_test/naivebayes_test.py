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

def test_fit_featureset(x, y):
    classifier = NaiveBayesClassifier()
    classifier.fit(x, y)

def test_fit_dataframe():
    data = {
        'feature1': [True],
        'feature2': [False],
        'label': [True],
    }
    df = pd.DataFrame(data=data)
    classifier = NaiveBayesClassifier()
    classifier.fit(df.iloc[:, :-1], df['label'])

def test_fit_bad_x(y):
    x = 'True'
    with pytest.raises(TypeError):
        NaiveBayesClassifier().fit(x, y)

def test_fit_bad_y(x):
    y = pd.DataFrame(data={'col': [0, 0],})
    with pytest.raises(TypeError):
        NaiveBayesClassifier().fit(x, y)

def test_predict_dict(x, y):
    classifier = NaiveBayesClassifier()
    classifier.fit(x, y)
    new = {'feature': True, }
    assert classifier.predict(new) == True

def test_predict_featuresets(x, y):
    classifier = NaiveBayesClassifier()
    classifier.fit(x, y)
    new = [
        {'feature': True, }
    ]
    assert classifier.predict(new) == [True]

def test_predict_dataframe(x, y):
    classifier = NaiveBayesClassifier()
    classifier.fit(x, y)
    new = {'feature': [True], }
    dataframe = pd.DataFrame(data=new)
    assert classifier.predict(dataframe) == [True]

def test_predict_series(x, y):
    classifier = NaiveBayesClassifier()
    classifier.fit(x, y)
    new = {'feature': True, }
    series = pd.Series(data=new)
    assert classifier.predict(series) == True

def test_predict_bad_input_type(x, y):
    classifier = NaiveBayesClassifier()
    classifier.fit(x, y)
    with pytest.raises(TypeError):
        classifier.predict([0 ,1])

def test_predict_bad_input_value(x, y):
    classifier = NaiveBayesClassifier()
    classifier.fit(x, y)
    with pytest.raises(ValueError):
        classifier.predict(pd.Series([0, 1]))

def test_predict_bad_input_data(x, y):
    classifier = NaiveBayesClassifier()
    classifier.fit(x, y)
    with pytest.raises(TypeError):
        classifier.predict(pd.Series(pd.Series({'feature': pd.Series(0),})))

def test_get_labels():
    x = [
        {'feature': True, },
        {'feature': True, },
        {'feature': False, },
    ]
    y = [True, False, True]
    classifier = NaiveBayesClassifier()
    classifier.fit(x, y)
    assert classifier.get_labels() == [True, False]

def test_get_features():
    x = [
        {'feature1': True, 'feature2': 1,},
        {'feature1': True, 'feature2': 2,},
        {'feature1': False, 'feature2': 3,},
    ]
    y = [True, False, True]
    classifier = NaiveBayesClassifier()
    classifier.fit(x, y)
    assert classifier.get_features() == ['feature1', 'feature2']
