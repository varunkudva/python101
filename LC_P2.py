def nrcs(s):
    charmap = [-1] * 256
    start, sidx, eidx = -1, 0, 0
    lcount, longest = 0, 0
    i = 0

    while i < len(s):
        if charmap[ord(s[i])] > start:
            if lcount > longest:
                longest = lcount
                if start == -1:
                    sidx = 0
                else:
                    sidx = start
                eidx = i

            # reset
            lcount = 0
            start = charmap[ord(s[i])] + 1
            i = start
        else:
            lcount += 1
            charmap[ord(s[i])] = i
            i += 1

    if lcount > longest:
        longest = lcount
        if start == -1:
            sidx = 0
        else:
            sidx = start
        eidx = i

    return longest


if __name__ == '__main__':
    print nrcs(raw_input().strip('"'))
