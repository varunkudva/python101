"""
Twilio phonetic problem
scan through the vanity codes and get number equivalent
search for these number patterns in phone numbers
"""
import string
from collections import defaultdict
class Node(object):
    def __init__(self):
        self.child = dict()
        self.is_leaf = False
    def __str__(self):
        if self.child:
            return "child: {}, isleaf: {}".format(self.child.keys(), self.is_leaf)
        else:
            return "None"

class Trie(object):
    def __init__(self):
        self.root = Node()

    def add(self, input):
        node = self.root
        for num in input:
            if num in node.child:
                node = node.child[num]
                node.is_leaf = False
            else:
                node.child[num] = Node()
                node = node.child[num]
        node.is_leaf = True

    def lookup(self, search_num):
        node = self.root
        for num in search_num:
            #print(num, node)
            if not node or num not in node.child:
                return False
            node = node.child[num]
            if node.is_leaf:
                return True

        return False

def find_solution(numbers, vanity_codes) -> []:
    res = []
    char_to_num_dict = {}
    # build T9 char dictionary
    for c in string.ascii_lowercase:
        num = ord(c) - ord('a')
        digit = num // 3 + 2
        char_to_num_dict[c.upper()] = str(digit)

    # scan vanity codes and build number blocks
    vanity_code_nums = []
    for item in vanity_codes:
        vanity_num_str = ''
        for char in item:
            vanity_num_str += char_to_num_dict[char]
        vanity_code_nums.append(vanity_num_str)

    print(vanity_code_nums)
    code_trie = Trie()
    for code in vanity_code_nums:
        code_trie.add(code)

    for phone_num in numbers:
        for i in range(len(phone_num)):
            #print(code_trie, phone_num)
            if code_trie.lookup(phone_num[i:]):
                print(phone_num[i:])
                res.append(phone_num)

    # for code in vanity_code_nums:
    #     for phone_num in numbers:
    #         if code in phone_num:
    #             res.append(phone_num)
    #
    return res


def test_driver():
    input_nums = ["+17474824380", "+14157088956", "+919810155555", "+15109926333", "+1415123456"]
    vanity_codes = ["TWLO", "CODE", "HTCH"]
    print(find_solution(input_nums, vanity_codes))


if __name__ == '__main__':
    test_driver()
