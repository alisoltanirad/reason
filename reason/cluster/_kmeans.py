import pandas as pd


class KMeansClusterer:
    """K-means clusterer

    Clustering using k-means algorithm.

    """

    def __init__(self, data, k=None):
        """KMeansClusterer constructor.

        Args:
            data (pandas.DataFrame or list of dict): Data to cluster.
            k (int, optional): Number of clusters.

        Raises:
            TypeError: If input data is not valid.

        """
        if isinstance(data, pd.DataFrame):
            self._data = data
        elif self._is_featuresets_format(data):
            self._data = self._featuresets_to_dataframe(data)
        else:
            raise TypeError(
                'Data must be pandas DataFrame object '
                'or supported featuresets format.'
            )

        if k is None:
            self._k = self.elbow_method()
        elif isinstance(k, int) and k > 0:
            self._k = k
        else:
            raise TypeError('K must be positive integer.')

        


    def cluster(self):
        pass

    def elbow_method(self):
        return 1

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
