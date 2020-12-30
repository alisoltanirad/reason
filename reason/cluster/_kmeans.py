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

    def cluster(self, data, k=1, distance='euclidean'):
        """Cluster method.

        Args:
            data (pandas.DataFrame or list of dict): Data to cluster.
            k (int, optional): Number of clusters.
            distance (optional): Function returning distance between 2 vectors.

        Raises:
            TypeError: If input data is not valid.

        """
        self._set_data(data)
        self._set_k(k)
        self._set_distance(distance)

    def elbow_method(self):
        return 1

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

    def _set_k(self, k):
        if isinstance(k, int) and k > 0:
            self._k = k
        else:
            raise TypeError('K must be positive integer.')

    def _set_distance(self, distance):
        if isinstance(distance, str) and distance in _distance_funcs.keys():
            self._distance = _distance_funcs[distance]
        elif callable(distance):
            self._distance = distance
        else:
            raise ValueError(
                'Distance must be a supported distance name string or a '
                'function returning the distance between two vectors.'
            )

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
