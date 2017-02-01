string = raw_input()
cmap = [0] * 32
numchars = 0
for c in string:
    idx = ord(c) - ord('a')
    if cmap[idx] == 0:
        numchars += 1
    cmap[idx] += 1

h = dict()
for count in cmap:
    if h.get(count):
        h[count] += 1
    else:
        h[count] = 1

for count, val in h.iteritems():
    if val == numchars or val == numchars-1:
        print "YES"
        break
else:
    print "NO"

