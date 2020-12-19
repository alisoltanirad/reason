# -*- coding: utf-8 -*-
"""Word tokenize module.

API:
* *NaiveBayesClassifier* (class): Naive bayes classifier.

Example:
    Train a classifier and classify new entries:
        >>> from reason.classify import NaiveBayesClassifier

        >>> classifier = NaiveBayesClassifier(train_set)
        >>> y_pred = classifier.classify(new_data)

        >>> classifier.get_labels()
        [True, False]
        >>> classifier.get_features()
        ['length', 'is_upper', 'ends_with']

"""
import numpy as np
import pandas as pd

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
            dataset (pandas.DataFrame or list of tuple): Feature sets + labels

        Raises:
            Exception: If input is not valid.

        """
        self._dataset = dataset
        if type(dataset) == pd.DataFrame:
            self._dataset_type = 'dataframe'
            self._train_dataframe()
        else:
            self._dataset_type = 'featureset'
            self._train_featureset()

    def _train_dataframe(self):
        self._check_input_validation()

        self._n = len(self._dataset)

        self._features = list(self._dataset.columns[:-1])
        self._labels = list(self._dataset.iloc[:, -1].unique())

        self._prior = dict()
        for label in self._labels:
            self._prior[str(label)] = \
                self._dataset.iloc[:, -1].value_counts()[label]

        self._statistics = dict()
        for label in self._labels:
            features = dict()
            for feature in self._features:
                if self._dataset[feature].dtype in _numeric:
                    features[feature] = {
                        'mean': np.mean(
                            self._dataset[
                                self._dataset.iloc[:, -1] == label
                            ][feature]
                        ),
                        'var': np.var(
                            self._dataset[
                                self._dataset.iloc[:, -1] == label
                            ][feature]
                        ),
                    }
            self._statistics[str(label)] = features

    def _train_featureset(self):
        self._check_input_validation()

        self._n = len(self._dataset)

        y = list()
        for data in self._dataset:
            y.append(data[1])
        self._labels = set(y)

        self._features = list(self._dataset[0][0].keys())
        self._x = dict()

        for label in self._labels:
            self._x[str(label)] = dict()
            for feature in self._features:
                self._x[str(label)][feature] = list()

        for data in self._dataset:
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
        if self._dataset_type == 'dataframe':
            self._dataframe_validation()
            labels = list()
            for i in range(len(x)):
                labels.append(self._classify_data(x.iloc[i]))
            return labels
        else:
            if type(x) == dict:
                return self._classify_featureset(x)
            elif type(x) == list:
                if all(isinstance(item, dict) for item in x):
                    labels = list()
                    for instance in x:
                        labels.append(self._classify_featureset(instance))
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

    def _classify_data(self, x):
        posterior = list()
        for label in self._labels:
            posterior.append((
                self._prior[str(label)] * self._likelihood(x, label), label
            ))

        return max(posterior)[1]

    def _classify_featureset(self, x):
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

    def _likelihood(self, x, label):
        p = list()
        for feature in self._features:
            if x[feature].dtype in _numeric:
                mean = self._statistics[str(label)][feature]['mean']
                var = self._statistics[str(label)][feature]['var']
                p.append(
                    1 / np.sqrt(2 * np.pi * var)
                    * np.exp((-(x[feature] - mean) ** 2) / (2 * var))
                )
            elif x[feature].dtype in _categorical:
                p.append(
                    self._dataset[
                        self._dataset.iloc[:, -1] == label
                    ][feature].value_counts(x[feature]) / self._n
                )
            else:
                raise Exception('Input type is not supported.' + str(x[feature]))
        return np.prod(p)

    def _check_input_validation(self):
        if self._dataset_type == 'dataframe':
            self._dataframe_validation()
        elif self._dataset_type == 'featureset':
            self._featureset_validation()
        else:
            raise BadInput

    def _dataframe_validation(self):
        pass

    def _featureset_validation(self):

        if not isinstance(self._dataset, list):
            raise BadInput
        elif not all(isinstance(item, tuple) for item in self._dataset):
            raise BadInput
        elif not all(len(item) == 2 for item in self._dataset):
            raise BadInput('Dataset tuples must be (featureset, label) pairs.')
        elif not all(isinstance(item[0], dict) for item in self._dataset):
            raise BadInput('Dataset feature sets must be dictionary.')

        if all(isinstance(item[1], str) for item in self._dataset):
            self._is_label_bool = False
        elif all(isinstance(item[1], bool) for item in self._dataset):
            self._is_label_bool = True
        else:
            raise BadInput('Dataset labels must be string or boolean.')


class BadInput(Exception):

    def __init__(self, message='Input type is not supported.'):
        self.message = message

    def __str__(self):
        return self.message
