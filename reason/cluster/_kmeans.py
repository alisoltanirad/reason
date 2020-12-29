import pandas as pd

from ._distance import (
    euclidean_distance, manhattan_distance, hamming_distance
)

# Available distance types
_distance_funcs = {
    'euclidean': euclidean_distance,
    'manhattan': manhattan_distance,
    'hamming': hamming_distance,
}


class KMeansClusterer:
    """K-means clusterer

    Clustering using k-means algorithm.

    """

    def __init__(self, k='euclidean', distance=None):
        """KMeansClusterer constructor.

        Args:
            data (pandas.DataFrame or list of dict): Data to cluster.
            k (int, optional): Number of clusters.

        Raises:
            TypeError: If input data is not valid.

        """
        if k is None:
            self._k = self.elbow_method()
        elif isinstance(k, int) and k > 0:
            self._k = k
        else:
            raise TypeError('K must be positive integer.')

        if isinstance(distance, str) and distance in _distance_funcs.keys():
                self._distance = _distance_funcs[distance]
        elif callable(distance):
            self._distance = distance
        else:
            raise ValueError(
                'Distance must be a supported distance name string or a '
                'function returning the distance between two vectors.'
            )

    def cluster(self, data):
        if isinstance(data, pd.DataFrame):
            self._data = data
        elif self._is_featuresets_format(data):
            self._data = self._featuresets_to_dataframe(data)
        else:
            raise TypeError(
                'Data must be pandas DataFrame object '
                'or supported featuresets format.'
            )
        pass

    def elbow_method(self):
        return 1

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
