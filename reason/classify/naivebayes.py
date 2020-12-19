# -*- coding: utf-8 -*-
"""Word tokenize module.

API:
* *NaiveBayesClassifier* (class): Naive bayes classifier.

Example:
    Train a classifier and classify new entries:
        >>> from reason.classify import NaiveBayesClassifier

        >>> classifier = NaiveBayesClassifier(train_set)
        >>> y_pred = classifier.classify(data)

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

    def classify(self, data):
        """Classify method.

        Classifies new entries (feature sets).

        Args:
            input (pandas.DataFrame or list of dict): Features set(s).

        Returns:
            Label or list of labels.

        Raises:
            Exception: If input is not valid.

        """
        if type(data) == pd.Series:
            return self._classify_data(data)
        elif type(data) == dict:
            return self._classify_data(pd.Series(data))
        elif type(data) == pd.DataFrame:
            x = data
        elif self._is_featuresets_format(data):
            x = self._featuresets_to_dataframe(data)
        else:
            raise Exception('Data type is not supported.')

        self._dataframe_validation()

        labels = list()
        for i in range(len(x)):
            labels.append(self._classify_data(x.iloc[i]))
        return labels

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

    def _classify_data(self, x):
        assert isinstance(x, pd.Series), 'X type must be pandas.Series'
        posterior = list()
        for label in self._labels:
            posterior.append((
                self._prior[str(label)] * self._likelihood(x, label), label
            ))
        return max(posterior)[1]

    def _likelihood(self, x, label):
        p = list()
        for feature in self._features:
            if type(x[feature]) in _numeric:
                mean = self._statistics[str(label)][feature]['mean']
                var = self._statistics[str(label)][feature]['var']
                if var == 0:
                    p.append(1)
                else:
                    p.append(
                        1 / np.sqrt(2 * np.pi * var)
                        * np.exp((-(x[feature] - mean) ** 2) / (2 * var))
                    )

            elif type(x[feature]) in _categorical:
                p.append((
                    self._dataset[
                        self._dataset.iloc[:, -1] == label
                    ][feature].value_counts(x[feature]) / self._n
                )[0])

            else:
                raise Exception('Input type is not supported.')

        return np.prod(p)

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

    def _pairs_to_dataframe(self, pairs):
        data = dict()
        features = pairs[0][0].keys()

        for feature in features:
            data[feature] = pd.Series(pair[0][feature] for pair in pairs)
        labels = pd.Series(pair[1] for pair in pairs)

        df = pd.DataFrame(data=data)
        df['label'] = labels

        return df

    def _featuresets_to_dataframe(self, featuresets):
        data = dict()
        features = featuresets[0].keys()

        for feature in features:
            data[feature] = pd.Series(set[feature] for set in featuresets)

        df = pd.DataFrame(data=data)

        return df
