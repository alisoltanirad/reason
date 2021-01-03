# -*- coding: utf-8 -*-
"""cluster package.

Clustering tools using machine learning methods.

API:

* KMeansClusterer (class): Clusterer using k-means(++) algorithm.
* elbow_method (function): Finds optimum number of clusters.

"""

from ._kmeans import KMeansClusterer
from ._elbow_method import elbow_method
