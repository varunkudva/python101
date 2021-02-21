"""
Max heap class with following functions implemented:
1. insert(item) -> inserts item into heap
2. extract() -> returns max item from heap

Reference: algorithms robert sedgewick
           clrs heap chapter
"""
import unittest


class Heap:
    def __init__(self):
        self.heap = [None]
        self.heapsize = 0

    @staticmethod
    def _parent(i):
        return i // 2

    @staticmethod
    def _left(i):
        return 2 * i

    def __repr__(self):
        return "Heap: {} size: {}".format(self.heap, self.heapsize)

    @staticmethod
    def _right(i):
        return 2 * i + 1

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def less(self, i, j):
        return self.heap[i] < self.heap[j]

    def _swim(self, i):
        """
        Bottom up re-heapify: swim
        used when a new node is added at the bottom of a heap
        or priority of a node is increased with increase_key() api
        :param i:
        :return:
        """
        while i > 1 and self.less(self._parent(i), i):
            self._swap(i, self._parent(i))
            i = self._parent(i)

    def _sink(self, i):
        """
        Top down re-heapify: sink
        :param i:
        :return:
        """
        left = self._left(i)
        right = self._right(i)
        largest = i
        if left <= self.heapsize and self.heap[left] > self.heap[largest]:
            largest = left
        if right <= self.heapsize and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != i:
            self._swap(i, largest)
            self._sink(largest)

    @property
    def peek(self):
        return self.heap[1]

    def insert(self, item):
        self.heapsize += 1
        self.heap.append(item)
        # travel up the heap to restore order
        self._swim(self.heapsize)

    def extract(self):
        """
        :return: top element of the heap
        Swap top of heap to end of heap array to keep the complete tree variant
        reduce array size by 1
        Sink the swapped heap top to its right place in heap
        """
        if self.heapsize < 1:
            raise IndexError("No elements in heap")

        res = self.heap[1]
        self.heap[1] = self.heap[self.heapsize]
        self.heapsize -= 1
        self._sink(1)
        return res

    def heapify(self, arr):
        self.heap = arr
        self.heapsize = len(arr)
        pass

    def delete(self):
        pass

    def increase_key(self, i, new_key):
        if self.heap[i] > new_key:
            raise ValueError("Existing key already greater than new key")
        else:
            self.heap[i] = new_key
            self._swim(i)

    def decrease_key(self, i, new_key):
        pass


class TestHeapFunctions(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()

    def test_insert(self):
        heap = Heap()
        arr = [1, 2, 4, 3, 9, 8, 7, 10, 14, 15]
        for item in arr:
            heap.insert(item)
        res = []
        while self.heapsize > 1:
            res.append(heap.extract())
        self.assertEqual(arr, res[::-1])

    def test_extract(self):
        pass
