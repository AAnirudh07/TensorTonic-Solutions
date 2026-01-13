def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    tokens_without_stopwords = []
    stopwords_set = set(stopwords)

    for token in tokens:
        if token not in stopwords_set:
            tokens_without_stopwords.append(token)
    return tokens_without_stopwords