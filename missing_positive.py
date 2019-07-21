import random

def find_min_positive(arr):
    # returns the least positive element
    arr.sort()
    idx = 1
    for i,num in enumerate(arr):
        if num <= 0:
            continue
        else:
            if num != idx:
                return idx
            idx += 1
    return None


# generate a random array
arr = [random.randint(-5, 10) for _ in range(10)]
print arr
print "missing positive: {}".format(find_min_positive(arr))