from random import randint

import numpy as np
import pandas as pd

from ._distance import (
    euclidean_distance, manhattan_distance, hamming_distance
)
from ._clusterer import BaseClusterer

# Available distance types
_distance_funcs = {
    'euclidean': euclidean_distance,
    'manhattan': manhattan_distance,
    'hamming': hamming_distance,
}


class KMeansClusterer(BaseClusterer):
    """K-means clusterer

    Clustering using k-means algorithm.

    """
    def cluster(self, data, distance='euclidean', k=None):
        """Cluster method.

        Clusters data to k groups. If k is not given, finds the optimal number
        using the elbow method.

        Args:
            data (pandas.DataFrame or list of dict): Data to cluster.
            k (int, optional): Number of clusters.
            distance (optional): Function returning distance between 2 vectors.

        Raises:
            TypeError: If input data is not valid.

        """
        self._set_data(data)
        self._set_distance(distance)
        self._set_k(k)

        if self._k == 1:
            return self._data

        self._n_samples = self._data.shape[0]
        centroids = self._init_centroids(self._k)
        tolerance = (np.max(abs(self._data)) - np.min(abs(self._data))) / 1000
        iter = 100

        while iter > 0:

            clusters = dict()
            for i in range(self._k):
                clusters[i] = pd.DataFrame()

            for i in range(self._n_samples):
                distances = [
                    self._distance(self._data.loc[i], centroid)
                    for centroid in centroids
                ]
                cluster = distances.index(min(distances))
                clusters[cluster].append(self._data.loc[i])

            old_centroids = centroids.copy()
            for i in range(self._k):
                centroids[i] = np.mean(clusters[i])

            if (abs(centroids - old_centroids) < tolerance).all().all() is True:
                break

        return list(clusters.values())

    def elbow_method(self):
        return 1

    def _init_centroids(self, k):
        centroids = pd.DataFrame(columns=self._data.columns)
        for i in range(k):
            centroids.loc[i] = self._data.loc[randint(0, self._n_samples)]
        return centroids

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

    def _set_k(self, k):
        if k is None:
            self._k = self.elbow_method()
        if isinstance(k, int) and k > 0:
            self._k = k
        else:
            raise TypeError('K must be positive integer.')
