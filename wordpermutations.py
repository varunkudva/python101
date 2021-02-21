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

def permute2_without_dup(s):
    """
    This is similar to previous one but uses append/pop instead
    of passing indexes
    append/pop way
    :param s:
    :return:
    """
    res, out = [], []
    n = len(s)

    def helper(s, res, n):
        if len(res) == n:
            out.append(''.join(res[:]))

        for i, c in enumerate(s):
            res.append(c)
            helper(s[:i]+s[i+1:], res, n)
            res.pop()

    helper(s, res, n)
    print(out)

def permute_with_dup(s):
    n = len(s)
    res = [''] * n
    char_map = Counter(s)

    def permute(res, idx, n):
        # keep a dictionary of the characters and iterate over
        # the dictionary for generating unique permutations
        # when duplicates are allowed
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
n = len(nums)

def permute_nums(nums):
    out = []
    res = []
    n  = len(nums)
    def helper(k, res):
        if k == len(nums):
            out.append(nums[:])
            return

        for i in range(k, len(nums)):
            nums[k], nums[i] = nums[i], nums[k]
            do_permute_v2(res, nums, k + 1, n)
            nums[k], nums[i] = nums[i], nums[k]


    helper(0, res)
    return out


def test_driver():
    print("Permute without duplicates: Input: abcd")
    permute_without_dup('abcd')
    print("\n")
    print("Permute2 without duplicates: Input: abcd")
    permute2_without_dup('abcd')
    print("\n")
    print("Permute with duplicates: Input: aabc")
    permute_with_dup('aabc')


if __name__ == '__main__':
    test_driver()