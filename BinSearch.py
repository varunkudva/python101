'''
===================================================
Problem:
 Find number of characters to be removed to make  two strings anagrams of each other.

Solution:
- Maintain a hashmap of 256 characters.
- For each character in string A, increment frequency[c].
- Now go through second string B, decrement frequency.
- Do absoute count of non-zero values and return.

NOTE:
 If ASCII character set can be assumed, we can
 use 256 byte array instead of a hash.
===================================================
'''
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
