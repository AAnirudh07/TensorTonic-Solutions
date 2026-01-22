import numpy as np

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    """
    Normalize an array along a specified axis using a specified norm.
    """
    if norm_type not in ["l1", "l2", "max"]:
        return None

    x = np.array(matrix, dtype=float)
    if x.ndim != 2 or axis not in [0,1,None]:
        return None

    if norm_type == "l1":
        norms  = np.sum(np.abs(x), axis=axis, keepdims=True)
    elif norm_type == "l2":
        norms = np.sqrt(np.sum(np.square(x), axis=axis, keepdims=True))
    else:
        norms = np.max(x, axis=axis, keepdims=True)

    norms = np.where(norms>0, norms, 1.0)
    normalized = x / norms
    return normalized
