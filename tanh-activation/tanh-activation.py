import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    if not isinstance(x, list):
        x = [x]
    x = np.asarray(x, dtype=float)
    return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))