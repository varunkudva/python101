class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        OPEN = '('
        CLOSE = ')'
        STAR = '*'
        symbols = [OPEN, CLOSE, STAR]
        counts = {OPEN: 0, CLOSE: 0, STAR: 0}
        for char in s:
            if char not in symbols:
                return False
            counts[char] += 1
            if counts[OPEN] == counts[CLOSE]:
                counts[STAR] = 0
            elif counts[CLOSE] > counts[OPEN]:
                if counts[OPEN] + counts[STAR] >= counts[CLOSE]:
                    counts[STAR] = 0
                    continue
                else:
                    return False

        if counts[OPEN] > counts[CLOSE] + counts[STAR]:
            return False
        return True


s = "(()) ( (()) ()()(*) (* ()(())()) ())()()((()())((()))(*"
print(Solution().checkValidString(s))
