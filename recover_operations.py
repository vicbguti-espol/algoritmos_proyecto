def recover_operations(X, Y, m, n, dp):
    """
    Retrieves the sequence of edit operations needed to transform one string into the other.

    Args:
        X (str): The first input string.
        Y (str): The second input string.
        m (int): The length of string X.
        n (int): The length of string Y.
        dp (list): The dynamic programming table used to calculate the edit distance.

    Returns:
        list: The sequence of edit operations.
    """
    i, j = m, n
    operations = []

    while i > 0 or j > 0:
        if i > 0 and dp[i][j] == dp[i - 1][j] + 1:
            operations.append(f"Remover {X[i - 1]}")
            i -= 1
        elif j > 0 and dp[i][j] == dp[i][j - 1] + 1:
            operations.append(f"Insertar {Y[j - 1]}")
            j -= 1
        else:
            if i > 0 and j > 0 and X[i - 1] != Y[j - 1]:
                operations.append(f"Reemplazar {X[i - 1]} con {Y[j - 1]}")
            i -= 1
            j -= 1

    operations.reverse()
    return operations
