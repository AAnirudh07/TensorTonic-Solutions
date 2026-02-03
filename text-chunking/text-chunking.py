def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    chunks = []
    start = 0
    while start < len(tokens):
        chunks.append(tokens[start:start+chunk_size])
        if start + chunk_size < len(tokens):
            start += (chunk_size - overlap)
        else:
            break

    return chunks