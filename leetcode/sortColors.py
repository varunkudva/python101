"""
Given an array with n objects colored red, white or blue, sort them so that objects of the same
color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.
"""
def swap (a, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def sort_colors(arr):
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

arr = [2, 1, 2, 0, 1, 1, 0]
sort_colors(arr)
print arr



