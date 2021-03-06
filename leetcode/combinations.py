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

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        arr = [x for x in range(1, n+1)]
        return self.combine_bt(arr, k)

    def combine_bt(self, arr, k, res=[], output=[]):
        if len(res) == k:
            output.append(res[:])
        else:
            for i in range(len(arr)):
                res.append(arr[i])
                self.combine_bt(arr[i+1:], k, res, output)
                res.pop()
        return output

if __name__ == '__main__':
    k = int(input())
    n = int(input())
    print(Solution().combine(n, k))