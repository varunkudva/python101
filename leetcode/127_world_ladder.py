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

from __future__ import print_function

"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROBLEM:
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Algorithmic Pattern:
Greedy

Approach:
Whats a palindrome. Reads the same forwards and backwards. Which means first letter == last letter.
second == second from last. So it has even number of characters.

Source:
https://leetcode.com/problems/word-ladder/description/

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from collections import defaultdict
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        def is_similar(w1, w2):
            diff = 0
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    diff += 1
            return diff <= 1

        # build adjacency list
        sentinal = '#'
        queue = [beginWord, sentinal]
        seen = set()
        path = []
        dist = 0

        while queue:
            word = queue.pop(0)
            if word == sentinal:
                dist += 1
                queue.append(sentinal)
                continue
            for next in wordList:
                if next not in seen and is_similar(word, next):
                    if next == endWord:
                        print(dist)
                        break
                    seen.add(next)
                    queue.append(next)

        # not found



def main():
    beginWord = "hit",
    endWord = "cog",
    wordList = ["hot","dot","dog","lot","log","cog"]
    Solution().ladderLength('hit', 'cog', wordList)

if __name__ == '__main__':
    main()

