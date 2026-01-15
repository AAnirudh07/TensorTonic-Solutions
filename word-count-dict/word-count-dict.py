def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    word_frequencies = dict()

    for sentence in sentences:
        for token in sentence:
            if token not in word_frequencies:
                word_frequencies[token] = 0
            word_frequencies[token] += 1
    return word_frequencies