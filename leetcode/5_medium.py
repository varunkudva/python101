"""
https://leetcode.com/problems/longest-palindromic-substring/
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        s = "babad"
             babd b
             s e
        L(i, j) = L(i+1, j-1) + 2 if S[i] == s[j]
        """

        def is_palindrome(st, end):
            if st == end: return True
            if (st, end) in palindrome_map:
                return True
            return s[st:end] == s[st:end][::-1]

        i, j = 0, len(s) - 1
        while i < j:
            if s[i] == s[j]:
                if is_palindrome(i + 1, j):
                    return s[i:j + 1]
            elif s[i] == s[j - 1]:

            elif s[i + 1] == s[j]:
            else:
                i += 1
                j -= 1
