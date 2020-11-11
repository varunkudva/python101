"""
In computer science, edit distance is a way of quantifying how dissimilar two
strings (e.g., words) are to one another by counting the minimum number of
operations required to transform one string into the other.

There are three operations permitted on a word: replace, delete, insert.
For example, the edit distance between "a" and "b" is 1, the edit
distance between "abc" and "def" is 3.

Solution:
- Solution uses dynamic programming.
- D[i][j] represents the edit distance between two strings of length i,j
  respectively.


http://www.programcreek.com/2013/12/edit-distance-in-java/
"""
def edit_distance(word1, word2):
    m = len(word1)
    n = len(word2)
    d = [[0] * (n+1) for x in range(m+1)]

    for i in range(m+1):
        d[i][0] = i

    for j in range(n+1):
        d[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                d[i][j] = d[i - 1][j - 1]
            else:
                insert = d[i][j - 1] + 1
                delete = d[i - 1][j] + 1
                replace = d[i - 1][j - 1] + 1
                d[i][j] = min(insert, delete, replace)

    for i in range(m + 1):
        print((d[i]))

    return d[m][n]


word1 = eval(input())
word2 = eval(input())

print((edit_distance(word1, word2)))
