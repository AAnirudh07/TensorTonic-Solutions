import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    norm_a = np.linalg.norm(a) #np.sqrt(np.square(a, dtype=float).sum())
    norm_b = np.linalg.norm(b) #np.sqrt(np.square(b, dtype=float).sum())
    if norm_a == 0 or norm_b == 0:
        return 0

    return np.dot(a, b).item() / (norm_a * norm_b)

