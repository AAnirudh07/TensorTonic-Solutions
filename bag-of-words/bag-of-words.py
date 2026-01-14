import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    bow_vector = np.zeros(len(vocab), dtype=int)
    vocab_dict = {word: i for i, word in enumerate(vocab)}

    for token in tokens:
        if token in vocab_dict:
            bow_vector[vocab_dict[token]] += 1
        
    return bow_vector
    