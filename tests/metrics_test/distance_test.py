import pytest

from reason.metrics import (
    euclidean_distance, manhattan_distance, hamming_distance
)


@pytest.fixture
def u():
    return [2, 2]

@pytest.fixture
def v():
    return [5, 6]


def euclidean_test(u, v):
    assert euclidean_distance(u, v) == 5

def manhattan_test(u, v):
    assert manhattan_distance(u, v) == 7

def hamming_test(u, v):
    assert hamming_distance(u, v) == 2
