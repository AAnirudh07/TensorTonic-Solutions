import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # mean = sum(x) / len(x)
    
    # median = None
    # if len(x)%2 == 0:
    #     median = (x[len(x)//2] + x[(len(x)//2) - 1]) / 2
    # else:
    #     median = x[len(x)//2] 

    # counts = Counter(x)
    # mode = None
    # freq = -1

    # for item, count in counts.items():
    #     if count > freq or (count == freq and item < mode):
    #         mode = item
    #         freq = count

    # return float(mean), float(median), float(mode)
    mean = np.mean(x, dtype=float)

    median = np.median(x)

    counts = Counter(x)
    mode, freq = None, -1

    for item, count in counts.items():
        if count > freq or (count == freq and item < mode):
            mode = item
            freq = count

    return mean, median, mode



