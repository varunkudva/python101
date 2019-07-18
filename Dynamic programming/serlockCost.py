"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROBLEM:


APPROACH/SOLUTION:


NOTES:

COMPEXITY:
 Time: O(n)
 Space: Constant if considering only alphabets.
        O(k) where k is the character set count.

SOURCE:
None
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

def max_cost(b, n):
    c = [0] * n
    a = [0] * n

    for i in range(1, n):
        if i == 1:
            if b[i] > b[i-1]:
                a[i], a[i-1] = b[i], 1
            else:
                a[i], a[i-1] = 1, b[i-1]
        else:
            if abs(b[i] - a[i-1]) > abs(1 - a[i-1]):
                a[i] = b[i]
            else:
                a[i] = 1
        c[i] = c[i-1] + abs(a[i] - a[i-1])

    print a
    return c[n-1]

#b = [5,8,10,9,6]
T = int(raw_input())
for i in range(T):
    n = int(raw_input())
    b = map(int, raw_input().strip().split())
    print max_cost(b, n)
