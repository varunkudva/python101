"""
Problem:
All string related problems from CTCI


Algorithmic Pattern:
<BruteForce, Greedy, HashTable, DP, Divide and Conquer, Binary, Backtracking>

Approach/Solution:

Caveats:

Notes:

Compexity:
 Time: O(n)
 Space: O(n)

Source:
<URL>
"""
def reverse_string(str):
    """
    very low level reverse string API strings are immutable. So, have to
    convert to list to reverse and then form the string again.
    """
    str = list(str)
    if str:
        end = len(str) - 1
        start = 0
        while start < end:
            tmp = str[start]
            str[start] = str[end]
            str[end] = tmp
            start += 1
            end -= 1

    return ''.join(str)

def test_reverse_string():
    print reverse_string("invictus")
    # extended slice
    print "hollywood"[::-1]

if __name__ == '__main__':
    test_reverse_string()
