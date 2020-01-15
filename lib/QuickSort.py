def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def partition(arr, left, right):
    """
    partition the array around a pivot element,
    with elements < pivot to the left of pivot
    and elements >= pivot to the right of pivot
    """
    # can randomise pivot idx
    pivot_idx = right
    pivot = arr[pivot_idx]
    part_idx = left
    swap(arr, pivot_idx, right)
    for i in range(left, right):
        if arr[i] < pivot:
            swap(arr, i, part_idx)
            part_idx += 1
    swap(arr, part_idx, right)
    return part_idx

def qsort(arr, left, right):
    """ Quick sort algorithm """
    if left < right:
        part_idx = partition(arr, left, right)
        qsort(arr, left, part_idx-1)
        qsort(arr, part_idx+1, right)

    return arr

if __name__ == '__main__':
    arr = [4, 9, 6, 8, 5, 2, 3]
    qsort(arr, 0, len(arr)-1)
    print(arr)
