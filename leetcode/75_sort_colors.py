"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROBLEM
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are
adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's,
then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?

SOLUTION:
Without sorting, the first thing that comes to mind is to shuffle 0s to the begining and 2 to the end of the list
This approach is mentioned in sort_colors_2 method. But this is still a 2 pass solution

https://leetcode.com/problems/sort-colors/description/

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
class Solution(object):
    def sortColors(self, nums):
        """
        This is a simple counting sort solution for the problem
        """
        range = max(nums) + 1
        counts = [0] * range
        for num in nums: counts[num] += 1

        idx = 0
        for i, count in enumerate(counts):
            while count > 0:
                nums[idx] = i
                idx += 1
                count -= 1

    def sort_colors_2(self, arr):
        """
        Second approach. Two pass still. Shift all zeros to beginning of the
        list in one scan. Shift all ones in second scan.
        """
        def swap(a, i, j):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

        zero_idx = 0
        for i in range(len(arr)):
            if arr[i] == 0:
                swap(arr, zero_idx, i)
                zero_idx += 1

        one_idx = zero_idx
        for i in range(one_idx, len(arr)):
            if arr[i] == 1:
                swap(arr, one_idx, i)
                one_idx += 1

    def sort_colors_one_pass(self, arr):
        """
        Two pointers
        """
        ridx, bidx = -1, len(arr)
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                ridx += 1
                arr[ridx], arr[i] = arr[i], arr[ridx]
            elif arr[i] == 2:
                bidx -= 1
                arr[bidx], arr[i] = arr[i], arr[bidx]
            elif arr[i] == 1:
                i += 1


if __name__ == '__main__':
    # solution 1
    colors = [2,0,2,1,1,0]
    Solution().sortColors(colors)
    print "sortcolors: ",colors

    # solution 2
    colors = [2,0,2,1,1,0]
    Solution().sort_colors_2(colors)
    print "sort_colors_2: ", colors

    # solution 3
    colors = [2,0,2,1,1,0]
    Solution().sort_colors_one_pass(colors)
    print "sort_colors_one_pass: ", colors