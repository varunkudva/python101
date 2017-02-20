"""
Given two strings, find length of longest common subsequence and print them.
subsequence can be non-contiguous in the strings.
Eg:
x = abcbdab, y = bdcaba. lcs is bcba of length 4.
"""

def lcs_simple(x, y):
    def print_lcs(x, y , i, j, c):
        if i == 0 or j == 0:
            return
        if c[i][j] == c[i-1][j-1]+1:
            print_lcs(x, y, i-1, j-1, c)
            print x[i-1],
        elif c[i][j] == c[i-1][j]:
            print_lcs(x, y, i-1, j, c)
        else:
            print_lcs(x, y, i, j-1, c)

    """
    lcs_simple uses a m*n matrix to store lcs of prefixes of
    the string, in order to compute lcs at the current index
    """
    m, n = len(x), len(y)
    c = [[0] * (n+1) for _ in range(m+1)]
    i, j = 0,0

    # row 0 and column 0 are all 0s as there is no lcs
    # if one of the strings is null
    for i in range(m+1):
        c[i][0] = 0
    for j in range(n+1):
        c[0][j] = 0

    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i][j-1], c[i-1][j])

    print_lcs(x, y, m, n, c)
    return c[m][n]



if __name__ == '__main__':
    print "Length: {}".format(lcs_simple("abcbdab","bdcaba"))

