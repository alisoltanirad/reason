from ._classifier import BaseClassifier


class DecisionTreeClassifier(BaseClassifier):
    """Decision Tree Classifier

    Example:
        >>> from reason.classify import DecisionTreeClassifier
        >>> classifier = DecisionTreeClassifier()

    """
    def __init__(self):
        super().__init__()
        pass

    def _train_classifier(self):
        pass

    def _predict_data(self, data):
        pass
