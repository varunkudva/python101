"""
Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both subsets is equal.

Example 1:

Input: {1, 2, 3, 4}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum: {1, 4} & {2, 3}
Example 2:

Input: {1, 1, 3, 4, 7}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum: {1, 3, 4} & {1, 7}


Time complexity:
O(nS) rows * cols
"""
def can_partition(num):
  # TODO: Write your code here
  if sum(num) % 2:
    return False

  sub_sum = sum(num)//2
  n = len(num)

  # rows for the elements of the set and columns for the sum
  dp = [[0] * (sub_sum+1) for _ in range(n+1)]

  for i in range(n+1):
    # can always make sum 0 with empty set
    dp[i][0] = 1

  # start indexing from 1 to use 0 row col for base case or
  # initial conditions. only thing to take care of is that
  # array or input indexing will have a offset of -1
  for i in range(1, n+1):
    for s in range(1, sub_sum+1):
      if num[i-1] <= s:
          dp[i][s] = dp[i-1][s] or dp[i-1][s-num[i-1]]

  return True if dp[n][sub_sum] else Fals