# coding=utf-8


def four_sum(arr, k, sum, res):
    if k == 0:
        if sum == 0:
            return res, true
        else:
            return None, false

    for i in range(len(arr)):
        if arr[i] <= sum:
            res.append(arr[i])
            res, four_sum(arr, k - 1, arr[:i] + arr[i + 1:], sum - arr[i])
