""""""""""""""""""""""
Quicksort library
"""""""""""""""""""""


def swap(arr, left, right):
    arr[left], arr[right] = arr[right], arr[left]

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

def qs_helper(arr, left, right):
    """ Quick sort algorithm """
    # base case
    if left >= right:
        return

    # divide
    part_idx = partition(arr, left, right)
    qs_helper(arr, left, part_idx - 1)
    qs_helper(arr, part_idx + 1, right)

    # conquer

def quicksort(arr):
    # base case
    qs_helper(arr, 0, len(arr)-1)

if __name__ == '__main__':
    arr = [4, 9, 6, 8, 5, 2, 3]
    quicksort(arr)
    print(arr)