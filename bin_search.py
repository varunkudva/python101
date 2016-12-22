def bin_search(A, x, findfirst):
    low = 0
    high = len(A) - 1
    result = -1
    while low <= high:
        mid = (low + high) / 2
        if A[mid] == x:
            result = mid
            if findfirst:
                high = mid - 1
            else:
                low = mid + 1
        elif A[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return result


A = raw_input()
A = map(int, A.lstrip().rstrip().split(' '))
x = int(raw_input())
res = bin_search(A, x, True)

if res == -1:
    print "Not Found!"
else:
    first = res
    last = bin_search(A, x, False)
    print "First occurence:", first
    print "Last occurence:", last
    print "no. of occurences:", last - first + 1
