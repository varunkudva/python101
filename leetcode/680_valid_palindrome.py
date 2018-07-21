"""
Problem:
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Algorithmic Pattern:
Greedy

Approach:


Source:
https://leetcode.com/problems/valid-palindrome-ii/description/

"""
class Solution(object):
    def validPalindrome(self, s):
        def isPalindrome(i, j):
            return all(s[k] == s[j-k+i] for k in range(i,j))

        if len(s) == 0:
            return False

        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                # check if rest of the string from i+1 or j-1 forms
                # a palindrome
                return isPalindrome(i+1, j) or isPalindrome(i, j-1)
            i += 1
            j -= 1
        return True

if __name__ == '__main__':
    assert Solution().validPalindrome("aba") == True
    assert Solution().validPalindrome("abca") == True
    assert Solution().validPalindrome("a") == True
    assert Solution().validPalindrome("aa") == True
    assert Solution().validPalindrome("") == False
    assert Solution().validPalindrome("abc") == False
    assert Solution().validPalindrome("hello") == False
    print ("Test passed")
