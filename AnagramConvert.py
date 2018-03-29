"""
Problem:
Find number of characters to be removed to make two strings anagrams of
each other.

Solution:
Maintain a hashmap of 256 characters.
For each character in string A, increment frequency[c].
Now go through second string B, decrement frequency.
Do absoute count of non-zero values and return.

NOTE:
If ASCII character set can be assumed, we can
use 256 byte array instead of a hash.

Compexity:
Time: O(n) Space: O(n)

Source:
hackerrank
"""

from collections import defaultdict

def convert_to_anagram(a, b):
    freq = defaultdict(int)
    count = 0
    # create hashmap with a's characters
    for c in a:
        freq[c] += 1

    # Go through characters in b. pop them
    # if the exist. Else add to hash
    for c in b:
        freq[c] -= 1

    for v in freq.values():
        count += abs(v)

    return count

if __name__ == '__main__':
    # case 1
    assert convert_to_anagram("austin", "texas") == 5
    # case 2
    assert convert_to_anagram("london", "sydney") == 8
