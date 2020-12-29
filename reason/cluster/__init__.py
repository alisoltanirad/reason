# -*- coding: utf-8 -*-
"""cluster package.

Clustering tools using machine learning methods.

API:

* KMeansClusterer (class): Clusterer which uses k-means algorithm.
* euclidean_distance (function): Measures euclidean distance of two vectors.
* manhattan_distance (function): Measures manhattan distance of two vectors.
* hamming_distance (function): Measures hamming distance of two vectors.

"""

from ._kmeans import KMeansClusterer
from ._distance import (
    euclidean_distance, manhattan_distance, hamming_distance
)