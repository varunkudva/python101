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
    begin, end = 0, 0
    count = [0] * 128   # character count map
    valid = True
    for end in range(len(s)):
        count[ord(s[end])] += 1
        if count[ord(s[end])] > 1:
            # First repeating character
            valid = False
            if end-begin >= maxlen:
                maxlen = end-begin
                sub = s[begin:end]
            while not valid:
                if s[begin] == s[end]:
                    valid = True
                begin += 1

    return maxlen, sub

print longest_non_repeating('AODEBADOBACNC')
print longest_non_repeating('AAAAAAA')


