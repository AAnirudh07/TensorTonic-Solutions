import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """    
    if len(seqs) == 0:
      return np.empty((0, 0), dtype=int)
    
    max_len = max_len if max_len is not None else max(len(seq) for seq in seqs)
    
    output = []
    for seq in seqs:
      padded_sequence = seq[:min(max_len, len(seq))] + [pad_value]*max(0, max_len - len(seq)) 
      output.append(padded_sequence)
    return np.asarray(output)
    
