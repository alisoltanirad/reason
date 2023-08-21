import numpy as np
import pandas as pd

from ._classifier import BaseClassifier

# Supported feature types
_numeric = [int, float, bool, np.intc, np.single, np.bool_]
_categorical = [str]


class NaiveBayesClassifier(BaseClassifier):
    """Naive Bayes Classifier

    Uses gaussian distribution when dealing with continuous data.

    Example:
        >>> from reason.classify import NaiveBayesClassifier
        >>> classifier = NaiveBayesClassifier()
        >>> classifier.fit(x, y)
        >>> y_pred = classifier.predict(data)

    """

    def __init__(self):
        super().__init__()
        self._statistics = None
        self._prior = None

    def _train_classifier(self):
        self._n = min(len(self._x), len(self._y))

        self._features = list(self._x.columns)
        self._labels = list(self._y.unique())

        self._prior = dict()
        for label in self._labels:
            self._prior[str(label)] = self._y.value_counts()[label]

        self._statistics = dict()
        for label in self._labels:
            features = dict()
            for feature in self._features:
                if self._x[feature].dtype in _numeric:
                    features[feature] = {
                        "mean": np.mean(
                            self._dataset[self._dataset["label"] == label][feature]
                        ),
                        "var": np.var(
                            self._dataset[self._dataset["label"] == label][feature]
                        ),
                    }
            self._statistics[str(label)] = features

    def _predict_data(self, x):
        assert isinstance(x, pd.Series), "X data type must be pandas.Series"
        posterior = list()
        for label in self._labels:
            posterior.append(
                (self._prior[str(label)] * self._likelihood(x, label), label)
            )
        return max(posterior)[1]

    def _likelihood(self, x, label):
        p = list()
        for feature in self._features:
            try:
                value = x[feature]
            except KeyError:
                raise ValueError("Input data is not valid.")
            if type(value) in _numeric:
                mean = self._statistics[str(label)][feature]["mean"]
                var = self._statistics[str(label)][feature]["var"]
                if var == 0:
                    p.append(1)
                else:
                    p.append(
                        1
                        / np.sqrt(2 * np.pi * var)
                        * np.exp((-((value - mean) ** 2)) / (2 * var))
                    )

            elif type(value) in _categorical:
                p.append(
                    (
                        self._dataset[self._dataset.iloc[:, -1] == label][
                            feature
                        ].value_counts(value)
                        / self._n
                    )[0]
                )

            else:
                raise TypeError("Input data type is not supported.")

        return np.prod(p)
