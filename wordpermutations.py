"""
Problem:
All permutations of a given string with unique characters



Approach/Solution:


Notes:

Compexity:
 Time: O(n)
 Space:


Source:
None
"""
from collections import Counter

"""
Backtracking WAY
"""
def permute_without_dup(s):
    n = len(s)
    res = [''] * n

    def permute(res, s, idx, n):
        if idx == n:
            print(''.join(res), end=' ')
        for i, char in enumerate(s):
            res[idx] = char
            cand = s[:i] + s[i + 1:]
            permute(res, cand, idx + 1, n)

    permute(res, s, 0, n)


def permute_with_dup(s):
    n = len(s)
    res = [''] * n
    char_map = Counter(s)

    # print char_counts

    def permute(res, idx, n):
        if idx == n:
            print(''.join(res), end=' ')
        for char, count in list(char_map.items()):
            if count > 0:
                char_map[char] = count - 1
                res[idx] = char
                permute(res, idx + 1, n)
                char_map[char] = count

    permute(res, 0, n)


"""
BFS WAY
"""


def permute_without_dup_bfs(s):
    res = []
    return res


def permumute_with_dup_bfs(s):
    res = []
    return res


"""
SWAP WAY
"""


def test_driver():
    print("Permute without duplicates: Input: abc")
    permute_without_dup('abcd')
    print("\n")
    print("Permute with duplicates: Input: aabc")
    permute_with_dup('aabc')


if __name__ == '__main__':
    test_driver()
