"""
Problem:


Approach/Solution:


Notes:

Compexity:
 Time: O(n)
 Space:


Source:
None
"""


class Solution(object):
    def readBinaryWatch(self, num, result=None):
        """
        :type num: int
        :rtype: List[str]
        """
        for h in range(0, 12):
            for m in range(0, 60):
                if self.num_bits_set(h, m) == num:
                    result.append["{}:{:.2}".format(h, m)]
        return result

    def num_bits_set(self, h, m):
        return bin(h).count('1') + bin(m).count('1')


class Solution2(object):
    def combinationSum(self, candidates, target, res=[], output=[]):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if target == 0:
            output.append(res[:])
            return output
        # if target < 0:
        #     return output

        for num in candidates:
            if num <= target:
                res.append(num)
                self.combinationSum(candidates, target-num, res, output)
                res.pop()

        return output

print Solution2().combinationSum([2,3,6,7], 7)