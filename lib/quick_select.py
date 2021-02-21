"""

"""
import random

def swap(arr, left, right):
    arr[left],arr[right] = arr[right], arr[left]

def partition(arr, left, right):
    pivot_idx = random.randint(left, right)
    pivot = arr[pivot_idx]
    swap(arr, pivot_idx, right)
    part_idx = left
    for i in range(left, right):
        if arr[i] < pivot:
            swap(arr, part_idx, i)
            part_idx += 1
    swap(arr, part_idx, right)
    return part_idx


def quick_select(arr, k):
    """
    quick select the element at index k. this is the divide and conquer
    approach similar to quicksort. we divide the problem around a pivot
    element and solve subproblems. Here we only find if the pivot element
    is the kth element.

    Think from the point of a recursion manager subproblem. what do we
    need to find element at index k in a subarray. boundaries and k
    """
    def qs_helper(arr, left, right, k):
        # base case
        if left == right:
            return left

        # divide
        part_idx = partition(arr, left, right)
        if part_idx == k:
            return
        if part_idx < k:
            qs_helper(arr, part_idx + 1, right, k)
        else:
            qs_helper(arr, left, part_idx - 1, k)

    qs_helper(arr, 0, len(arr) - 1, k)
    return arr[k]

# driver code
arr = [3,2,5,7,6]
print(quick_select(arr, 2))
print(quick_select(arr, 1))
print(quick_select(arr, 0))


