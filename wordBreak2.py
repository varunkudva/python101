class Solution(object):
    def wordBreak(self, s, wordDict, result):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if len(s) == 0:
            print result
            return True

        for i in range(1, len(s)+1):
            word = s[0:i]
            if word in wordDict:
                self.wordBreak(s[i:], wordDict, result + word + " ")

s = "catsanddog"
d = ["cat", "cats", "and", "sand", "dog"]
result = ""
Solution().wordBreak(s, d,result)
