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

# Enter your code here. Read input from STDIN. Print output to STDOUT
N, M = map(int, raw_input().strip().split(' '))
nlist = (0 for i in range(N+1))
max = 0
for i in range(M):
    a, b, k = map(int, raw_input().strip().split(' '))
    for idx in range(a, b+1):
        nlist[idx] += k
        if nlist[idx] > max:
            max = nlist[idx]
print max
