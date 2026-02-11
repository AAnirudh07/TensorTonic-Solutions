import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    x = np.asarray(x)
    axis=None if x.ndim == 1 else 1

    max_val = np.max(x, axis=axis, keepdims=True)

    scaled_vals = x - max_val

    exps = np.exp(scaled_vals)

    return exps/np.sum(exps, axis=axis, keepdims=True)