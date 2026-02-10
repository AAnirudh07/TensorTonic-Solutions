import numpy as np

def bootstrap_mean(x, n_bootstrap=1000, ci=0.95, rng=None):
    """
    Returns: (boot_means, lower, upper)
    """
    x = np.asarray(x)

    alpha = 1 - ci
    indices = None
    n = x.shape[0]
    size = (n_bootstrap, n)

    if rng is not None:
        indices = rng.integers(n, size=size)
    else:
        indices = np.random.choice(n, size=size)
    
    B = x[indices].mean(axis=1)
    return (
        B,
        np.quantile(B, alpha/2),
        np.quantile(B, 1-alpha/2)
    )    