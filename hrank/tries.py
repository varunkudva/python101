class tnode():
    def __init__(self):
        self.children = {}
        self.words = 0
        self.prefixes = 0


class Trie():
    def __init__(self):
        # initialize trie root
        self.root = tnode()

    def add_word(self, word):
        node = self.root
        for char in word:
            node.prefixes += 1
            if char not in node.children:
                node.children[char] = tnode()
            node = node.children[char]
        node.words += 1
        node.prefixes += 1

    def count_prefixes(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
               return 0
        return node.prefixes

    # def count_words2(self, node, word):
    #     if not word:
    #         return node.words
    #     index = ord(word[0]) - ord('a')
    #     if node.children[index] is None:
    #         return 0
    #     else:
    #         return self.count_words2(node.children[index], word[1:])
    #
    # def add_word2(self):
    #     if not word:
    #         node.words += 1
    #     else:
    #         node.prefixes += 1
    #         index = ord(word[0]) - ord('a')
    #         if node.children[index] is None:
    #             node.children[index].appendtnode()
    #         self.add_word(node.children[index], word[1:])
    #
    # def count_prefixes2(self, node, word):
    #     if not word:
    #         return node.prefixes
    #
    #     index = ord(word[0]) - ord('a')
    #     if node.children[index] is None:
    #         return 0
    #     else:
    #         return self.count_prefixes2(node.children[index], word[1:])
    #
    # def count_words2(self, node, word):
    #     if not word:
    #         return node.words
    #     index = ord(word[0]) - ord('a')
    #     if node.children[index] is None:
    #         return 0
    #     else:
    #         return self.count_words2(node.children[index], word[1:])


def main():
    my_trie = Trie()
    n = int(raw_input().strip())
    for a0 in xrange(n):
        op, contact = raw_input().strip().split(' ')
        if op == 'add':
            my_trie.add_word(contact)
        if op == 'find':
            print my_trie.count_prefixes(contact)


if __name__ == '__main__':
    main()
