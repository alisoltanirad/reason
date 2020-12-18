# -*- coding: utf-8 -*-
"""Word tokenize module.

API:
* *NaiveBayesClassifier* (class): Naive bayes classifier.

"""
import numpy as np

# Supported feature types
_numeric = [int, float, bool]
_categorical = [str]


class NaiveBayesClassifier:
    """Naive Bayes Classifier

    Uses gaussian distribution when dealing with continuous data.

    """

    def __init__(self, dataset=None):
        """Naive Bayes Classifier Constructor.

        Trains classifier when dataset is given, otherwise use train method.

        Args:
            dataset (list, optional): Dataset for training.

        """

        if dataset != None:
            self.train(dataset)

    def train(self, dataset):
        """Train method.

        Trains classifier with dataset.

        Args:
            dataset (list of tuple): Feature sets + labels

        Raises:
            Exception: If input is not a list of tuples of feature set and label.

        """
        if type(dataset) != list:
            raise Exception('Dataset must be in the form of list of tuples.')
        elif not all(isinstance(item, tuple) for item in dataset):
            raise Exception('Dataset must be in the form of list of tuples.')
        elif not all(len(item) == 2 for item in dataset):
            raise Exception('Tuples in the dataset must have 2 values.')
        elif not all(isinstance(item[0], dict) for item in dataset):
            raise Exception('Feature set must be a dictionary.')

        if all(isinstance(item[1], str) for item in dataset):
            self._is_label_bool = False
        elif all(isinstance(item[1], bool) for item in dataset):
            self._is_label_bool = True
        else:
            raise Exception('Labels must be string or boolean.')

        self._n = len(dataset)

        y = list()
        for data in dataset:
            y.append(data[1])
        self._labels = set(y)

        self._features = list(dataset[0][0].keys())
        self._x = dict()

        for label in self._labels:
            self._x[str(label)] = dict()
            for feature in self._features:
                self._x[str(label)][feature] = list()

        for data in dataset:
            label = data[1]
            for feature in self._features:
                self._x[str(label)][feature].append(data[0][feature])


        self._prior = dict()
        for label in self._labels:
            self._prior[str(label)] = y.count(label) / self._n



        self._statistics = dict()
        for label in self._labels:
            features = dict()
            for feature in self._features:
                if type(self._x[str(label)][feature][0]) in _numeric:
                    features[feature] = {
                        'mean': np.mean(self._x[str(label)][feature]),
                        'var': np.var(self._x[str(label)][feature]),
                    }
            self._statistics[str(label)] = features

    def classify(self, x):
        """Classify method.

        Classifies new entries (feature sets).

        Args:
            x (dict or list of dict): Features set(s).

        Returns:
            Label or list of labels.

        Raises:
            Exception: If input is not a dictionary or list of dictionaries.

        """
        if type(x) == dict:
            return self._classify_instance(x)
        elif type(x) == list:
            if all(isinstance(item, dict) for item in x):
                labels = list()
                for instance in x:
                    labels.append(self._classify_instance(instance))
                return labels
            else:
                raise Exception('Input type is not supported.')
        else:
            raise Exception('Input type is not supported.')

    def get_labels(self):
        """Get labels method.

        Returns:
            List: Labels

        """
        return list(self._labels)

    def get_features(self):
        """Get features method.

        Returns:
            List: Features

        """
        return self._features

    def _classify_instance(self, x):
        posterior = list()
        for label in self._labels:
            posterior.append((
                self._prior[str(label)] * self._likelihood(x, str(label))
                , str(label)
            ))

        label = max(posterior)[1]
        if self._is_label_bool == True:
            return bool(label)
        return label

    def _likelihood(self, x, y):
        p = list()
        for feature in self._features:
            if type(x[feature]) in _numeric:
                mean = self._statistics[y][feature]['mean']
                var = self._statistics[y][feature]['var']
                p.append(
                    1 / np.sqrt(2 * np.pi * var)
                    * np.exp((-(x[feature] - mean) ** 2) / (2 * var))
                )
            elif type(x[feature]) in _categorical:
                p.append(
                    self._x[y][feature].count(x[feature]) / self._n
                )
            else:
                raise Exception('Input type is not supported.' + str(x[feature]))
        return np.prod(p)
