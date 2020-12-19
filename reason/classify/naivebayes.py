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
_numeric = [int, float, bool, np.intc , np.single, np.bool_]
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
        if type(dataset) == pd.DataFrame:
            self._dataset = dataset
        elif self._is_pairs_format(dataset):
            self._dataset = self._pairs_to_dataframe(dataset)
        else:
            raise Exception('Dataset type is not supported.')

        self._train_classifier()

    def _pairs_to_dataframe(self, pairs):
        data = dict()
        features = pairs[0][0].keys()

        for feature in features:
            data[feature] = pd.Series(pair[0][feature] for pair in pairs)
        labels = pd.Series(pair[1] for pair in pairs)

        df = pd.DataFrame(data=data)
        df['label'] = labels

        return df

    def _train_classifier(self):

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

    def classify(self, data):
        """Classify method.

        Classifies new entries (feature sets).

        Args:
            input (dict or list of dict): Features set(s).

        Returns:
            Label or list of labels.

        Raises:
            Exception: If input is not a dictionary or list of dictionaries.

        """
        if type(data) == pd.DataFrame:
            x = data
        elif self._is_featuresets_format(data):
            x = self._featuresets_to_dataframe(data)
        elif type(data) == dict:
            return self._classify_data(self._dict_to_dataframe(data))
        else:
            raise Exception('Data type is not supported.')

        self._dataframe_validation()

        labels = list()
        for i in range(len(x)):
            labels.append(self._classify_data(x.iloc[i]))
        return labels

    def _dict_to_dataframe(self, dictionary):
        data = dict()
        for key, value in dictionary.items():
            data[key] = [value]
        return pd.DataFrame(data=data)


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


    def _likelihood(self, x, label):
        p = list()
        for feature in self._features:
            if type(x[feature][0]) in _numeric:
                mean = self._statistics[str(label)][feature]['mean']
                var = self._statistics[str(label)][feature]['var']
                p.append((
                    1 / np.sqrt(2 * np.pi * var)
                    * np.exp((-(x[feature] - mean) ** 2) / (2 * var))
                )[0])

            elif type(x[feature][0]) in _categorical:
                p.append((
                    self._dataset[
                        self._dataset.iloc[:, -1] == label
                    ][feature].value_counts(x[feature][0]) / self._n
                )[0])

            else:
                raise Exception('Input type is not supported.')
        return np.prod(p)

    def _featuresets_to_dataframe(self, featuresets):
        data = dict()
        features = featuresets[0].keys()

        for feature in features:
            data[feature] = pd.Series(set[feature] for set in featuresets)

        df = pd.DataFrame(data=data)

        return df


    def _dataframe_validation(self):
        pass

    def _is_pairs_format(self, input):

        if not isinstance(input, list):
            return False
        elif not all(isinstance(item, tuple) for item in input):
            return False
        elif not all(len(item) == 2 for item in input):
            return False
        elif not all(isinstance(item[0], dict) for item in input):
            return False

        return True

    def _is_featuresets_format(self, input):

        if not isinstance(input, list):
            return False
        elif not all(isinstance(item, dict) for item in input):
            return False

        return True

class BadInput(Exception):

    def __init__(self, message='Input type is not supported.'):
        self.message = message

    def __str__(self):
        return self.message
