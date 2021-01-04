import pytest
import pandas as pd

from reason.cluster import KMeansClusterer


@pytest.fixture
def df():
    x = {'feature1': [2, 7], 'feature2': [3, 6]}
    df = pd.DataFrame(data=x)
    return df

def test_object_creation():
    KMeansClusterer()

def test_fit_featureset():
    data = [{'feature1': 2, 'feature2': 3}, {'feature1': 7, 'feature2': 6}]
    clusterer = KMeansClusterer()
    clusterer.fit(data)

def test_fit_dataframe(df):
    clusterer = KMeansClusterer()
    clusterer.fit(df)

def test_fit_tolerance():
    data = pd.DataFrame(data={'feature': [1]})
    clusterer = KMeansClusterer()
    clusterer.fit(data)

def test_fit_bad_data():
    data = [1, 0]
    clusterer = KMeansClusterer()
    with pytest.raises(TypeError):
        clusterer.fit(data)

def test_fit_bad_k(df):
    clusterer = KMeansClusterer()
    with pytest.raises(ValueError):
        clusterer.fit(df, k=0)

def test_fit_callable_distance(df):
    clusterer = KMeansClusterer()
    def dist(u, v):
        return 1
    clusterer.fit(df, distance=dist)

def test_fit_bad_distance(df):
    clusterer = KMeansClusterer()
    with pytest.raises(TypeError):
        clusterer.fit(df, distance=1)

def test_predict_dict(df):
    clusterer = KMeansClusterer()
    clusterer.fit(df)
    new = {'feature1': 2, 'feature2': 2}
    clusterer.predict(new)

def test_predict_featuresets(df):
    clusterer = KMeansClusterer()
    clusterer.fit(df)
    new = [
        {'feature1': 2, 'feature2': 2}
    ]
    clusterer.predict(new)

def test_predict_dataframe(df):
    clusterer = KMeansClusterer()
    clusterer.fit(df)
    new = {'feature1': [2],'feature2': [2]}
    dataframe = pd.DataFrame(data=new)
    clusterer.predict(dataframe)

def test_predict_series(df):
    clusterer = KMeansClusterer()
    clusterer.fit(df)
    new = {'feature1': 2, 'feature2': 2}
    series = pd.Series(data=new)
    clusterer.predict(series)

def test_predict_not_fitted():
    clusterer = KMeansClusterer()
    new = {'feature1': 2, 'feature2': 2}
    series = pd.Series(data=new)
    with pytest.raises(AttributeError):
        clusterer.predict(series)

def test_predict_bad_input_type(df):
    clusterer = KMeansClusterer()
    clusterer.fit(df)
    with pytest.raises(TypeError):
        clusterer.predict([0 ,1])

def test_predict_bad_input_value(df):
    clusterer = KMeansClusterer()
    clusterer.fit(df)
    with pytest.raises(ValueError):
        clusterer.predict(pd.Series([0, 1, 2]))

def test_get_clusters_not_fitted():
    clusterer = KMeansClusterer()
    with pytest.raises(AttributeError):
        clusterer.get_clusters()

def test_get_features(df):
    clusterer = KMeansClusterer()
    clusterer.fit(df)
    assert clusterer.get_features() == ['feature1', 'feature2']

def test_inertia(df):
    clusterer = KMeansClusterer()
    clusterer.fit(df)
    assert isinstance(clusterer.inertia(), float)
