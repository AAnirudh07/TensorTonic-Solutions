import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    sample_mean = sum(x) / len(x)

    squared_diff = sum((x[i]-sample_mean)**2 for i in range(len(x)))
    sample_variance = squared_diff / (len(x)-1)
    sample_std_deviation = sample_variance ** 0.5

    return sample_variance, sample_std_deviation

