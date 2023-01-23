from reason.metrics import accuracy


def test_bool_100():
    y_true = [True, False, True]
    y_pred = [True, False, True]
    assert accuracy(y_true, y_pred) == 1.0


def test_bool_66():
    y_true = [True, False, True]
    y_pred = [True, False, False]
    assert accuracy(y_true, y_pred) == 0.6667


def test_bool_0():
    y_true = [True, False, True]
    y_pred = [False, True, False]
    assert accuracy(y_true, y_pred) == 0.0


def test_int():
    y_true = [10, 4, 3, 5]
    y_pred = [3, 4, 7, 5]
    assert accuracy(y_true, y_pred) == 0.5


def test_float():
    y_true = [10.4, 4.7, 3.0, 5.02]
    y_pred = [10.40, 4.74, 3, 5.02]
    assert accuracy(y_true, y_pred) == 0.75


def test_str():
    y_true = ["a", "b", "c"]
    y_pred = ["d", "b", "a"]
    assert accuracy(y_true, y_pred) == 0.3333


def test_list():
    y_true = [["a", "b"], ["c"]]
    y_pred = [["a", "b"], ["d"]]
    assert accuracy(y_true, y_pred) == 0.5
