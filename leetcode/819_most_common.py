# coding=utf-8
import heapq
import unittest
from collections import Counter


def most_common(paragraph, banned):
    # normalize the paragraph by removing
    # special characters
    freq_heap = []
    word_count = Counter([s.strip(',.') for s in paragraph.lower().split()])
    for word, freq in word_count.items():
        heapq.heappush(freq_heap, (-freq, word))

    while freq_heap:
        word = heapq.heappop(freq_heap)[1]
        if word not in banned:
            return word

    return None


class TestMostCommon(unittest.TestCase):
    def setUp(self):
        self.input = "Bob hit a ball, the hit BALL flew far after it was hit."
        self.banned = ['hit']

    def test_valid_input(self):
        self.assertEqual(most_common(self.input, self.banned), 'ball')

    def test_banned_word_not_in_input(self):
        self.assertEqual(most_common(self.input, ['abc']), 'hit')


if __name__ == '__main__':
    unittest.main(verbosity=2)
