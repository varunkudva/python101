'''
Find pair of numbers whose sum adds up to a given
number [1 4 4 8] sum 8 numbers [4,4]
'''
def find_pair(arr, sum):
    comp = dict()
    for num in arr:
        numcomp = comp.get(num)
        if numcomp:
            return sorted([arr.index(num)+1, arr.index(numcomp)+1])
        # add to complement array
        comp[sum - num] = num

def find_pair_idx(arr, sum):
    comp = dict()
    for idx in range(len(arr)):
        num = arr[idx]
        numcomp = comp.get(num)
        if numcomp is not None:
            return sorted([numcomp+1, idx+1])
        # add to complement array
        comp[sum - num] = idx

tests = int(raw_input())
for i in range(tests):
    m = int(raw_input())
    n = int(raw_input())
    priceList = map(int, raw_input().split())
    print ' '.join(map(str, find_pair_idx(priceList, m)))

