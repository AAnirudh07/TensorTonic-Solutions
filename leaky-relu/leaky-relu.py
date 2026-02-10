import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    x = np.atleast_1d(x)
    # return np.maximum(x, 0.0) + alpha*np.minimum(x, 0.0)
    return np.where(x>0, x, alpha*x)