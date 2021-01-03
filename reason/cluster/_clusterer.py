import pandas as pd


class BaseClusterer:
    """Base Clusterer

    Base class for clusterers.

    """
    def inertia(self):
        inertia = 0
        for i in range(self._k):
            for j in self._clusters[i].index:
                inertia += self._distance(
                    self._clusters[i].loc[j], self._centroids.loc[i]
                )
        return inertia

    def _set_data(self, data):
        if isinstance(data, pd.DataFrame):
            self._data = data
        elif self._is_featuresets_format(data):
            self._data = self._featuresets_to_dataframe(data)
        else:
            raise TypeError(
                'Data must be pandas DataFrame object '
                'or supported featuresets format.'
            )

    def _is_featuresets_format(self, input_data):
        if (
            not isinstance(input_data, list) or
            not all(isinstance(item, dict) for item in input_data)
        ):
            return False

        return True

    def _featuresets_to_dataframe(self, featuresets):
        data = dict()
        features = featuresets[0].keys()

        for feature in features:
            data[feature] = pd.Series(set[feature] for set in featuresets)

        df = pd.DataFrame(data=data)

        return df