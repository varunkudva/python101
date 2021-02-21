"""
Total no. of ways to make change 'n' with denominations 'm'
dp[i,j] : no. of ways to make change j with i denominations
dp[i,j] = dp[i-1, j] + dp[i, j-d[i]] if d[i] <= j
          dp[i-1,j] if dp[i] > 0
          dp[i][0] = 1

orig ans: dp[m,n]
"""
def coin_change(denominations, n):
    """
    :param denominations:
    :param n:
    :return:
    """
    def print_res(dp):

    m = len(denominations)
    dp = [[0] * (n+1) for _ in range(m+1)]
    dp[0][0] = 1
    for i in range(1, m+1):
        for j in range(0, n+1):
            if denominations[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-denominations[i-1]]

    return dp[m][n]



n = 4
coins = [1, 2, 3]
print (coin_change(coins, n))
