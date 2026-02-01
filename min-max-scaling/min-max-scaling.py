def min_max_scaling(data):
    """
    Scale each column of the data matrix to the [0, 1] range.
    """
    output = [[] for _ in range(len(data))]

    for col in range(len(data[0])):
        column_data = [row[col] for row in data]
        maxv, minv = max(column_data), min(column_data)
        for i, val in enumerate(column_data):
            output[i].append((val-minv)/(maxv-minv) if maxv != minv else 0.0)

    return output
