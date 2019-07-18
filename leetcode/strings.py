# coding=utf-8

def string_to_int(string):
    """

    :param s: input number in string format
    :return: integer representation of s
    """
    res = 0
    for c in string:
        digit = ord(c) - ord('0')
        print digit
        res = res * 10 + digit

    return -res if string[0] == '-' else res


def integer_to_string(num):
    """

    :param num:
    :return:
    """
    if num < 0:
        num, is_negative = -num, True

    res = []
    while num:
        res.append(ord('0') + (num % 10))
        num //= 10
    return ('-' if is_negative else '') + ''.join(reversed(res))




if __name__ == '__main__':
    print string_to_int('-200')
