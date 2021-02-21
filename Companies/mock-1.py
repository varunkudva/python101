"""
Given an array of numbers print it in [in,dec,in,dec] order
basically [2, 3, 1, 4, 5, 6] => [1, 2, 3, 4, 5, 6]
[1, 3, 2, 5, 4, 6]
"""
import random

def solve_1(arr):
    """
    This is a 2 pointer one pass approach
    """
    arr.sort()
    for i in range(1, len(arr)-1, 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]
    return(arr)


def partition(arr, left, right):
    # find pivot element
    pivot_idx =  random.randint(left, right)
    pivot = arr[pivot_idx]
    swap(arr, pivot_idx, right)
    part_idx = left
    for i in range(left, right):
        if arr[i] < pivot:
            swap(arr, part_idx, i)
    swap(arr, part_idx, right)

def quick_select(arr, k):
    left, right = 0, len(arr)-1

    def qs_helper(arr, left, right, k):
        # base case
        if left == right:
            return left

        part_idx = partition(arr, left, right)
        if part_idx == k:
            return arr[part_idx]
        if part_idx < k:
            qs_helper(arr, part_idx+1, right, k)
        else:
            qs_helper(arr, left, part_idx-1, k)

    helper(arr, left, len(arr)-1, k)


def solve_2(arr):
    n = len(arr)
    # find median
    x, y = 0, 0
    if n % 2:
        # arr is even
        x = quick_select(arr, n//2)
        med = x
    else:
        x = quick_select(arr, n//2)
        y = quick_select(arr, n//2-1)
        med = (x + y)//2

    for i in range(len(arr))


arr = [2,3,1,4,5,6]
print(solve_1(arr))
solve_2(arr)
