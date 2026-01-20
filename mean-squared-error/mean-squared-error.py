import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    nx, ny = np.array(y_pred), np.array(y_true)
    mse_res = np.square(nx-ny).sum() / nx.shape[0]
    return mse_res