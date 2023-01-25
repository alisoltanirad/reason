from ._classifier import BaseClassifier


class DecisionTreeClassifier(BaseClassifier):
    """Decision Tree Classifier

    Example:
        >>> from reason.classify import DecisionTreeClassifier
        >>> classifier = DecisionTreeClassifier()

    """

    def __init__(self):
        raise NotImplementedError(
            "Decision tree classifier will be implemented in future versions."
        )

    def _train_classifier(self):
        pass

    def _predict_data(self, data):
        pass
