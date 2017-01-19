# find an element in a sorted rotated array

def search(arr, low, high, x):
    mid = (low + high) / 2
    if arr[mid] == x:
        return mid
    if arr[low] <= arr[mid]:
        # if arr[low...mid] is sorted
        if arr[low] <= x <= arr[mid]:
            return search(arr, low, mid - 1, x)
        else:
            return search(arr, mid + 1, high, x)
    else:
        # if arr[mid...high] is sorted
        if arr[mid] <= x <= arr[high]:
            return search(arr, mid + 1, high, x)
        else:
            return search(arr, low, mid - 1, x)


def find_pivot(arr, low, high):
    mid = (low + high) / 2
    if low > high: return -1

    if arr[mid - 1] > arr[mid]:
        return arr[mid]
    else:
        if arr[mid] > arr[high]:
            low = mid+1
        else:
            high = mid-1
        return find_pivot(arr, low, high)


arr = [1, 4, 5, 6, 7, 8, 9]
print "Element at index:", search(arr, 0, len(arr) - 1, 8)
print "Pivot element:", find_pivot(arr, 0, len(arr) - 1)
