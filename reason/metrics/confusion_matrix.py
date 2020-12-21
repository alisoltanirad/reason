# -*- coding: utf-8 -*-
"""Confusion matrix module.

API:
* *ConfusionMatrix* (class): Forms up confusion matrix.

Example:


"""


class ConfusionMatrix:

    def __init__(self, y_true, y_pred):

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
        return '\n'.join(
            ' '.join(
                self._array_matrix[i]
            ) for i in range(len(self._labels))
        )

    def __getitem__(self, keys):
        true, pred = keys
        return self._matrix[pred][true]

    def accuracy(self):
        correct = 0.0
        for label in self._labels:
            correct += self._matrix[label][label]
        return float('{:.4f}'.format(correct / self._n_y))

    def precision(self):
        if len(self._labels) != 2:
            raise Exception(
                'Precision can only be calculated for binary matrix.'
            )
        false, true = self._labels[0], self._labels[1]
        return (
            self._matrix[true][true] /
            (self._matrix[true][true] + self._matrix[true][false])
        )

    def recall(self):
        if len(self._labels) != 2:
            raise Exception(
                'Recall can only be calculated for binary matrix.'
            )
        false, true = self._labels[0], self._labels[1]
        return (
                self._matrix[true][true] /
                (self._matrix[true][true] + self._matrix[false][true])
        )

    def f1_score(self):
        if len(self._labels) != 2:
            raise Exception(
                'F1 score can only be calculated for binary matrix.'
            )
        precision, recall = self.precision(), self.recall()
        return (
            2 * precision * recall / (precision + recall)
        )
