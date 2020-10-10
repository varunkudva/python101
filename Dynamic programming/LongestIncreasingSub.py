"""
Longest Increasing Subsequence

For example, given [10, 9, 2, 5, 3, 7, 101, 18], the longest increasing
subsequence is [2, 3, 7, 101]. Therefore the length is 4.

Solution:
Let arr[0..n-1] represent the array of length n.
Let L[i] represent the longest increasing subsequence ending at arr[i]
    L[i] = max(L[j]) + 1 for  0 < j < i and arr[j] < arr[i]
    or
    L[i] = 1 if no such j < i exists
"""
def lis(arr, n):
    L = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if arr[j] < arr[i]:
                L[i] = max(L[i], L[j]+1)
    return max(L)

if __name__ == '__main__':
    arr = [9, 1, 3, 7, 5, 6, 20]
    print("LIS:", lis(arr, len(arr)))
