def edit_distance(X, Y, m, n):
    """
    Calculates the minimum edit distance between two strings.

    Args:
        X (str): The first input string.
        Y (str): The second input string.
        m (int): The length of string X.
        n (int): The length of string Y.

    Returns:
        int: The minimum edit distance between X and Y.
    """
    
    m = len(X)
    n = len(Y)
    
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else: 
                dp[i][j] = min(
                    dp[i - 1][j] + 1,     
                    dp[i][j - 1] + 1,      
                    dp[i - 1][j - 1] + 1   
                )
    return dp[m][n], dp
