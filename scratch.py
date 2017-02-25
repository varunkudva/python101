
def min_deletes(n, arr):
    hmap = {}
    max = 1
    for val in arr:
        if val in hmap:
            hmap[val] += 1
            if hmap[val] > max:
                max = hmap[val]
        else:
            hmap[val] = 1
    print n - max



n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
min_deletes(n, arr)


