# -*- coding: utf-8 -*-
"""Word tokenize module.

API:
* *accuracy* (function): Calculates accuracy score.

Example:
    Tokenize an string:

        >>> from reason.metrics import accuracy

        >>> accuracy(y_true, y_pred)
        0.9358

"""


def accuracy(y_true, y_pred):
    """Accuracy score function.

    Easy-to-use word tokenize function.

    Args:
        y_true (list): Real labels.
        y_pred (list): Predicted labels returned by classifier.

    Returns:
        float: Accuracy score.

    """
    all = len(y_true)
    correct = 0
    for i in range(all):
        if y_true[i] == y_pred[i]:
            correct += 1
    return float('{:.4f}'.format(correct / all))
