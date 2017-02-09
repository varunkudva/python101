"""
kth largest element
"""
def swap(arr, i, j):

    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def partition(arr, left, right):
    pivot_idx = left + (right - left)/2
    pivot = arr[pivot_idx]
    part_idx = 0
    swap(arr, pivot_idx, right)
    for i in range(left, right):
        if arr[i] < pivot:
            swap(arr, i, part_idx)
            part_idx += 1
    swap(arr, part_idx, right)
    return part_idx


def quick_select(arr, left, right, k):
    p = partition(arr, left, right)
    if p-left == k-1:
        return arr[p]
    elif p-left > k-1:
        return quick_select(arr, left, p-1, k)
    else:
        return quick_select(arr, p+1, right, k-p+1)


arr = [4, 9, 2, 8, 6, 5, 3]
print quick_select(arr, 0, len(arr)-1, 3)
