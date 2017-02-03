
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            #print '1'
            return '1'
        else:
            num = self.countAndSay(n-1)
            count = 1
            seq = ''
            i = 0
            for i in range(0, len(num)-1):
                if num[i] == num[i+1]:
                    count += 1
                else:
                    seq += str(count) + str(num[i])
                    count = 1
            seq += str(count) + str(num[len(num)-1])
            #print seq
            return seq

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        res = [''] * numRows
        idx = 0
        while True:
            for i in range(0, numRows):
                if idx >= len(s): break
                res[i] += s[idx]
                idx += 1
            for i in range(numRows-2, 0, -1):
                if idx >= len(s): break
                res[i] += s[idx]
                idx += 1
            if idx >= len(s): break
        zigzag = ''.join(res)
        return zigzag



s = raw_input()
numRows = int(raw_input())
print Solution().convert(s, numRows)

# n = int(raw_input())
# print Solution().countAndSay(n)