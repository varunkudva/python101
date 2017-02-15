class HashTable(object):
    def __init__(self, capacity=1000):
        self.hash = [[] for _ in range(capacity)]
        self.capacity = capacity
        self.size = 0
        self.keylist = []

    def hash_func(self, key):
        return sum([ord(c) for c in key]) % self.capacity

    def _set(self, key, val):
        hkey = self.hash_func(key)
        for item in self.hash[hkey]:
            # update value if key found
            if item[0] == key:
                item[1] = val
        else:
            self.hash[hkey].append((key, val))
            self.size += 1
            # add to keys
            self.keylist.append(key)

    def keys(self):
        return self.keylist

    def _get(self, key):
        hkey = self.hash_func(key)
        for ent in self.hash[hkey]:
            if ent[0] == key:
                return ent[1]

        return None

    def _del(self, key):
        hkey = self.hash_func(key)
        for item in self.hash[hkey]:
            if item[0] == key:
                self.hash[hkey].remove(item)
                self.keylist.remove(key)

    def __getitem__(self, item):
        return self._get(item)

    def __setitem__(self, key, value):
        self._set(key, value)

    def __delitem__(self, key):
        self._del(key)


if __name__ == '__main__':
    h = HashTable(100)
    h['a'] = 10
    h['b'] = 20
    h['c'] = 50

    del h['b']
    for key in h.keys():
        print key, h[key]

