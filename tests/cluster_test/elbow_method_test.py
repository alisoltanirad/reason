import pandas as pd
import pytest
from sklearn.datasets import make_blobs

from reason.cluster import KMeansClusterer, elbow_method


@pytest.fixture
def df():
    x, y = make_blobs(n_samples=100, centers=5, random_state=101)
    return pd.DataFrame(x)


def test_elbow_method(df):
    assert elbow_method(df, KMeansClusterer, 10) == 5

def test_k_1(df):
    assert elbow_method(df, KMeansClusterer, 1) == 1

def test_k_max(df):
    assert elbow_method(df, KMeansClusterer, 2) == 2
