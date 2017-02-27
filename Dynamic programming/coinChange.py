
def coin_change_2(n, m, coins):
    pass

def coin_change(n, m, coins):
    """
    :param n: total coin change
    :param m: no. of coins
    :param coins: list of m coins with corresponding value
    :return:
    """
    c = [[0] * (n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(0, n+1):
            if coins[i-1] < j:
                c[i][j] = c[i-1][j] + c[i][j-coins[i-1]]
            elif coins[i-1] == j:
                c[i][j] = c[i-1][j] + 1
            else:
                c[i][j] = c[i-1][j]
    print c
    return c[m][n]

n, m = (map(int, raw_input().strip().split(' ')))
coins = map(int, raw_input().strip().split(' '))
print coin_change(n, m, coins)
