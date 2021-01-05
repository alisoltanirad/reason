import numpy as np
import pandas as pd

from reason.metrics import euclidean_distance as euclidean
from ._clusterer import BaseClusterer


class _DistanceMatrix:
    def __init__(self, data, distance, eps):
        self._data = data
        self._distance = distance
        self._eps = eps
        self._n = self._data.shape[0]
        self._matrix = self._build_matrix()

    def neighbors(self, i):
        row = np.where(self._matrix[i] < self._eps)[0]
        return np.delete(row, np.where(row == i))

    def _build_matrix(self):
        matrix = np.zeros((self._n, self._n))
        for i in range(self._n):
            for j in range(self._n):
                matrix[i][j] = self._distance(
                    self._data.loc[i], self._data.loc[j]
                )

        return matrix


class DBSCAN(BaseClusterer):
    """DBSCAN clusterer

    Clustering using DBSCAN algorithm.

    Example:
        >>> from reason.cluster import DBSCAN
        >>> clusterer = DBSCAN()
        >>> labels = clusterer.fit(x, eps=0.21)

    """
    def fit(self, data, eps, min_pts=3, distance=euclidean, verbose=1):
        """Fit method.

        Args:
            data (pandas.DataFrame or list of dict): Data to cluster.
            eps (float): Epsilon.
            min_pts (int): Minimum number of points required to form a cluster.
            distance (function, optional): Distance function.
            verbose (int, optional): Verbosity mode.

        Returns:
            labels (list): Data cluster labels.

        Raises:
            TypeError: If input data type is not valid.
            ValueError: If input data value is not valid.

        """
        super().fit(data, distance)
        self._set_min_pts(min_pts)
        self._set_eps(eps)
        self._dist_matrix = _DistanceMatrix(self._data, distance, eps)

        self._n_samples = self._data.shape[0]
        self._clusters = dict()
        self._visited = np.zeros(self._n_samples, dtype=int)
        self._labels = np.full(self._n_samples, -1)
        cluster_index = 0

        for i in range(self._n_samples):
            if self._visited[i] == 0:
                self._visited[i] = 1

                neighbors = self._dist_matrix.neighbors(i)
                if neighbors.shape[0] >= self._min_pts:
                    cluster = self._expand_cluster(i, neighbors, cluster_index)
                    self._clusters[cluster_index] = cluster
                    cluster_index += 1

        return self._labels

    def _expand_cluster(self, init, neighbors, cluster_index):
        cluster = pd.DataFrame(columns=self._data.columns)

        cluster = cluster.append(self._data.loc[init])
        self._labels[init] = cluster_index

        reachable = list(neighbors)
        for i in reachable:
            if self._visited[i] == 0:
                self._visited[i] = 1

                new_neighbors = self._dist_matrix.neighbors(i)
                if neighbors.shape[0] >= self._min_pts:
                    for j in new_neighbors:
                        if j not in reachable:
                            reachable.append(j)

            if self._labels[i] == -1:
                cluster = cluster.append(self._data.loc[i])
                self._labels[i] = cluster_index

        return cluster

    def _set_min_pts(self, min_pts):
        if isinstance(min_pts, int) and min_pts > 0:
            self._min_pts = min_pts
        else:
            raise ValueError('min_pts must be positive integer.')

    def _set_eps(self, eps):
        try:
            self._eps = float(eps)
            assert self._eps > 0
        except (ValueError, AssertionError):
            raise ValueError('min_pts must be positive float number.')
