#!/usr/bin/env python

def search_rotated(arr, target):
    def search_helper(arr, low, high):
        if low > high:
            return None
        mid = low + (high - low)//2
        if arr[mid] == target:
            return mid
        else:
            if arr[mid] <= arr[high]:
                # right is sorted
                if arr[mid] < target <= arr[high]:
                    low = mid+1
                else:
                    high = mid-1
            else:

                # left is sorted
                if arr[low] <= target < arr[mid]:
                    high = mid - 1
                else:
                    low = mid+1
        return search_helper(arr, low, high)

    return search_helper(arr, 0, len(arr)-1)


arr = [7, 9, 11, 1, 3, 5, 6]
for num in arr:
    print("Number {} at index {}".format(num,search_rotated(arr, num)))
