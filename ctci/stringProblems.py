
def reverse_string(str):
    """
    very low level reverse string API strings are immutable. So, have to
    convert to list to reverse and then form the string again.
    """
    str = list(str)
    if str:
        end = len(str) - 1
        start = 0
        while start < end:
            tmp = str[start]
            str[start] = str[end]
            str[end] = tmp
            start += 1
            end -= 1

    return ''.join(str)

if __name__ == '__main__':
    print reverse_string("invictus")
    # extended slice
    print "hollywood"[::-1]
