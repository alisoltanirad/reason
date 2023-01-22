import pandas as pd
import pytest

from reason.cluster import DBSCAN


@pytest.fixture
def df():
    x = {'feature1': [2, 7], 'feature2': [3, 6]}
    df = pd.DataFrame(data=x)
    return df

def test_object_creation():
    DBSCAN()

def test_fit_featureset():
    data = [{'feature1': 2, 'feature2': 3}, {'feature1': 7, 'feature2': 6}]
    clusterer = DBSCAN()
    clusterer.fit(data, eps=10, min_pts=1)

def test_fit_dataframe(df):
    clusterer = DBSCAN()
    clusterer.fit(df, eps=10, min_pts=1)

def test_fit_bad_data():
    data = [1, 0]
    clusterer = DBSCAN()
    with pytest.raises(TypeError):
        clusterer.fit(data, eps=10, min_pts=1)

def test_fit_bad_eps(df):
    clusterer = DBSCAN()
    with pytest.raises(ValueError):
        clusterer.fit(df, eps=-1)

def test_fit_bad_min_pts(df):
    clusterer = DBSCAN()
    with pytest.raises(ValueError):
        clusterer.fit(df, eps=1, min_pts=0)

def test_fit_callable_distance(df):
    clusterer = DBSCAN()
    def dist(u, v):
        return 1
    clusterer.fit(df, eps=10, min_pts=1, distance=dist)

def test_fit_bad_distance(df):
    clusterer = DBSCAN()
    with pytest.raises(TypeError):
        clusterer.fit(df, eps=10, min_pts=1, distance=1)

def test_get_clusters_not_fitted():
    clusterer = DBSCAN()
    with pytest.raises(AttributeError):
        clusterer.get_clusters()

def test_get_features(df):
    clusterer = DBSCAN()
    clusterer.fit(df, eps=10, min_pts=1)
    assert clusterer.get_features() == ['feature1', 'feature2']

