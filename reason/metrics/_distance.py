import numpy as np


def euclidean_distance(u, v):
    """
    Args:
        u (array-like): Vector
        v (array-like): Vector

    Returns:
        The euclidean distance between vectors u and v.

    """
    return np.linalg.norm(np.array(u) - np.array(v))


def manhattan_distance(u, v):
    """
    Args:
        u (array-like): Vector
        v (array-like): Vector

    Returns:
        The manhattan distance between vectors u and v.

    """
    return np.abs(np.array(u) - np.array(v)).sum()


def hamming_distance(u, v):
    """
    Args:
        u (array-like): Vector
        v (array-like): Vector

    Returns:
        The hamming distance between vectors u and v.

    """
    return np.count_nonzero(np.array(u) != np.array(v))
