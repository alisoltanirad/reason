from random import randint

import numpy as np
import pandas as pd

from reason._mixins import progress_bar
from reason.metrics import (
    euclidean_distance, manhattan_distance, hamming_distance
)
from ._clusterer import BaseClusterer

# Available distance metrics
_distance_funcs = {
    'euclidean': euclidean_distance,
    'manhattan': manhattan_distance,
    'hamming': hamming_distance,
}


class KMeansClusterer(BaseClusterer):
    """K-means clusterer

    Clustering using k-means algorithm.

    """
    def fit(self, data, k=2, distance='euclidean', verbose=1):
        """Fit method.

        Clusters data to k groups.

        Args:
            data (pandas.DataFrame or list of dict): Data to cluster.
            k (int, optional): Number of clusters.
            distance (optional): Function returning distance between 2 vectors.
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
        MAX_ITER = 10
        iter = 0

        while iter < MAX_ITER:

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
                progress_bar(iter, MAX_ITER, prefix='Progress')

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
        try:
            return list(self._clusters.values())
        except NameError:
            raise NameError('Fit your data using fit method.')

    def _init_centroids(self, k):
        centroids = pd.DataFrame(columns=self._data.columns)
        for i in range(k):
            centroids.loc[i] = self._data.loc[randint(0, self._n_samples - 1)]
        return centroids

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
        return
