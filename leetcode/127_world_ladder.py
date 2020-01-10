"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROBLEM:

Algorithmic Pattern:
Graph + BFS

Approach:

Source:
https://leetcode.com/problems/word-ladder/description/

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""


import string
from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        def is_similar(w1, w2):
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    diff += 1
            return diff <= 1

        sentinal = '#'
        queue = deque([beginWord, sentinal])
        seen = set()
        dist=1
        if endWord not in wordList:
            return 0

        while queue:
            word = queue.popleft()
            seen.add(word)
            if word == sentinal:
                dist += 1
                if queue:
                    queue.append(sentinal)
                    continue
            if word == endWord:
                return dist
                break

            # create similar words by replacing one character
            # at a time and look for them in wordList. If found,
            # append them to the queue for BFS
            for c in string.ascii_lowercase:
                for i in range(len(word)):
                    simWord = word[:i] + c + word[i+1:]
                    if simWord not in seen and simWord in wordList:
                        seen.add(simWord)
                        queue.append(simWord)
        return 0


if __name__ == '__main__':
    beginWord, endWord = "hit", "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]

    print(Solution().ladderLength(beginWord, endWord, wordList))
