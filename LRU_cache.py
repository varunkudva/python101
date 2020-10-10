"""
Problem:


Approach/Solution:
# create node of double linked list storing both key and value. key for reverse lookup at delete
# define LRU cache with hashtable, double_linked_list head/tail , capacity and count

Compexity:
 Time: O(n)
 Space:

Source:
None
"""

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.hash = dict()
        self.capacity = capacity
        self.count = 0
        self.head = self.tail = None

    def enqueue(self, new_node):
        if self.head is None:
            self.head = self.tail = new_node
        else:
            # add to tail
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def dequeue(self):
        if self.head is None:
            raise ValueError("Empty list")
        else:
            node = self.head
            if self.head == self.tail:
                # single node
                self.head = self.tail = None
            else:
                self.head = self.head.next
        return node

    def move_to_tail(self, node):
        """
        # remove node and enqueue
        1. node is head
        2. node is tail
        3. node in middle

        :param node:
        :return:
        """
        if node == self.head:
            self.head = self.head.next
        elif node == self.tail:
            return
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.enqueue(node)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hash:
            node = self.hash[key]
            self.move_to_tail(node)
            return node.val
        else:
            return -1

    def set(self, key, val):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.count == self.capacity:
            # evict using LRU. least recently used is
            # at the head of list
            node = self.dequeue()
            del(self.hash[node.key])
            self.count -= 1

        new_node = Node(key, val)
        self.enqueue(new_node)
        self.hash[key] = new_node
        self.count += 1


class LRUCache_v2(object):
    """
    with dummy head tail
    """
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.hash = dict()
        self.capacity = capacity
        self.count = 0
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def enqueue(self, new_node):
        # add to tail
        old_tail = self.tail.prev
        old_tail.next = new_node
        new_node.next = self.tail
        new_node.prev = old_tail

    def dequeue(self):
        if self.head.next == self.tail:
            return -1

        node = self.head.next
        self.head.next = node.next
        return node

    def move_to_tail(self, node):
        """
        # remove node and enqueue
        1. node is head
        2. node is tail
        3. node in middle

        :param node:
        :return:
        """
        node.prev.next = node.next
        node.next.prev = node.prev
        self.enqueue(node)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hash:
            node = self.hash[key]
            self.move_to_tail(node)
            return node.val
        else:
            return -1

    def set(self, key, val):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.count == self.capacity:
            # evict using LRU. least recently used is
            # at the head of list
            node = self.dequeue()
            del(self.hash[node.key])
            self.count -= 1

        new_node = Node(key, val)
        self.enqueue(new_node)
        self.hash[key] = new_node
        self.count += 1


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
