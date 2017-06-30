"""
Problem:

Check if two strings are anagrams of each other.

Approach/Solution:

Maintain a frequency hashmap which stores the count of occurence
of characters.
Increment the count while parsing the first string.
Decrement the count while parsing second string.

check if count is 0 for all elements in the hashmap

Notes:

Compexity:

 Time: O(n)
 Space: Constant if considering only alphabets.
        O(k) where k is the character set count.

Source:
None
"""


def anagram_check(first, second):
    charmap = [0] * 256
    for c in first:
        charmap[ord(c)] += 1
    for c in second:
        charmap[ord(c)] -= 1

    if all(c == 0 for c in charmap):
        return True

    return False

if __name__ == '__main__':
    assert anagram_check("iceman", "cinema") == True
    assert anagram_check("iceman", "cinema1") == False
    assert anagram_check("iceman", "") == False
    assert anagram_check("", "") == True
