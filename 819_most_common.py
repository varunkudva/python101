import heapq
from collections import Counter


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        maxheap = []
        word_counts = Counter([s.strip(',.') for s in paragraph.lower().split()])
        for word, freq in list(word_counts.items()):
            heapq.heappush(maxheap, (-freq, word))

        while heapq:
            word = heapq.heappop(maxheap)[1]
            if word not in banned:
                return word

        return None


print(Solution().mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
