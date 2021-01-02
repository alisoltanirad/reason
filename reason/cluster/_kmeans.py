from random import randint
from sys import maxsize

import numpy as np
import pandas as pd

from reason._mixins import progress_bar
from reason.metrics import (
    euclidean_distance, manhattan_distance, hamming_distance
)
from ._clusterer import BaseClusterer

# Available distance functions
_distance_funcs = {
    'euclidean': euclidean_distance,
    'manhattan': manhattan_distance,
    'hamming': hamming_distance,
}


class KMeansClusterer(BaseClusterer):
    """K-means clusterer

    Clustering using k-means algorithm.

    Example:
        >>> from reason.cluster import KMeansClusterer
        >>> clusterer = KMeansClusterer()
        >>> clusters = clusterer.fit(x, k=2)
        >>> pred = clusterer.predict(new_data)

    """
    def fit(self, data, k=2, distance='euclidean', max_iter=8, verbose=1):
        """Fit method.

        Clusters data to k groups.

        "distance" parameter can be a function taking 2 vectors and returning
        distance between them or a ready-to-use distance function name.
        Ready-to-use distances are: 'euclidean', 'manhattan' and 'hamming'.

        "verbose" can be 0 or 1. 1 verbosity mode shows algorithm progress in
        the console.

        Args:
            data (pandas.DataFrame or list of dict): Data to cluster.
            k (int, optional): Number of clusters.
            distance (function, optional): Distance function.
            max_iter (int, optional): Maximum number of algorithm iterations.
            verbose (int, optional): Verbosity mode.

        Returns:
            labels (list): Data cluster labels.

        Raises:
            TypeError: If input data is not valid.

        """
        self._set_data(data)
        self._set_k(k)
        self._set_distance(distance)

        if self._k == 1:
            return self._data

        self._n_samples = self._data.shape[0]
        centroids = self._init_centroids(self._k)
        tolerance = (np.max(abs(self._data)) - np.min(abs(self._data))) / 100
        clusters = dict()
        iter = 0

        while iter < max_iter:

            for i in range(self._k):
                clusters[i] = pd.DataFrame(columns=self._data.columns)

            for i in range(self._n_samples):
                distances = [
                    self._distance(self._data.loc[i], centroids.loc[j])
                    for j in range(self._k)
                ]
                cluster = distances.index(min(distances))
                clusters[cluster] = clusters[cluster].append(self._data.loc[i])

            old_centroids = centroids.copy()
            for i in range(self._k):
               centroids.loc[i] = np.mean(clusters[i])

            if (abs(centroids - old_centroids) < tolerance).all().all() is True:
               break

            if verbose == 1:
                progress_bar(iter + 1, max_iter, prefix='Progress')

            iter += 1

        self._clusters = clusters
        self._centroids = centroids

        labels = [-1 for i in range(self._n_samples)]
        for i in range(self._k):
            for j in clusters[i].index:
                labels[j] = i

        return np.array(labels)

    def predict(self, data):
        """Predict method.

        Clusters new entries (feature sets).

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

    def get_clusters(self):
        """Get clusters method

        Returns:
            list: Clusters

        Raises:
            NameError: If data is not fitted yet.

        """
        try:
            return list(self._clusters.values())
        except NameError:
            raise NameError('Fit your data using fit method.')

    def get_features(self):
        """Get features method.

        Returns:
            List: Features

        """
        return list(self._data)

    def _init_centroids(self, k):
        centroids = pd.DataFrame(columns=self._data.columns)
        centroids.loc[0] = self._find_first_centroid()
        for i in range(1, k):
            centroids.loc[i] = self._find_next_centroid(centroids)
        return centroids

    def _find_first_centroid(self):
        return self._data.loc[randint(0, self._n_samples - 1)]

    def _find_next_centroid(self, centroids):
        distances = []
        for i in range(self._n_samples):
            point = self._data.loc[i]
            min_dist = maxsize

            for j in range(len(centroids)):
                temp_dist = self._distance(point, centroids.loc[j])
                min_dist = min(min_dist, temp_dist)

            distances.append(min_dist)

        index = distances.index(max(distances))
        return self._data.loc[index]

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

    def _predict_data(self, x):
        assert isinstance(x, pd.Series), 'X data type must be pandas.Series'
        try:
            centroids = self._centroids
        except NameError:
            raise NameError('Fit your data using fit method.')
        distances = [
            self._distance(x, centroids.loc[i])
            for i in range(self._k)
        ]
        return distances.index(min(distances))
