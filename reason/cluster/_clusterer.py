import pandas as pd


class BaseClusterer:
    """Base Clusterer

    Base class for clusterers.

    """
    def predict(self, data):
        """Predict method.

        Clusters new entries (feature sets).

        Args:
            data (pandas.DataFrame or list of dict): Features set(s).

        Returns:
            Label or list of labels.

        Raises:
            TypeError: If input data type is not supported.
            ValueError: If input data is not valid.

        """
        if type(data) == pd.Series:
            return self._predict_data(data)
        elif type(data) == dict:
            return self._predict_data(pd.Series(data))
        elif type(data) == pd.DataFrame:
            x = data
        elif self._is_featuresets_format(data):
            x = self._featuresets_to_dataframe(data)
        else:
            raise TypeError('Input data type is not supported.')

        labels = list()
        for i in range(len(x)):
            labels.append(self._predict_data(x.iloc[i]))
        return labels

    def get_clusters(self):
        """Get clusters method

        Returns:
            list: Clusters

        Raises:
            NameError: If data is not fitted yet.

        """
        try:
            return list(self._clusters.values())
        except AttributeError:
            raise AttributeError('Fit your data using fit method.')

    def get_features(self):
        """Get features method.

        Returns:
            List: Features

        """
        return list(self._data)

    def inertia(self):
        """Inertia score.

        Sum of distances between points and center of their clusters.

        Returns:
              inertia (float): Inertia score.

        """
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
