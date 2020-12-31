# -*- coding: utf-8 -*-
"""metrics package.

Machine learning evaluation metrics.

API:

* ConfusionMatrix (class): Forms up confusion matrix of given values.
* BinaryConfusionMatrix (class): Matrix for cases with only 2 label values.
* accuracy (function): Easy-to-use accuracy calculator.
* euclidean_distance (function): Measures euclidean distance of two vectors.
* manhattan_distance (function): Measures manhattan distance of two vectors.
* hamming_distance (function): Measures hamming distance of two vectors.

"""

from ._confusion_matrix import ConfusionMatrix, BinaryConfusionMatrix
from ._accuracy import accuracy
from ._distance import (
    euclidean_distance, manhattan_distance, hamming_distance
)
