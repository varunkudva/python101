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
https://leetcode.com/articles/daily-temperatures/
None
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import unittest

def temperature_diff(T):
    # returns res array with differences
    n = len(T)
    res = [0] * n
    stack = []
    for i in range(n-1, -1, -1):
        while stack and T[i] >= T[stack[-1]]:
            stack.pop()
        if stack:
            res[i] = stack[-1] - i
        stack.append(i)
    return res



class Test(unittest.TestCase):

    def test_empty(self):
        T = []
        self.assertEqual(temperature_diff(T), [])

    def test_single(self):
        T = [70]
        self.assertEqual(temperature_diff(T), [0])

    def test_one(self):
        T = [73, 74, 75, 71, 69, 72, 76, 73]
        self.assertEqual(temperature_diff(T), [1, 1, 4, 2, 1, 1, 0, 0])


if __name__ == '__main__':
    unittest.main(verbosity=3)
