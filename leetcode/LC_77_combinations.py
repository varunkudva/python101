"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROBLEM:
https://leetcode.com/problems/combinations/

APPROACH/SOLUTION:
The initial thought process is to use multiple for loops to generate
sets of numbers but that easily gets shot down as the group can vary
in size based on the input parameter k, and we cant create as many for
loops as k dynamically.

This boils down to a backtracking problem where in each iteration we choose
if the element can be added to the group

NOTES:

COMPEXITY:
 Time: O(n^k) as at each step you choose one of n elements and this continues for k elements
       This boils down to a n-array tree with depth k
 Space: Constant if considering only alphabets.
        O(k) where k is the character set count.

SOURCE:
None
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
# coding=utf-8
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def combine_bt(res, comb, idx, k, n):
            if 0 == k:
                res.append(comb[:])
            else:
                for i in range(idx, n):
                    if k > n-i:
                        break
                    val = i+1
                    comb.append(val)
                    combine_bt(res, comb, i+1, k-1, n)
                    comb.pop()
            return res

        #nums = [i for i in range(1, n + 1)]
        return combine_bt([], [], 0, k, n)




print((Solution().combine(4, 3)))
print((Solution().combine(4, 2)))
