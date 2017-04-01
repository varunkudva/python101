'''
Problem:
Check if two strings are anagrams of each other.

Approach/Solution:

Notes:

Compexity:
 Time: O(n)
 Space: O(n)

Source:
None
'''
from collections import defaultdict

def anagram_check(first, second):
    charmap = defaultdict(int)
    for c in first:
        charmap[c] += 1
    for c in second:
        charmap[c] -= 1

    for count in charmap.itervalues():
        if count: return False

    return True

if __name__ == '__main__':
    assert anagram_check("iceman", "cinema") == True
    assert anagram_check("iceman", "cinema1") == False
    assert anagram_check("iceman", "") == False
    assert anagram_check("", "") == True
