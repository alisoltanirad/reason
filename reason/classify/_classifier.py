import pandas as pd

from reason._ml import MachineLearningModel


class BaseClassifier(MachineLearningModel):
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
