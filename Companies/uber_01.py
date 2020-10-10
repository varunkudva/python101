#!/usr/bin/env python
'''
Convert a string with digits into a literal representation of the number like:
1001 to one thousand one
'''

ones_map = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}

teens_map = {
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
}

tens_map = {
    2: 'twenty',
    3: 'thirty',
    4: 'fourty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety'
}

factors = {1: 'thousand', 2: 'million', 3: 'billion'}


def convert_hundreds(num):
    # convert 10s
    res = ''
    tens = num % 100
    dig0 = num % 10
    num = num // 10
    dig1 = num % 10
    num = num // 10
    dig2 = num % 10

    if 9 < tens < 20:
        res = teens_map[tens]
    else:
        if dig0: res = ones_map[dig0]
        if dig1: res = tens_map[dig1] + " " + res

    if dig2:
        res = " ".join([ones_map[dig2], 'hundred', res])

    return res



def convert_number_to_words(num):
    res = ''
    count = 0
    factor = 0
    while num > 1000:
        factor += 1
        block = num % 1000
        print(block)
        num = num // 1000
        res = res + ' ' + factors[factor] + ' ' + convert_hundreds(block)

    if factor:
        res = ' '.join([convert_hundreds(num), factors[factor+1], res])
    else:
        res = convert_hundreds(num) + res
    return res


# print(convert_number_to_words(234))
# print(convert_number_to_words(423748))
print(convert_number_to_words(34423748))
