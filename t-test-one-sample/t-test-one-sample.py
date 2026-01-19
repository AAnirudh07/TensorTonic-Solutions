import numpy as np

def t_test_one_sample(x, mu0):
    """
    Compute one-sample t-statistic.
    """
    nx = np.array(x)
    sample_mean = np.mean(x)
    sample_std = np.sqrt((np.sum(np.square((x - sample_mean), dtype=float))) / (nx.shape[0] - 1))
    t_stat = (sample_mean - mu0) / (sample_std / np.sqrt(nx.shape[0]))
    return t_stat