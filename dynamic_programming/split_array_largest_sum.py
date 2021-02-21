"""
Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.


nums = [7,2,5,10,8], m = 2
Output: 18
7,2,5, 10, 8
subproblem:
 x[i:] into m-1 subarrays
guess:
where should we split the last subarray
recurrence:
dp[i,j] => denote the sum for i: split into j subarrays
dp[i,j] = minimum sum of i items with j splits
        min(dp[i-k, j-1] + sum(k:i)]
dp[n,m] original answer


Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
"""
def solve_split(arr, m)
    arr_len = len(arr)
    dp = [[0] * (m+1) for _ in range(arr_len+1)]
    psum = [0] * (arr_len+1)
    for i in range(1, arr_len+1):
        psum[i] = psum[i-1] + arr[i-1]

    for i in range(1, arr_len+1):
        for j in range(1, m+1):
            for k in range(i):
                dp[i][j] = min(dp[i][j], max(dp[k, j-1] + psum(i) - psum(k)))

    return dp[arr_len][m]


