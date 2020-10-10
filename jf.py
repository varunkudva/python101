"""
/**
 * Given an integer array, the values of the array need to be separated into two subsets A and B whose intersections is
 * null and whose union is the entire array. The sum of values in set A must be strictly greater than the sum of values
 * is set B, and the number of elements is set A must be minimal.  Return the values in set A is increasing order.
 *
 * If there are multiple sets that are possible solutions, return the set that has maximum total sum of all its
 * elements.
 *
 *
 * For example:
 *
 * Given arr = [3,7,5,6,2], the divisions with the minimal 2 elements in subset A are [5,7] and [6,7].
 * Of the two candidates, [6,7] sums to the higher amount.
 *
 */
"""
from collections import namedtuple
class Block(object):
    def __init__(self, sum, start, end):
        self.sum = sum
        self.start_idx = start
        self.end_idx = end
    def __str__(self):
        print("block sum {} start {} end {}".format(self.sum, self.start_idx, self.end_idx))

def find_subsets(arr):
    res = []
    # compute total sum
    arr_sum = sum(arr)
    a_sum = 0
    arr.sort()
    # create blocks for numbers which are identical with
    # triplets (block_sum, start_idx, end_idx)

    block_arr = [Block(arr[0], 0, 0)]
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            block_arr[-1].sum += arr[i]
            block_arr[-1].end_idx = i
        else:
            block_arr.append(Block(arr[i], i, i))

    block_arr.sort(key=lambda x: x.sum)
    #print(block_arr)

    for i in range(len(block_arr)-1, -1, -1):
        a_sum += block_arr[i].sum
        arr_sum -= block_arr[i].sum
        sidx, eidx = block_arr[i].start_idx, block_arr[i].end_idx
        res.extend(arr[sidx: eidx + 1])
        if a_sum > arr_sum:
            return res
    return None

result = find_subsets([3,7,5,6,2])
print(result)
result = find_subsets([2, 3, 2, 3, 5, 5, 7, 7])
print(result)
result = find_subsets([2, 5, 5, 7])
print(result)
result = find_subsets([5, 5, 3, 7])
print(result)
