def accuracy(y_true, y_pred):
    """Accuracy score function.

    Easy-to-use word tokenize function.

    Example:
        >>> from reason.metrics import accuracy
        >>> accuracy(y_true, y_pred)
        0.9358

    Args:
        y_true (list): Real labels.
        y_pred (list): Predicted labels returned by classifier.

    Returns:
        float: Accuracy score.

    """
    length = len(y_true)
    correct = 0
    for i in range(length):
        if y_true[i] == y_pred[i]:
            correct += 1
    return float('{:.4f}'.format(correct / length))
