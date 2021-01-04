import pandas as pd

from reason.metrics import euclidean_distance as euclidean
from ._clusterer import BaseClusterer


class DBSCAN(BaseClusterer):
    """DBSCAN clusterer

    Clustering using DBSCAN algorithm.

    """
    def fit(self, data, min_pts=3, eps=0.13, distance=euclidean, verbose=1):
        """Fit method.

        Args:
            data (pandas.DataFrame or list of dict): Data to cluster.
            min_pts (int): Minimum number of points required to form a cluster.
            eps (float): Epsilon.
            distance (function, optional): Distance function.
            verbose (int, optional): Verbosity mode.

        Returns:
            labels (list): Data cluster labels.

        Raises:
            TypeError: If input data type is not valid.
            ValueError: If input data value is not valid.

        """
        super().fit(data, distance, verbose)
        self._set_min_pts(min_pts)
        self._set_eps(eps)

    def _set_min_pts(self, min_pts):
        if isinstance(min_pts, int) and min_pts > 0:
            self._min_pts = min_pts
        else:
            raise ValueError('min_pts must be positive integer.')

    def _set_eps(self, eps):
        if isinstance(eps, float) and eps > 0:
            self._eps = eps
        else:
            raise ValueError('min_pts must be positive float number.')
