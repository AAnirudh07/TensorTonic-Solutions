import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    output = np.empty((A.shape[1], A.shape[0]), dtype=A.dtype)
    rows, cols = A.shape[0], A.shape[1]

    for i in range(rows):
        for j in range(cols):
            output[j, i] = A[i, j]
    return output 