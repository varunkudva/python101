def mid_sum(arr):
    i, j = 0, len(arr) - 1
    lsum, rsum = 0, 0
    while i < j:
        if lsum == rsum:
            if (j - i) == 2:
                return i+1
            lsum += arr[i]
            rsum += arr[j]
            i += 1
            j -= 1
        elif lsum < rsum:
            i += 1
            lsum += arr[i]
        else:
            j -= 1
            rsum += arr[j]

    return -1

def mid_sum2(arr):
    lsum = 0
    rsum = sum(arr)
    i = 0
    for i in range(len(arr)):
        if lsum == rsum - arr[i]:
            return i
        else:
            lsum += arr[i]
            rsum -= arr[i]

    return -1

if __name__ == '__main__':
    # tests
    arr = [1, 3, 2, 4, 0]
    print "midsum for arr {} is at index: {}".format(arr, mid_sum(arr))
    print "midsum2 for arr {} is at index: {}".format(arr, mid_sum2(arr))

    arr = [1, 1, 1, 1]
    print "midsum for arr {} is at index: {}".format(arr, mid_sum(arr))
    print "midsum2 for arr {} is at index: {}".format(arr, mid_sum2(arr))

    arr = []
    print "midsum for arr {} is at index: {}".format(arr, mid_sum(arr))
    print "midsum2 for arr {} is at index: {}".format(arr, mid_sum2(arr))

    arr = [1, 2, 3, 3]
    print "midsum for arr {} is at index: {}".format(arr, mid_sum(arr))
    print "midsum2 for arr {} is at index: {}".format(arr, mid_sum2(arr))
