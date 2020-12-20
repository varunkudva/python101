"""
Merge sort algorithm

Time: O(nlogn) worst and average
Space: O(n)
"""
def merge(arr, left, mid, right):
    """
    Copy array elements into temporary array, so that sorted elements can
    be directly merged back into original array.
    """
    temp = arr[:]
    i = left
    j = mid + 1
    k = left

    while i <= mid and j <= right:
        if temp[i] < temp[j]:
            arr[k] = temp[i]
            i += 1
        else:
            arr[k] = temp[j]
            j += 1
        k += 1

    # No need to copy j -> right as its already
    # in the original array in its position
    for i in range(i, mid+1):
        arr[k] = temp[i]
        k += 1

    return arr


def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        # merge
        merge(arr, left, mid, right)

    return arr

if __name__ == '__main__':
    arr = [4, 2, 5, 6, 3, 1]
    print(sort(arr, 0, len(arr)-1))

    arr = [1, 2, 3, 4, 5, 6]
    print(sort(arr, 0, len(arr)-1))

