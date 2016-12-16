
def max_palindrome():
    n, k = map(int, raw_input().strip().split(' '))
    num = list(raw_input().strip())
    num = map(int, num)
    # result set
    res = num[:]
    # indexes of numbers to change for palindrome
    ilist = []
    # count of integers to flip to make it a palindrome
    count = 0
    for i in range(0, n):
        j = n-i-1
        if i >= j:
            break
        if num[i] != num[j]:
            count += 1
            ilist.append(i)
            if num[i] < num[j]:
                res[i] = res[j]
            else:
                res[j] = res[i]

    if count == k:
        return ''.join(str(s) for s in res)
    elif count > k:
        return -1
    else:
        # count < k. Can still flip more integers

        # special case
        if n <= k:
            for i in range(0, n):
                res[i] = 9
            return ''.join(str(s) for s in res)

        j = n
        for i in range(0, n):
            j = n-i-1
            if i > j or count == k:
                break
            if res[i] != 9:
                if i in ilist:
                    if count+1 > k:
                        break
                    else:
                        res[i] = res[j] = 9
                        count += 1
                else:
                    if count+2 > k:
                        continue
                    else:
                        res[i] = res[n-i-1] = 9
                        count += 2

        return ''.join(str(s) for s in res)

if __name__ == '__main__':
    res = max_palindrome()
    print res
