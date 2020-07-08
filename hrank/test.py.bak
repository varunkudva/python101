# Find all anagramatic pairs of substrings in a string.
# solution:
# Find all substrings of same length and check if they are
# anagrams. BRUTE-FORCE
#
string = raw_input()


# for i in range(len(string)+1):
#     for j in range(i, len(string)+1):
#         print string[i:j]


def anagram_check(a, b):
    chmap = [0] * 32
    for c in a:
        chmap[ord(c) - ord('a')] += 1
    for c in b:
        chmap[ord(c) - ord('a')] -= 1
    if max(chmap) == min(chmap) == 0:
        print a,b


length = len(string)
j = 0
for i in range(length):
    for slen in range(1, length):
        for j in range(i+1, length - slen + 1):
            a = string[i:i+slen]
            b = string[j:j+slen]
            print ([i,j,slen,a,b])
            anagram_check(string[i:i+slen], string[j:j+slen])


