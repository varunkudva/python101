"""
trie module
"""
CHARACTER_RANGE = 26
def char_index(c):
    return (ord(c) - ord('a'))

class Node():
    def __init__(self):
        self.children = [None] * CHARACTER_RANGE
        self.words = 0
        self.prefixes = 0

class Trie2(object):
    def __init__(self):
        self.root = {}

    def add_word(self, word):
        node = self.root
        for char in word:
           if node[char] is None:
               node[char] = {}
           node = node[char]
        node['*'] = None

    def find_word(self, word):
        node = self.root
        for char in word:
            if node[char]:
                node = node[char]
            else:
                return False
        # check if end of word exists
        #  in last node
        if node['*']:
            return True


class Trie():
    def __init__(self):
        # initialize trie root
        self.root = Node()

    def add_word(self, word):
        node = self.root
        for char in word:
            node.prefixes += 1
            if node.children[char_index(char)] is None:
                node.children[char_index(char)] = Node()
            node = node.children[char_index(char)]
        node.words += 1
        node.prefixes += 1

    def count_prefixes(self, word):
        node = self.root
        for char in word:
            if node.children[char_index(char)]:
                node = node.children[char_index(char)]
            else:
               return 0
        return node.prefixes

if __name__ == '__main__':
    my_trie = Trie()
    print "Enter number of operations:"
    n = int(raw_input().strip())
    while True:
        print "Enter operation(add, find, lcs,  exit):"
        op, item = raw_input().strip().split(' ')
        if op == 'add':
            my_trie.add_word(item)
        if op == 'find':
            print my_trie.count_prefixes(item)
        if op == 'exit':
            exit(0)



