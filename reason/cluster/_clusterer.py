import pandas as pd

from reason.ml.model import MachineLearningModel


class BaseClusterer(MachineLearningModel):
    """Base Clusterer

    Base class for clusterers.

    """

    def __init__(self):
        super().__init__()
        self._dataset = None
        self._distance = None
        self._n = None
        self._clusters = None

    def fit(self, data, distance):
        self._set_data(data)
        self._set_distance(distance)
        self._n = self._data.shape[0]
        self._clusters = dict()

    def get_clusters(self):
        """Get clusters method

        Returns:
            list: Clusters

        Raises:
            NameError: If data is not fitted yet.

        """
        try:
            return list(self._clusters.values())
        except AttributeError:
            raise AttributeError("Fit your data using fit method.")

    def get_features(self):
        """Get features method.

        Returns:
            List: Features

        """
        return list(self._data)

    def _predict_data(self, data):
        raise NotImplementedError

    def _set_data(self, data):
        if isinstance(data, pd.DataFrame):
            self._data = data
        elif self._is_featuresets_format(data):
            self._data = self._featuresets_to_dataframe(data)
        else:
            raise TypeError(
                "Data must be pandas DataFrame object "
                "or supported featuresets format."
            )

    def _set_distance(self, distance):
        if callable(distance):
            self._distance = distance
        else:
            raise TypeError("Distance must be a function.")
