"""
Maximum sum subarray (continuous)
Kadanes algorithm

"""
A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

def maxSum(A):
    min_idx, max_idx = 0,0
    max_sum = 0
    sum = 0
    for i in range(0, len(A)):
        sum += A[i]
        if sum > max_sum: max_idx = i
        max_sum = max(sum, max_sum)
        if sum < 0:
            sum = 0
            min_idx = i+1
    print min_idx, max_idx, A[min_idx:max_idx+1]



maxSum(A)
