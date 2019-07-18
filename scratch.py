"""
Problem:


Approach/Solution:


Notes:

Compexity:
 Time: O(n)
 Space:


Source:
None
"""


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

# n, m = (map(int, raw_input().strip().split(' ')))
# coins = map(int, raw_input().strip().split(' '))
# print coin_change(n, m, coins)

def licence_key_formatter(S, K):
    s = S[::-1]
    res = []
    count = 0

    for idx, char in enumerate(s):
        if char == '-':
            continue
        if count != 0  and count % K == 0:
            res.append('-')
        res.append(char.upper())
        count += 1
    print ''.join(res[::-1])

class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        # convert lower to upper
        # between groups of K characters
        s = S[::-1]
        res = []
        count = 0

        for idx, char in enumerate(s):
            if char == '-':
                continue
            if count != 0  and count % K == 0:
                res.append('-')
            res.append(char.upper())
            count += 1
        return ''.join(res[::-1])

s = '5F3Z-2e-9-w'
s = '2-5g-3-J'
licence_key_formatter(s, 4)
