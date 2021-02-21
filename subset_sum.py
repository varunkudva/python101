"""
Given a set of integers, the task is to divide it into two sets S1 and S2 such that the absolute difference between their sums is minimum.
If there is a set S with n elements, then if we assume Subset1 has m elements, Subset2 must have n-m elements and the value of abs(sum(Subset1) – sum(Subset2)) should be minimum.
"""
def subset_sum(nums):
    # find a subset with sum == n/2 or close to n/2
    total = sum(nums)
    target = total//2
    m = len(nums)
    # dp(i,j) => subset in nums[:i] with sum == j
    # dp(i,j) = dp(i-1, j) or dp(i-1, j-nums[i])
    dp = [[0] * (target+1) for _ in range(m+1)]
    for i in range(m):
        dp[i][0] = 1
    for i in range(1, m+1):
        for j in range(1, target+1):
            dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]

    print(dp)
    return dp[m][target]

nums = [1,2, 2, 3, 6, 7]
print(subset_sum(nums))






