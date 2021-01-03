# -*- coding: utf-8 -*-
"""cluster package.

Clustering tools using machine learning methods.

API:

* KMeansClusterer (class): Clusterer which uses k-means algorithm.


"""

from ._kmeans import KMeansClusterer
from ._elbow_method import elbow_method
