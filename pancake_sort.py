"""
 Given an array
a. Write a method which flips the first k elements of the array. k is a parameter passed to the method
b. Write a method which sorts an input array using only the flip method for any modifications of the array
need for sorting.
"""


# arr [5, 4, 9, 3, 6, 2]
def flip(arr, k):
    if not arr or len(arr) < k:
        return arr
    i, j = 0, k - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr


def pancake_sort(arr):
    # ridx partitions the arr into unsorted in left and sorted in right
    ridx = len(arr) - 1
    while ridx > 0:
        # find maximum element in the left
        # flip max to top
        # flip to the right_idx
        max_idx = 0
        for j in range(0, ridx + 1):
            max_idx = j if arr[j] > arr[max_idx] else max_idx

        flip(arr, max_idx + 1)
        flip(arr, ridx + 1)
        ridx -= 1


arr = [5, 4, 9, 3, 6, 2]
pancake_sort(arr)
print
arr
