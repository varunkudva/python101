"""
Given n dice each with m faces, numbered from 1 to m, find the number of ways to get sum X.
X is the summation of values on each face when all the dice are thrown.
"""


def dice_throw(X, n, m):
    """

    :param X: Total sum to be obtained with n dice roll
    :param n: number of dices
    :param m: number of faces on each dice
    :return:
    """
    w = [[0] * (X + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, X + 1):
            if i == 1 and j <= m:
                w[i][j] = 1
            else:
                for k in range(1, m + 1):
                    if k < j:
                        w[i][j] += w[i - 1][j - k]

    return w[n][X]


print "No. of ways to generate sume 5 is:", dice_throw(5, 3, 4)
