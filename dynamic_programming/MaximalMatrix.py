"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Return 6
Solution:
Let S(i,j) represent the size of submatrix with all 1s with i,j being the right bottom
cell in the matrix

S(i,j) = 0 if M(i,j) = 0
         min(S(i-1,j), S(i-1,j-1), S(i, j-1)) if M(i,j) = 1
         M(i,j) if i = 0 or j = 0
"""
def maximal_submatrix(M):
    m = len(M)
    n = len(M[0])
    S = [[0] * n for _ in range(m)]
    max = 0

    S[0] = M[0]
    for i in range(m):
        S[i][0] = M[i][0]

    for i in range(1, m):
        for j in range(1, n):
            if M[i][j] == 0:
                S[i][j] = 0
            else:
                S[i][j] = min(S[i-1][j], S[i][j-1], S[i-1][j-1]) + 1
                if S[i][j] > max:
                    max = S[i][j]
    print(S)
    return max

if __name__ == '__main__':
    M = [[1, 0, 1, 0, 0],
         [1, 0, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [1, 0, 0, 1, 0]]

    print(maximal_submatrix(M))
