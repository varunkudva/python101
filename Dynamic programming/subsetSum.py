"""
Subset sum problem
Given a set of pos­i­tive inte­gers, and a value sum S, find out if there exist a sub­set in
array whose sum is equal to given sum S.

Backtracking:

DP:

"""
def print_set(arr, s, i, j):
        return
    if s[i][j] == 1:
        if s[i-1][j]:
            print_set(arr, s, i-1, j)
        else:
            print_set(arr, s, i-1, j-arr[i])

        res.append(arr[i])


def subset_sum_dp(arr, sum, n):
    """
     s[i][j] is true if a subset exists in 0..i with sum j
    """
    s = [[0] * (sum+1) for _ in range(n)]
    for i in range(0, n):
        s[i][0] = 1

    if arr[0] < sum:
        s[0][arr[0]] = 1

    for i in range(1, n):
        for j in range(1, (sum+1)):
            if arr[i] <= j:
                s[i][j] = s[i-1][j-arr[i]] || s[i-1, j]

    res = []
    print_set(arr, res, s, i, j)
    return s[n][m]

if __name__ == '__main__':
    A = [3, 34, 4, 12, 5, 2]
    sum = 9
    print "subset exists:", subset_sum_dp(arr, sum, len(A))

