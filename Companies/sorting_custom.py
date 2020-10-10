

from collections import Counter
from functools import cmp_to_key


def solution(arr):
    counts = Counter(arr)
    def compare(this, other):
        if counts[this] < counts[other]:
            return -1
        if counts[this] > counts[other]:
            return 1
        return this - other
    return sorted(arr, key=cmp_to_key(compare))


arr = [8,5,5,5,5,1,1,1,4,4]
print(solution(arr))
