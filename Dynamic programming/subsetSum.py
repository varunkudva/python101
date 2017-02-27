"""
Subset sum problem:
Given a set of non-negative integers, and a value sum, determine if there is a subset of the
given set with sum equal to given sum.

Solution:
Given: arr[], size = n, sum = m

lets say subsetSum api returns true if there is a subset for given sum
Solution may either include the ith element or not include it.
Recursive definition is:
    subsetSum(arr, n, m) = subsetSum(arr, n-1, m) or subsetSum(arr, n-1, m-a[n])
    subsetSum(arr, 0, m) = 0, if m > 0 and there are no elements
    subsetSum(arr, n, 0) = 1, if m =0  returns empty set

This can be build bottom up in DP fashion by defining S[i][j]
        S[i][j] = True if there is a subset in arr[0...i] with sum j

        Answer would be in S[n][m]
"""
def print_set(arr, res, s, i, j, n, sum):
    if sum == 0:
        print res
        return
    if i < 0 or j < 0:
        return

    if s[i][j] == 1:
        if arr[i] <= j and s[i-1][j-arr[i]]:
            res.insert(0, arr[i])
            print_set(arr, res, s, i-1, j-arr[i], n, sum-arr[i])
            res.pop(0)
        if s[i-1][j]:
            print_set(arr, res, s, i-1, j, n, sum)

def subset_sum_dp(arr, m, n):
    """
     s[i][j] is true if a subset exists in 0..i with sum j
    """
    s = [[0] * (m+1) for _ in range(n)]
    for i in range(0, n):
        s[i][0] = 1

    if arr[0] < m:
        s[0][arr[0]] = 1

    for i in range(1, n):
        for j in range(1, (m+1)):
            s[i][j] = s[i-1][j]
            if arr[i] <= j:
                s[i][j] = s[i-1][j-arr[i]] or s[i-1][j]

    if s[n-1][m]:
        # subset(s) exists
        print_set(arr, s, n-1, m)

    return s[n-1][m]

if __name__ == '__main__':
    A = [3, 34, 4, 12, 5, 2]
    sum = 9
    print "subset exists:", subset_sum_dp(A, sum, len(A))
