'''
===================================================
Problem:
 Find longest non repeating sequence in a string

Solution:
- hashmap and 2 pointer technique

NOTE:
 If ASCII character set can be assumed, we can
 use 256 byte array instead of a hash.
===================================================
'''
def longest_non_repeating(s):
    maxlen = 0
    begin, end, counter = 0, 0, 0
    map = [0] * 128   # character map map
    for end in range(len(s)):
        map[ord(s[end])] += 1
        if map[ord(s[end])] > 1:
            # First repeating character
            counter += 1
            valid = False
            if end-begin >= maxlen:
                maxlen = end-begin
                sub = s[begin:end]
            while not valid:
                if s[begin] == s[end]:
                    valid = True
                else:
                    # reset entries in the map
                    map[ord(s[begin])] = 0
                begin += 1

    return maxlen, sub

print longest_non_repeating('AODEBADOBACNC')
print longest_non_repeating('AAAAAAA')


