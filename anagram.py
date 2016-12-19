'''
 Find number of characters to be removed to make
 two strings anagrams of each other.
 NOTE:
 If ASCII character set can be assumed, we can
 use 256 byte array instead of a hash.
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
