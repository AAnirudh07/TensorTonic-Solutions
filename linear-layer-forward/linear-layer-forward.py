def linear_layer_forward(X, W, b):
    """
    Compute the forward pass of a linear (fully connected) layer.
    """
    n, din, dout = len(X), len(X[0]), len(W[0])
    Y = [[0.0 for _ in range(dout)] for _ in range(n)]

    if len(b) == 1:
        b = [b[0] for _ in range(dout)]
    
    for i in range(n):
        for j in range(dout):
            result = 0.0
            for k in range(din):
                result += X[i][k]*W[k][j]
            Y[i][j] = result + b[j]
    
    return Y

