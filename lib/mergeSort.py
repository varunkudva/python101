"""
Merge sort algorithm

Time: O(nlogn) worst and average
Space: O(n)
"""
def merge(arr, low, mid, high):
    """
    Copy array elements into temporary array, so that sorted elements can
    be directly merged back into original array.
    """
    temp = arr[:]
    i = low
    j = mid+1
    k = low

    while i <= mid and j <= high:
        if temp[i] < temp[j]:
            arr[k] = temp[i]
            i += 1
        else:
            arr[k] = temp[j]
            j += 1
        k += 1

    # No need to copy j -> high as its already
    # in the original array in its position
    for i in range(i, mid+1):
        arr[k] = temp[i]
        k += 1

    return arr

def sort(arr, low, high):
    if low < high:
        mid = (low + high) / 2
        sort(arr, low, mid)
        sort(arr, mid+1, high)
        merge(arr, low, mid, high)

    return arr

if __name__ == '__main__':
    arr = [4, 2, 5, 6, 3, 1]
    print(sort(arr, 0, len(arr)-1))

    arr = [1, 2, 3, 4, 5, 6]
    print(sort(arr, 0, len(arr)-1))

