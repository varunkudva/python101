# coding=utf-8

# AAAABBBBCCCCCDDEEEE

def compress(s):
    res = []
    if len(s) == 1:
        return s
    start, cur = 0, 1
    res.append(s[start])
    for cur in range(len(s)):
        if s[cur] != s[start]:
            res.append(cur - start)
            start = cur
            res.append(s[start])

    res.append(cur - start)
    return ''.join(map(str, res))


print(compress('AAAABBBBCCCCCDDEEEE'))
