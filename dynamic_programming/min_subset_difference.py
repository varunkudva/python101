"""
Given a set of positive numbers, partition the set into two subsets with a minimum difference between their subset sums.

Example 1: #
Input: {1, 2, 3, 9}
Output: 3
Explanation: We can partition the given set into two subsets where minimum absolute difference
between the sum of numbers is '3'. Following are the two subsets: {1, 2, 3} & {9}.
subproblem: if there is a subset with sum S in a[i-1]
            or with S S-a[i]
            dp[i, S] = dp[i-1, S] or dp[i-1, S-arr[i]] iff arr[i] <= S
"""
def solve(arr):
    sub_sum = sum(arr)//2
    # find a subset with sub_sum or closest
    sum1, sum2 = 0, 0
    dp = [[0] * (sub_sum+1) for _ in range(len(arr)+1)]
    for i in range(1, len(arr)+1):
        for j in range(1, sub_sum+1):
            if dp[i-1][j]:
                dp[i][j] = dp[i-1][j]
            else:
                if arr[i-1] <= j:
                    dp[i][j] = dp[i-1][j-arr[i-1]]

    # find a subset with sub_sum
    for i in range(sub_sum, -1, -1):
        if dp[len(arr)][i]:
            sum1 = i
            break

    sum2 = sub_sum - sum1
    return abs(sum1-sum2)


if __name__ == '__main__':
