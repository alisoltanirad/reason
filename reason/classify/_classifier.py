import pandas as pd

from reason.ml.model import MachineLearningModel


class BaseClassifier(MachineLearningModel):
    """Base Classifier

    Base class for classifiers.

    """

    def __init__(self):
        super().__init__()
        self._x = None
        self._y = None
        self._features = None
        self._n = None

    def fit(self, x, y):
        """Fit method.

        Trains classifier with dataset.

        Args:
            x (pandas.DataFrame or list of dict): Feature sets
            y (pandas.Series or list): Labels

        Raises:
            TypeError: If input data is not valid.

        """
        self._set_parameters(x, y)

        self._train_classifier()

    def _train_classifier(self):
        raise NotImplementedError

    def _predict_data(self, data):
        raise NotImplementedError

    def _set_parameters(self, x, y):
        self._set_x(x)
        self._set_y(y)
        self._set_data()

    def _set_x(self, x):
        if type(x) == pd.DataFrame:
            self._x = x
        elif self._is_featuresets_format(x):
            self._x = self._featuresets_to_dataframe(x)
        else:
            raise TypeError(
                "X must be pandas.DataFrame object " "or supported featuresets format."
            )

    def _set_y(self, y):
        try:
            self._y = pd.Series(y)
        except (TypeError, ValueError):
            raise TypeError("Y must be array-like object.")

    def _set_data(self):
        self._dataset = self._x.copy()
        self._dataset["label"] = self._y
