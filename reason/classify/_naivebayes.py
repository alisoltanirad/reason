import numpy as np
import pandas as pd

# Supported feature types
_numeric = [int, float, bool, np.intc , np.single, np.bool_]
_categorical = [str]


class NaiveBayesClassifier:
    """Naive Bayes Classifier

    Uses gaussian distribution when dealing with continuous data.

    Example:
        >>> from reason.classify import NaiveBayesClassifier
        >>> classifier = NaiveBayesClassifier()
        >>> classifier.fit(x, y)
        >>> y_pred = classifier.predict(data)

    """

    def fit(self, x, y):
        """Fit method.

        Trains classifier with dataset.

        Args:
            x (pandas.DataFrame or list of dict): Feature sets
            y (pandas.Series or list): Labels

        Raises:
            TypeError: If input data is not valid.

        """
        try:
            self._y = pd.Series(y)
        except (TypeError, ValueError):
            raise TypeError('Y must be array-like object.')
        if type(x) == pd.DataFrame:
            self._x = x
        elif self._is_featuresets_format(x):
            self._x = self._featuresets_to_dataframe(x)
        else:
            raise TypeError(
                'X must be pandas.DataFrame object '
                'or supported featuresets format.'
            )
        self._dataset = self._x.copy()
        self._dataset['label'] = self._y

        self._train_classifier()

    def predict(self, data):
        """Predict method.

        Classifies new entries (feature sets).

        Args:
            data (pandas.DataFrame or list of dict): Features set(s).

        Returns:
            Label or list of labels.

        Raises:
            TypeError: If input data type is not supported.
            ValueError: If input data is not valid.

        """
        if type(data) == pd.Series:
            return self._predict_data(data)
        elif type(data) == dict:
            return self._predict_data(pd.Series(data))
        elif type(data) == pd.DataFrame:
            x = data
        elif self._is_featuresets_format(data):
            x = self._featuresets_to_dataframe(data)
        else:
            raise TypeError('Input data type is not supported.')

        labels = list()
        for i in range(len(x)):
            labels.append(self._predict_data(x.iloc[i]))
        return labels

    def get_labels(self):
        """Get labels method.

        Returns:
            List: Labels

        """
        return list(self._labels)

    def get_features(self):
        """Get features method.

        Returns:
            List: Features

        """
        return self._features

    def _train_classifier(self):

        self._n = min(len(self._x), len(self._y))

        self._features = list(self._x.columns)
        self._labels = list(self._y.unique())

        self._prior = dict()
        for label in self._labels:
            self._prior[str(label)] = \
                self._y.value_counts()[label]

        self._statistics = dict()
        for label in self._labels:
            features = dict()
            for feature in self._features:
                if self._x[feature].dtype in _numeric:
                    features[feature] = {
                        'mean': np.mean(
                            self._dataset[
                                self._dataset['label'] == label
                            ][feature]
                        ),
                        'var': np.var(
                            self._dataset[
                                self._dataset['label'] == label
                            ][feature]
                        ),
                    }
            self._statistics[str(label)] = features

    def _predict_data(self, x):
        assert isinstance(x, pd.Series), 'X data type must be pandas.Series'
        posterior = list()
        for label in self._labels:
            posterior.append((
                self._prior[str(label)] * self._likelihood(x, label), label
            ))
        return max(posterior)[1]

    def _likelihood(self, x, label):
        p = list()
        for feature in self._features:
            try:
                value = x[feature]
            except KeyError:
                raise ValueError('Input data is not valid.')
            if type(value) in _numeric:
                mean = self._statistics[str(label)][feature]['mean']
                var = self._statistics[str(label)][feature]['var']
                if var == 0:
                    p.append(1)
                else:
                    p.append(
                        1 / np.sqrt(2 * np.pi * var)
                        * np.exp((-(value - mean) ** 2) / (2 * var))
                    )

            elif type(value) in _categorical:
                p.append((
                    self._dataset[
                        self._dataset.iloc[:, -1] == label
                    ][feature].value_counts(value) / self._n
                )[0])

            else:
                raise TypeError('Input data type is not supported.')

        return np.prod(p)

    def _is_featuresets_format(self, input_data):

        if (
            not isinstance(input_data, list) or
            not all(isinstance(item, dict) for item in input_data)
        ):
            return False

        return True

    def _featuresets_to_dataframe(self, featuresets):
        data = dict()
        features = featuresets[0].keys()

        for feature in features:
            data[feature] = pd.Series(set[feature] for set in featuresets)

        df = pd.DataFrame(data=data)

        return df
