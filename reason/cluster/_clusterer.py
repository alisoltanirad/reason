import pandas as pd

from reason._ml import MachineLearningModel


class BaseClusterer(MachineLearningModel):
    """Base Clusterer

    Base class for clusterers.

    """
    def __init__(self):
        self._dataset = None
        self._distance = None
        self._n = None
        self._clusters = None
        self._labels = None

    def fit(self, data, distance):
        self._set_data(data)
        self._set_distance(distance)

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
            raise AttributeError('Fit your data using fit method.')

    def get_features(self):
        """Get features method.

        Returns:
            List: Features

        """
        return list(self._data)

    def _set_data(self, data):
        if isinstance(data, pd.DataFrame):
            self._data = data
        elif self._is_featuresets_format(data):
            self._data = self._featuresets_to_dataframe(data)
        else:
            raise TypeError(
                'Data must be pandas DataFrame object '
                'or supported featuresets format.'
            )

    def _set_distance(self, distance):
        if callable(distance):
            self._distance = distance
        else:
            raise TypeError(
                'Distance must be a function.'
            )
