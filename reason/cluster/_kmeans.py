from random import randint
from sys import maxsize

import numpy as np
import pandas as pd

from reason._mixins import progress_bar
from reason.metrics import euclidean_distance as euclidean

from ._clusterer import BaseClusterer


class KMeansClusterer(BaseClusterer):
    """K-means clusterer

    Clustering using k-means algorithm.

    Example:
        >>> from reason.cluster import KMeansClusterer
        >>> clusterer = KMeansClusterer()
        >>> labels = clusterer.fit(x, k=2)
        >>> pred = clusterer.predict(new_data)

    """

    def __init__(self):
        super().__init__()
        self._centroids = None
        self._tolerance = None

    def fit(self, data, k=2, distance=euclidean, max_iter=21, verbose=1):
        """Fit method.

        Clusters data to k groups.

        "distance" parameter can be a function taking 2 vectors and returning
        distance between them in the form of a float number.

        "verbose" can be 0 or 1. 1 verbosity mode shows algorithm progress in
        the console.

        Args:
            data (pandas.DataFrame or list of dict): Data to cluster.
            k (int, optional): Number of clusters.
                Default=2
            distance (function, optional): Distance function.
                Default=euclidean
            max_iter (int, optional): Maximum number of algorithm iterations.
                Default=21
            verbose (int, optional): Verbosity mode.
                Default=1

        Returns:
            labels (list): Data cluster labels.

        Raises:
            TypeError: If input data type is not valid.
            ValueError: If input data value is not valid.

        """
        super().fit(data, distance)
        self._set_k(k)
        self._set_max_iter(max_iter)
        self._set_tolerance()
        self._init_centroids(self._k)

        return self._cluster(verbose)

    def _cluster(self, verbose):
        itr = 0

        while itr < self._max_iter:
            self._init_clusters()
            self._set_clusters()

            old_centroids = self._centroids.copy()
            self._update_centroids()

            if (abs(self._centroids - old_centroids) < self._tolerance).all().all():
                if verbose == 1:
                    progress_bar(self._max_iter, self._max_iter, prefix="Progress")
                break

            if verbose == 1:
                progress_bar(itr + 1, self._max_iter, prefix="Progress")

            itr += 1

        labels = self._set_labels()

        return np.array(labels)

    def inertia(self):
        """Inertia score.

        Sum of distances between points and center of their clusters.

        Returns:
              inertia (float): Inertia score.

        """
        inertia = 0
        for i in range(len(self._clusters)):
            for j in self._clusters[i].index:
                inertia += self._distance(
                    self._clusters[i].loc[j], self._centroids.loc[i]
                )
        return inertia

    def _set_labels(self):
        labels = [-1] * self._n
        for i in range(self._k):
            for j in self._clusters[i].index:
                labels[j] = i
        return labels

    def _init_clusters(self):
        for i in range(self._k):
            self._clusters[i] = pd.DataFrame(columns=self._data.columns)

    def _set_clusters(self):
        for i in range(self._n):
            distances = [
                self._distance(self._data.loc[i], self._centroids.loc[j])
                for j in range(self._k)
            ]
            cluster = distances.index(min(distances))
            self._clusters[cluster] = self._clusters[cluster].append(self._data.loc[i])

    def _init_centroids(self, k):
        self._centroids = pd.DataFrame(columns=self._data.columns)
        self._centroids.loc[0] = self._find_first_centroid()
        for i in range(1, k):
            self._centroids.loc[i] = self._find_next_centroid()

    def _find_first_centroid(self):
        return self._data.loc[randint(0, self._n - 1)]

    def _find_next_centroid(self):
        distances = []
        for i in range(self._n):
            point = self._data.loc[i]
            min_dist = maxsize

            for j in range(len(self._centroids)):
                temp_dist = self._distance(point, self._centroids.loc[j])
                min_dist = min(min_dist, temp_dist)

            distances.append(min_dist)

        index = distances.index(max(distances))
        return self._data.loc[index]

    def _update_centroids(self):
        for i in range(self._k):
            self._centroids.loc[i] = np.mean(self._clusters[i])

    def _set_k(self, k):
        if isinstance(k, int) and k > 0:
            self._k = k
        else:
            raise ValueError("K must be positive integer.")

    def _set_max_iter(self, max_iter):
        if isinstance(max_iter, int) and max_iter > 0:
            self._max_iter = max_iter
        else:
            raise ValueError("max_iter must be positive integer.")

    def _set_tolerance(self):
        self._tolerance = (np.max(abs(self._data)) - np.min(abs(self._data))) / 144

    def _predict_data(self, x):
        assert isinstance(x, pd.Series), "X data type must be pandas.Series"
        if self._centroids is None:
            raise AttributeError("Fit your data using fit method.")
        distances = [self._distance(x, self._centroids.loc[i]) for i in range(self._k)]
        return distances.index(min(distances))
