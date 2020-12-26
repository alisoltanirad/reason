# -*- coding: utf-8 -*-
"""metrics package.

Machine learning evaluation metrics.

API:

* ConfusionMatrix (class): Forms up confusion matrix of given values.
* BinaryConfusionMatrix (class): Matrix for cases with only 2 label values.
* accuracy (function): Easy-to-use accuracy calculator.

"""

from ._confusion_matrix import ConfusionMatrix, BinaryConfusionMatrix
from ._accuracy import accuracy
