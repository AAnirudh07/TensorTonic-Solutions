import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    return np.abs(np.array(x) - np.array(y), dtype=float).sum()