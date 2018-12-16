"""
    ova_file = glob.glob(params.build_dir +'/vms/vmware-sensor*')
kth smallest/largest element
- use quickselect algorithm (part of quicksort)
  to choose pivot element which is at index k-1
- Can be used to find medians in unsorted arrays
  by having k = len/2.
"""
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


def quick_select(arr, left, right, k):
    if left == right:
        return arr[left]

    p = partition(arr, left, right)
    if p == k-1:
        return arr[p]
    elif p > k-1:
        return quick_select(arr, left, p-1, k)
    else:
        return quick_select(arr, p+1, right, k)


if __name__ == '__main__':
    arr = [4, 9, 2, 8, 6, 5, 3]
    print quick_select(arr, 0, len(arr)-1, 3)
    print arr
