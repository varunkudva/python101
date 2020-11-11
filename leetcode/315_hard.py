"""
315. Count of Smaller Numbers After Self
https://leetcode.com/problems/count-of-smaller-numbers-after-self/
Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
"""


class Solution(object):
    def countSmaller(self, nums)
        """
        :type nums: List[int]
        :rtype: List[int]
        9 4 5 3 2 6 0 1
        """

        def in_place_merge(left, mid, right):
            pass

        def sort_and_count(left, right):
            if left >= right:
                return

            mid = left + (right - left) // 2
            sort_and_count(left, mid)
            sort_and_count(mid + 1, right)
            i, j = left, mid + 1
            while i <= mid and j <= right:
                # nums[i] > nums[j], keep counting
                while j <=

            in_place_merge(left, mid, right)

        n = len(nums)
        res = [0] * n
        count = [(nums[i], i) for i in range(nums)]
        sort_and_count(0, len(nums) - 1)
