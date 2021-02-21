"""
traditional heap sort with inbuilt python heap
"""
import heapq
import unittest

def heap_sort(arr):
    heapq.heapify(arr)
    res = []
    while len(arr):
        res.append(heapq.heappop(arr))
    return res


class TestHeap(unittest.TestCase):
    def test_empty(self):
        pass
    def test_simple(self):
        arr = [2, 4, 1, 9, 3, 6]
        expected = [1, 2, 3, 4, 6, 9]
        self.assertEqual(heap_sort(arr), expected)

if __name__ == '__main__':
    unittest.main(verbosity=3)