"""
Problem:
 Find longest non repeating substring in a string


Approach/Solution:
hashmap and sliding window technique with [start:end) pointers

The technique uses a  hashmap and a sliding window over the string
with start and end pointers. end pointer is moved and each new character
is checked if it is already seen by hashmap lookup. If its seen, calculate
the length between start and end and update max length. Also the start
pointer is moved to an index after the last seen index of the character
which end pointer points to. This way the window slides to new set of
unique characters and new substring lengths are determined.


NOTE:
    Once a duplicate is found and the start is slides to position
    after duplicate, the seen hashmap needs to be updated with the new
    character index. hence, the same character is processed twice by keeping
    j in same position and only incrementing i

Compexity:
 Time: O(n)
 Space:


Source:
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
def longest_nrcs(s):
    i, j = 0, 0 # marks the sliding window
    n = len(s)
    seen = dict()
    sub = None
    maxlen = 0
    while i < n and j < n:
        curr_char = s[j]
        if curr_char not in seen or seen[curr_char] < i:
            seen[curr_char] = j
            j += 1
        else:
            if j-i > maxlen:
                maxlen = max(maxlen, j-i)
                sub = s[i:j]
            i = seen[curr_char]+1
    return maxlen, sub


print longest_nrcs('AODEBADOBACNC')
print longest_nrcs('AAAAAAA')


