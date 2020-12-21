# -*- coding: utf-8 -*-
"""Confusion matrix module.

API:
* *ConfusionMatrix* (class): Forms up confusion matrix.
* *BinaryConfusionMatrix* (class): Binary version of confusion matrix class.

Example:
    Binary Confusion matrix with [False, True] labels:
        >>> from reason.metrics import BinaryConfusionMatrix
        >>> cm = BinaryConfusionMatrix(y_true, y_pred)

        >>> cm
        68 21
        24 87

        >>> cm[True, False]
        24

        >>> cm.accuracy()
        0.775
        >>> cm.precision()
        0.7837
        >>> cm.recall()
        0.8055
        >>> cm.f1_score()
        0.7944

"""


class ConfusionMatrix:
    """Confusion Matrix

    Forms up an confusion matrix with given data. Has precision, recall and
    f1 score for binary cases.

    """

    def __init__(self, y_true, y_pred):
        """ConfusionMatrix constructor.

        Takes input data and makes a dict type matrix for storing and returning
        data and a list type matrix for presentation.

        Args:
            y_true (list): Real labels.
            y_pred (list): Predicted labels returned by classifier.

        Raises:
            Exception: If input data is not valid.

        """
        try:
            self._y_true = list(y_true)
            self._y_pred = list(y_pred)
        except TypeError:
            raise Exception('Inputs must be array-like objects.')

        self._labels = sorted(set(self._y_true))
        self._n_y = len(self._y_true)

        self._matrix = dict()
        for i in self._labels:
            self._matrix[i] = dict()
            for j in self._labels:
                self._matrix[i][j] = 0

        for i in range(self._n_y):
            self._matrix[self._y_pred[i]][self._y_true[i]] += 1

        self._array_matrix = [
            [str(n) for n in self._matrix[key].values()]
            for key in self._matrix.keys()
        ]

    def __str__(self):
        """String converter.

        Columns represent actual values, Rows represent predicted values.

        Returns:
            str: String presentation of the matrix.

        """
        return '\n'.join(
            ' '.join(
                self._array_matrix[i]
            ) for i in range(len(self._labels))
        )

    def __getitem__(self, keys):
        true, pred = keys
        return self._matrix[pred][true]

    def accuracy(self):
        """Accuracy method.

        Returns:
            float: Accuracy.

        """
        correct = 0.0
        for label in self._labels:
            correct += self._matrix[label][label]
        return float('{:.4f}'.format(correct / self._n_y))



class BinaryConfusionMatrix(ConfusionMatrix):
    """Binary Confusion Matrix

    Base class: ConfusionMatrix

    """

    def __init__(self, y_true, y_pred):
        """BinaryConfusionMatrix constructor.

        Calls base class constructor, then checks if matrix is binary (if labels
        set has two values.

        Args:
            y_true (list): Real labels.
            y_pred (list): Predicted labels returned by classifier.

        Raises:
            Exception: If labels set has less or more than two values.

        """
        super().__init__(y_true, y_pred)
        if len(self._labels) != 2:
            raise Exception('Binary matrix should have only two labels.')

    def precision(self):
        """Precision method.

        Returns:
            float: Precision.

        """
        false, true = self._labels[0], self._labels[1]
        return float('{:.4f}'.format(
            self._matrix[true][true] /
            (self._matrix[true][true] + self._matrix[true][false])
        ))

    def recall(self):
        """Recall method.

        Returns:
            float: Recall.

        """
        false, true = self._labels[0], self._labels[1]
        return float('{:.4f}'.format(
                self._matrix[true][true] /
                (self._matrix[true][true] + self._matrix[false][true])
        ))

    def f1_score(self):
        """F1 score method.

        Returns:
            float: F1 score.

        """
        precision, recall = self.precision(), self.recall()
        return float('{:.4f}'.format(
            2 * precision * recall / (precision + recall)
        ))
