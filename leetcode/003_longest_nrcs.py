"""
Problem:
 Find longest non repeating substring in a string


Approach/Solution:
hashmap and sliding window technique with [start:end) pointers

The technique uses a  hashmap and a sliding window over the string
with start and end pointers. end pointer is moved and each new character
is checked if it is already seen by hashmap lookup. If its seen, calculate
the length between start and end and update max length. Also the start
pointer is moved to an index after the last seen index of the character
which end pointer points to. This way the window slides to new set of
unique characters and new substring lengths are determined.


NOTE:
    Once a duplicate is found and the start is slides to position
    after duplicate, the seen hashmap needs to be updated with the new
    character index. hence, the same character is processed twice by keeping
    j in same position and only incrementing i

Compexity:
 Time: O(n)
 Space:


Source:
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


def longest_nrcs(s):
    left, right = 0, 0  # marks the sliding window
    n = len(s)
    seen = dict()
    sub = None
    maxlen = 0
    while right < n:
        char = s[right]
        if char not in seen or seen[char] < left:
            seen[char] = right
            right += 1
        else:
            maxlen = max(maxlen, right - left)
            sub = s[left:right]
            left = seen[char] + 1
    return maxlen, sub


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left, right = 0, 0  # marks the sliding window
        maxlen = 0
        seen = [-1] * 256
        while right < len(s):
            char = s[right]
            cidx = ord(char)
            # print cidx
            if seen[cidx] < left:
                seen[cidx] = right
                right += 1
            else:
                maxlen = max(maxlen, right - left)
                left = seen[cidx] + 1

        maxlen = max(maxlen, right - left)
        return maxlen


print(longest_nrcs('AODEBADOBACNC'))
print(longest_nrcs('AAAAAAA'))
print(longest_nrcs('abc'))
