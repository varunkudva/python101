n = int(raw_input())
for i in range(n):
    a = raw_input()
    b = raw_input()
    map_str = b if len(a) > len(b) else a
    check_str = a if map_str is b else b
    charmask = 0
    for c in map_str:
        charmask |= 1 << (ord(c) - ord('a'))
    for c in check_str:
        if charmask & (1 << (ord(c) - ord('a'))):
            print "YES"
            break
    else: 
        print "NO"
