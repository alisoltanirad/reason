import pandas as pd

from reason._mixins import is_featuresets_format, featuresets_to_dataframe


class BaseClassifier:
    """Base Classifier

    Base class for classifiers.

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
        elif is_featuresets_format(x):
            self._x = featuresets_to_dataframe(x)
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
        elif is_featuresets_format(data):
            x = featuresets_to_dataframe(data)
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
