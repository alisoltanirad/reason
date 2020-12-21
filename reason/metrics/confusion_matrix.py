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

        self._matrix = dict()
        for i in self._labels:
            self._matrix[i] = dict()
            for j in self._labels:
                self._matrix[i][j] = 0

        for i in range(len(self._y_true)):
            self._matrix[self._y_pred[i]][self._y_true[i]] += 1

        self._array_matrix = [
            [str(n) for n in self._matrix[key].values()]
            for key in self._matrix.keys()
        ]

    def __str__(self):
        return '\n'.join(' '.join(
            self._array_matrix[i]
        ) for i in range(len(self._labels)))
