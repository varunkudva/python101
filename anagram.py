'''
===================================================
Problem:
 Find number of characters to be removed to make  two strings anagrams of each other.
 
Solution:
- Maintain a hashmap of 256 characters.
- For each character in string A, increment frequency[c].
- Now go through second string B, decrement frequency.
- Do absoute count of non-zero values and return.

NOTE:
 If ASCII character set can be assumed, we can
 use 256 byte array instead of a hash.
===================================================
'''

def number_needed(a, b):
    freq = dict()
    count = 0
    # create hashmap with a's characters
    for c in a:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1

    # Go through characters in b. pop them
    # if the exist. Else add to hash
    for c in b:
        if c in freq:
            freq[c] -= 1
        else:
            freq[c] = -1

    for v in freq.values():
        count += abs(v)

    return count


a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)
