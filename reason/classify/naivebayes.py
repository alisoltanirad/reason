import numpy as np


class NaiveBayesClassifier:

    def __init__(self):
        pass

    def classify(self, x):
        posterior = dict()
        for label in self._labels:
            posterior[str(label)] = self._prior[str(label)] * self._likelihood(x, label)

    def train(self, dataset):
        n = len(dataset)

        y = list()
        for data in dataset:
            y.append(data[1])
        self._labels = set(y)

        features = dataset[0][0].keys()
        x = dict()

        for label in self._labels:
            x[str(label)] = dict()
            for feature in features:
                x[str(label)][feature] = list()

        for data in dataset:
            label = data[1]
            for feature in features:
                x[str(label)][feature].append(data[0][feature])


        self._prior = dict()
        for label in self._labels:
            self._prior[str(label)] = y.count(label) / n

        self._statistics = dict()
        for label in self._labels:
            features = dict()
            for feature in features:
                features[feature] = {
                    'mean': np.mean(x[str(label)][feature]),
                    'var': np.var(x[str(label)][feature]),
                }
            self._statistics[str(label)] = features


    def _likelihood(self, x, y):
        pass

