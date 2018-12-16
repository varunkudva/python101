# coding=utf-8
# coding=utf-8
"""
A peak element is an element that is greater than its neighbors.
Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5
Explanation: Your function can return either index number 1 where the peak element is 2,
             or index number 5 where the peak element is 6.
"""


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # brute force compare neighboring elements
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                return i-1
        return len(nums)-1
        # binary log n implementation

    def findPeakElement_2(self, nums):
        """
        mid element is either the peak element
        or it can be on the rising or falling
        edge
        """
        low, high = 0, len(nums)-1
        while low < high:
            mid = (low+high)/2
            if nums[mid] < nums[mid+1]:
                #rising edge, peak to the right
                low=mid+1
            else:
                high = mid
                #rising edge, peak to the right
                low=mid+1

nums = [1,2]
print Solution().findPeakElement(nums)
print Solution().findPeakElement_2(nums)
