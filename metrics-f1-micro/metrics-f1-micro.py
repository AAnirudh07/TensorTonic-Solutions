def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    true_positives = sum(y_true[i] == y_pred[i] for i in range(len(y_true)))
    return true_positives / len(y_true)
    