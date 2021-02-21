"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROBLEM: Find kth smallest or kth largest element in a list

BF approach is to sort and return the element at index k
Complexity is O(nlogn)

We dont have to sort all the elements to get kth smallest.
We just need to find the position of kth element in the sorted order.
This can be done by partitioning the array and check if the partitioned
element is the kth element

for kth largest you just need to modify partitioning to reverse the
order and return kth element

NOTES:

COMPEXITY:
 Time: O(n)

SOURCE:
None
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def partition(arr, left, right, asc):
    """
    partition the array around a pivot element,
    with elements < pivot to the left of pivot
    and elements >= pivot to the right of pivot
    """
    # can randomize pivot idx
    pivot_idx = right
    pivot = arr[right]
    part_idx = left
    for i in range(left, right):
        if asc:
            # ascending order
            if arr[i] < pivot:
                # move to the left of part_idx
                swap(arr, part_idx, i)
                part_idx += 1
        else:
            if arr[i] > pivot:
                swap(arr, part_idx, i)
                part_idx += 1

    # part_idx is the new position of pivot element
    swap(arr, part_idx, pivot_idx)
    return part_idx


def quick_select(arr, left, right, k):
    p = partition(arr, left, right)
    if p == k-1:
        return arr[p]
    elif p > k-1:
        return quick_select(arr, left, p-1, k)
    else:
        return quick_select(arr, p+1, right, k)

def kth_smallest(arr, k):
    """
    This uses the quickselect algorithm to find
    smallest
    """
    left, right = 0, len(arr)-1
    while left <= right:
        p = partition(arr, left, right, True)
        if p == k-1:
            return arr[p]
        if p > k-1:
            right = p-1
        else:
            left = p+1

def kth_largest(arr, left, right, k):
    """
    This uses the quickselect algorithm to find
    smallest
    """
    while left <= right:
        p = partition(arr, left, right, False)
        if p == k-1:
            return arr[p]
        if p > k-1:
            right = p-1
        else:
            left = p+1

if __name__ == '__main__':
    arr = [4, 9, 2, 8, 6, 5, 3]
    for i in range(1, len(arr)+1):
        print("{} smallest: {}".format(i, kth_smallest(arr, 0, len(arr)-1, i)))
    for i in range(1, len(arr)+1):
        print("{} largest: {}".format(i, kth_largest(arr, 0, len(arr)-1, i)))
