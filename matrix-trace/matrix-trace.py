import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    if len(A) != len(A[0]):
        raise ValueError()
    return sum(A[i][i] for i in range(len(A)))