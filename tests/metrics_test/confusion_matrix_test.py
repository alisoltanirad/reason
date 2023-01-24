import pytest

from reason.metrics import BinaryConfusionMatrix, ConfusionMatrix


def test_bad_input():
    with pytest.raises(TypeError):
        ConfusionMatrix(True, [True])


def test_cm_getitem():
    y_true = ["red", "blue", "red", "red", "blue", "green", "red"]
    y_pred = ["blue", "blue", "red", "red", "green", "red", "red"]
    cm = ConfusionMatrix(y_true, y_pred)
    assert cm["red", "blue"] == 1


def test_cm_accuracy():
    y_true = ["red", "blue", "red", "red", "blue", "green", "red"]
    y_pred = ["blue", "blue", "red", "red", "green", "red", "red"]
    cm = ConfusionMatrix(y_true, y_pred)
    assert cm.accuracy() == 0.5714


def test_bcm_bad_input():
    with pytest.raises(ValueError):
        BinaryConfusionMatrix([0, 1, 2], [0, 0, 0])


def test_bcm_precision():
    y_true = ["True", "True", "False", "True", "True", "False"]
    y_pred = ["True", "True", "False", "False", "False", "True"]
    cm = BinaryConfusionMatrix(y_true, y_pred)
    assert cm.precision() == 0.6667


def test_bcm_recall():
    y_true = ["True", "True", "False", "True", "True", "False"]
    y_pred = ["True", "True", "False", "False", "False", "True"]
    cm = BinaryConfusionMatrix(y_true, y_pred)
    assert cm.recall() == 0.5


def test_bcm_f1_score():
    y_true = ["True", "True", "False", "True", "True", "False"]
    y_pred = ["True", "True", "False", "False", "False", "True"]
    cm = BinaryConfusionMatrix(y_true, y_pred)
    assert cm.f1_score() == 0.5714


def test_str():
    assert ConfusionMatrix([True], [False]).__str__() == "0 1\n0 0"
