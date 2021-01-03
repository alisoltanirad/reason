import numpy as np


def elbow_method(data, clusterer, max_k, verbose=1):
    k_range = range(1, max_k + 1)
    scores = []
    for i in k_range:
        if verbose == 1:
            print('k = {}:'.format(i))
        model = clusterer()
        model.fit(data, k=i, verbose=verbose)
        scores.append(model.inertia())

    return np.array(scores)
