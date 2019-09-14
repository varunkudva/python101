"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROBLEM:
Reverse a sentence in place.
Eg: steal pound cake => cake pound steal


APPROACH/SOLUTION:

Optimum solution is to reverse the string and then reverse
each individual words

NOTES:

COMPEXITY:
 Time: O(n)
 Space: Constant if considering only alphabets.
        O(k) where k is the character set count.

SOURCE:
None
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

def str_rev(arr, s, e):
    while s < e:
        # swap characters
        arr[s], arr[e] = arr[e], arr[s]
        s += 1
        e -= 1

def word_rev(sentence):
    """
    Reverse the whole sentence using str_rev and then reverse
    :param sentence:
    :return:
    """
    st = list(sentence)
    str_rev(st, 0, len(st)-1)
    start, idx = 0, 0

    for idx in range(len(st) + 1):
        if idx == len(st) or st[idx] == ' ':
            str_rev(st, start, idx-1)
            start = idx+1

    return ''.join(st)

print(word_rev("hello world"))
print(word_rev("shuffle list in place"))
