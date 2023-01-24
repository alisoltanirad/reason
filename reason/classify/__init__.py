# -*- coding: utf-8 -*-
"""classify package.

Classification tools using machine learning methods.

API:

* NaiveBayesClassifier (class): Classifier which uses naive bayes algorithm.
* KNNClassifier (class): Classifier which uses KNN algorithm.
* DecisionTreeClassifier (class): Classifier which uses decision tree algorithm.

"""

from ._decisiontree import DecisionTreeClassifier
from ._knn import KNNClassifier
from ._naivebayes import NaiveBayesClassifier
