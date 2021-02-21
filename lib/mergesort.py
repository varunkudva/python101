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
    temp = [0] * (right - left + 1)
    for k in range(left, right):
        temp[k] = arr[k]

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
    for i in range(i, mid + 1):
        arr[k] = temp[i]
        k += 1

    return arr

def merge_sort(arr):
    def merge_sort_helper(arr, left, right):
        if left < right:
            # find the division point, partition based on position
            mid = left + (right-left)//2
            merge_sort_helper(arr, left, mid)
            merge_sort_helper(arr, mid + 1, right)
            merge(arr, left, mid+1, right)

    merge_sort_helper(arr, 0, len(arr)-1)
    return arr

if __name__ == '__main__':
    arr = [4, 2, 5, 6, 3, 1]
    temp = arr[:]
    print(merge_sort(arr, temp, 0, len(arr)-1))

    arr = [1, 2, 3, 4, 5, 6]
    temp = arr[:]
    print(merge_sort(arr, temp, 0, len(arr)-1))
