"""
Problem:


Approach/Solution:


Notes:

Compexity:
 Time: O(n)
 Space:


Source:
None
"""
from lib.linklist import Dll

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.hash = dict()
        self.queue = Dll()
        self.capacity = capacity
        self.count = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hash:
            node = self.hash[key]
            self.queue.requeue(node)
            return node.val
        else:
            return -1

        print self.hash, self.queue

    def put(self, key, val):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.count == self.capacity:
            # evict using LRU


        self.hash[key] = self.queue.enqueue(val)
        self.count += 1

        print self.hash, self.queue


if __name__ == '__main__':
    cache = LRUCache(2)

    cache.set(1, 1)
    cache.set(2, 2)
    cache.get(1)     # returns 1
    cache.set(3, 3)  # evicts key 2
    cache.get(2);  # returns -1 (not found)
    cache.get(3);  # returns 3.
    cache.set(4, 4);  # evicts key 1.
    cache.get(1);  # returns -1 (not found)
    cache.get(3);  # returns 3
    cache.get(4);  # returns 4
