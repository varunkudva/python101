class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __repr__(self):
        return "[{},{}]".format(self.start, self.end)

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res = []
        for int in sorted(intervals, key = lambda i: i.start):
            if res and int.start < res[-1].end:
                res[-1].end = max(res[-1].end, int.end)
            else:
                res += [int]
        return res

input = []
input.append(Interval(1,3))
input.append(Interval(2,6))
input.append(Interval(8,10))
input.append(Interval(15,18))
res = Solution().merge(input)
print res
