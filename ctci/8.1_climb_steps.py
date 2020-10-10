"""
Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
steps at a time. Implement a method to count how many possible ways the child can run up the
stairs.
1, 2, 3 n= 5
n: 3
1, 1
2
2
"""
def count_ways_recursive(n):
    """
    no. of ways to n-1 + hop 1 step
    no. of ways to n-2 + hop 2 step
    no. of ways to n-3 + hop 3 step
    :param n:
    :return:
    """
    if n == 0:
        return 1
    if n < 0:
        return 0
    return count_ways(n-1) + count_ways(n-2) + count_ways(n-3)

def count_ways(n):
    """
    this is a DP solution where the ways array is built bottom up
    :param n:
    :return:
    """
    ways = [0] * (n+1)
    ways[0] = 1
    for i in range(1, n+1):
        if i == 1: ways[i] = ways[i-1]
        if i == 2: ways[i] = ways[i-1] + ways[i-2]
        if i >= 3:
            ways[i] = ways[i-1] + ways[i-2] + ways[i-3]
    return ways[n]

print(count_ways(1))
print (count_ways(2))
print (count_ways(10))