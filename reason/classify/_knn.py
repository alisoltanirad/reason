from ._classifier import BaseClassifier


class KNNClassifier(BaseClassifier):
    """KNN Classifier

    K Nearest Neighbors classifier.

    Example:
        >>> from reason.classify import KNNClassifier
        >>> classifier = KNNClassifier()

    """
    def __init__(self):
        super().__init__()
        pass

    def _train_classifier(self):
        pass

    def _predict_data(self, data):
        pass
