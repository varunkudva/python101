"""
Merge sort implementation

Space complexity: O(n) for the extra placeholder array for merge

Time complexity: O(nlogn) (average, worst case)
"""
def merge_sort(arr, low, high):
    while low < high:
        mid = (low + high)/2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid+1, high)
        merge(arr, low, mid, high)


def merge(arr, low, mid, high):
    """
    Copy array elements into placeholder array.
    Scan elements in placeholder array and merge them into original array.
    """
    temp = arr[:]

