"""
Given an array of integers, find sub-array(s) in the array which add
to a given sum.

Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
Output: Sum found between indexes 2 and 4

Input: arr[] = {-10, 0, 2, -2, -20, 10}, sum = 20
Output: No subarray with given sum exists

NOTE: sub-arrays are contiguous. Array can have both positive and
negative integers.

Solution:
This problem can be solved differently for arrays which have negative
versus arrays which do not have negative integers

without negative integers:
Scan the array from beginning and keep a running sum.
if sum == target_sum:
    print elements from start to this index.
else:
    remove elements from start till the sum < target_sum.
continue scanning for running_sum with new start idx.

With negative integers:
Scan the elements and keep track of current sum
Store current sum and index at current_sum into hashmap.
At each iteration, check if curr_sum - target_sum is in the hashmap.
if present, it means the subarray from (curr_sum -target_sum) to curr_sum
has a sum equal to target_sum

Ref:
http://www.geeksforgeeks.org/find-subarray-with-given-sum-in-array-of-integers/

"""

def subarraySum(arr, target_sum):
    smap = dict()
    curr_sum = 0
    for i in range(len(arr)):
        curr_sum += arr[i]
        if curr_sum == target_sum:
            print(arr[0:i+1])
        else:
            off_sum = curr_sum - target_sum
            # off_sum+1 to i adds up to target_sum
            if off_sum in smap:
                print(arr[smap[off_sum]+1:i+1])
            smap[curr_sum] = i

alist = [
    [10, 2, -2, -20, 10],
    [1, 4, 20, 3, 10, 5],
    [-10, 0, 2, -2, -20, 10]
]

for arr in alist:
    #print arr
    subarraySum(arr, -10)
