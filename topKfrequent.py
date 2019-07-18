# coding=utf-8

from collections import Counter
from collections import namedtuple
import heapq

def k_frequent(input, k):
    freq_count = Counter(input)
    Node = namedtuple('Node', ('freq', 'data'))
    minh = []
    res = []
    count = 0
    for num, freq in freq_count.items():
        node = Node(freq, num)
        if count == k:
            heapq.heappushpop(minh, node)
        else:
            heapq.heappush(minh, node)
            count += 1
        print minh

    res = [heapq.heappop(minh).data for _ in range(k)]
    return res



input = [2,2,5,5,9,9,9,6,3,5]
print k_frequent(input, 1)
