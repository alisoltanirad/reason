def elbow_method(data, clusterer, max_k):
    """Elbow method function.

    Takes dataset, "Reason" clusterer class and returns the optimum number of
    clusters in range of 1 to max_k.

    Args:
        data (pandas.DataFrame or list of dict): Data to cluster.
        clusterer (class): "Reason" clusterer.
        max_k (int): Maximum k to analysis.

    Returns:
        k (int): Optimum number of clusters.

    """
    k = None
    score = _get_score(data, clusterer, 1)
    for i in range(2, max_k + 1):
        current_score = _get_score(data, clusterer, i)
        if (score - current_score) < (score / 8):
            k = i - 1
            break
        score = current_score

    if k == None:
        return max_k

    return k


def _get_score(data, clusterer, k):
    model = clusterer()
    model.fit(data, k=k, verbose=0)
    return model.inertia()
