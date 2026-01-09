import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # n = len(v)
    # result = np.zeros((n,n), dtype=type(v[0]))
    # for i in range(n):
    #     result[i, i] = v[i]
    # return result
    return np.diag(np.array(v))    
