"""
Dice Throw Problem

Given n dice each with m faces, numbered from 1 to m, find the number of ways to get sum X.
X is the summation of values on each face when all the dice are thrown.

DP Solution:
Lets define optimal structure for problem first

let w[i][j] represent no. of ways to get sum j with i dices, with m faces
on each dice:

    w[1][1] = 1, w[1][2] = 1, w[1][m] = 1
    w[1][j] = 1 if j <=  m, i.e theres only one way to get each face

    we want to find w[n][X]

    Lets say the nth dice rolls to 1, in which case, no. of ways becomes w[n-1][j-1]
    which is basically obtain sum j-1 with n-1 dices.
    Lets say the nth dice rolls to 2, in which case, no. of ways becomes w[n-1][j-2]
    which is basically obtain sum j-2 with n-2 dices.

Define recursive solution for subproblem

        w[i,j] = sum[w[i-1, j-k]], where k = (1, m)
"""
def dice_throw_r(X, n, m):
    """
    recursive method
    """
    if X == 0 and n == 0:
        return 1
    if X <= 0 or n == 0:
        return 0
    sum = 0
    for i in range(1, m+1):
        sum += dice_throw_r(X-i, n-1, m)

    return sum

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


print("Recursive No. of ways to generate sum 5 is:", dice_throw_r(X=5, n=3, m=4))
print("DP No. of ways to generate sum 5 is:", dice_throw(X=5, n=3, m=4))
