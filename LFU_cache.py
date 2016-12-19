class LFUCache(object):
    def __init__(self, capacity):
        """

        :type capacity: int
        """
        self.hash = {}
        self.queue = []
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hash:
            self.queue[key] += 1
            print self.hash[key]
        else:
            print  -1
        print self.hash, self.queue
        if key in self.hash:
            self.queue.

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """

        if len(self.hash) == self.capacity:
            s = sorted(self.hash.keys(), key=lambda key: self.queue[key])
            print s
            del self.hash[s[0]]
            del self.queue[s[0]]
        self.queue.insert(0, key)
        self.hash
        self.queue
        self.hash[key] = value
        self.queue[key] = 0
        print self.hash, self.queue


if __name__ == '__main__':
    hash = LFUhash(2)

    hash.set(1, 1);
    hash.set(2, 2);
    hash.get(1);  # returns 1
    hash.set(3, 3);  # evicts key 2
    hash.get(2);  # returns -1 (not found)
    hash.get(3);  # returns 3.
    hash.set(4, 4);  # evicts key 1.
    hash.get(1);  # returns -1 (not found)
    hash.get(3);  # returns 3
    hash.get(4);  # returns 4
