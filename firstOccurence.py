"""
Problem:
Given a sorted list, find first and last occurence of a number in the list

Approach/Solution:
Binary search finds the index of an element in the sorted list. One finding
an occurance of the element, store the element idx and keep searching left
or right based on first or last occurance that needs to be found.

If no more instances of element exist, result will have the index of last
found index

Notes:

Compexity:
 Time: O(logn)
 Space: NA


Source:
None
"""
def bin_search(A, x, findfirst):
    low = 0
    high = len(A) - 1
    result = -1
    while low <= high:
        mid = (low + high) / 2
        if A[mid] == x:
            result = mid
            if findfirst:
                high = mid - 1
            else:
                low = mid + 1
        elif A[mid] < x:
           low = mid + 1
        else:
            high = mid - 1

    return result


def search(arr, num):
    # find first
    first = bin_search(arr, num, True)
    if first == -1:
        print "{} Not Found!".format(num)
    else:
        # find last
        last = bin_search(arr, num, False)
        print "First occurence of {}: {}".format(num, first)
        print "Last occurence of {}: {}".format(num, last)
        print "no. of occurences:", last - first + 1

if __name__ == '__main__':
    arr = [4, 5, 5, 5, 7, 9, 11, 22, 22, 29]
    search(arr, 5)
    search(arr, 1)
    search(arr, 11)
