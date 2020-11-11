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

    1 + max(L[j] where arr[i] <= arr[j] for j = i+1, n)
"""


def lis_recursive(arr, i):
    """
    lis(i) = max(lis(i-1), lis(i-j) for j < i and arr[j] < arr[i])
    :param arr:
    :param n:
    :return:
    """
    if i == 0:
        return 1
    lis_without_i = lis_recursive(arr, i - 1)
    lis_with_i = 1
    for j in range(0, i):
        if arr[j] < arr[i]:
            lis_with_i = max(lis_recursive(arr, j) + 1, lis_with_i)
    return max(lis_without_i, lis_with_i)


def lis_v2(arr, n):
    L = [1] * n
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] > arr[i]


def lis(arr, n):
    L = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if arr[j] < arr[i]:
                L[i] = max(L[i], L[j] + 1)
    return max(L)


def solve(arr):
    print("LIS recursive: {}".format(lis_recursive(arr, len(arr) - 1)))
    print("LIS:", lis(arr, len(arr)))


if __name__ == '__main__':
    arr = [9, 1, 3, 7, 5, 6, 20]
    solve(arr)
    arr2 = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    solve(arr2)
