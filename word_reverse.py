"""
Reverse characters in a string and subsequently reverse words in a sentence
"""

def str_rev(arr, s, e):
    while s != e:
        # swap characters
        tmp = arr[s]
        arr[s] = arr[e]
        arr[e] = tmp
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
    start = 0
    for idx in range(len(st)):
        if st[idx] == " " or idx+1 == len(st):
            end = idx-1
            str_rev(st, start, end)
            start = idx+1

    return ''.join(st)

print word_rev("hello world")
