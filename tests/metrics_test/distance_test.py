import pytest

from reason.metrics import (euclidean_distance, hamming_distance,
                            manhattan_distance)


@pytest.fixture
def u():
    return [2, 2]

@pytest.fixture
def v():
    return [5, 6]


def test_euclidean(u, v):
    assert euclidean_distance(u, v) == 5

def test_manhattan(u, v):
    assert manhattan_distance(u, v) == 7

def test_hamming(u, v):
    assert hamming_distance(u, v) == 2
