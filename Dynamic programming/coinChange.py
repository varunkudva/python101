"""
Coin change problem:
Given amount n and a set of denominations D = [s1, s2, ... sm],
count number of ways the make change for n with denomiations.

NOTE: There is infinite supply of denominations.

Solution:
To count the total number of ways to make change for n with m denominations
- Count no. of ways to make change n with m-1. Solutions that do not contain Sm
- Count no. of ways to make change n-Sm with m. Solutions that contain atleast one Sm.

    c[m, n] = c[m-1, n] + c[m, n-sm]

DP relation:
    C[i, j] =   c[i-1, j] if D[i] > j
                c[i-1, j] + 1 if D[i] == j
                c[i-1][j] + c[i-1][j-D[i]] if D[i] < j
"""


def coin_change_r(amt, m, coins):
    # recursive
    if amt == 0:
        return 1
    elif amt < 0:
        return 0
    elif m <= 0 and amt >= 1:
        # if there are no coins and amount is still > 0
        # no solution exists
        return 0
    else:
        return coin_change_r(amt, m - 1, coins) + coin_change_r(amt - coins[m - 1], m, coins)


def coin_change_dp(n, m, coins):
    """
    :param n: total coin change
    :param m: no. of coins
    :param coins: list of m coins with corresponding value
    :return:
    """
    c = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(0, n + 1):
            if coins[i - 1] < j:
                c[i][j] = c[i - 1][j] + c[i][j - coins[i - 1]]
            elif coins[i - 1] == j:
                c[i][j] = c[i - 1][j] + 1
            else:
                c[i][j] = c[i - 1][j]
    print c
    return c[m][n]


if __name__ == '__main__':
    # n, m = (map(int, raw_input().strip().split(' ')))
    # coins = map(int, raw_input().strip().split(' '))
    n = 4
    coins = [1, 2, 3]
    print "Recursive no. of ways: {}".format(coin_change_r(n, len(coins), coins))
    print "DP no. of ways: {}".format(coin_change_dp(n, len(coins), coins))
