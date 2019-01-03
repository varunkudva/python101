#!/usr/bin/env python
# Convert a string with digits into a literal representation of the number like:
1001 to one thousand one

digit_map = {
    0: '', 1: 'one', 2: 'two', 3:'three',
    4:'four', 5:'five', 6:'six',
    7: 'seven', 8: 'eight', 9: 'nine'
}

teens_map = {
    10: 'ten', 11: 'eleven', 12: 'twelve',
    13: 'thirteen', 14: 'fourteen',
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

factors = {2: 'hundred', 3: 'thousand', 6: 'million', 9: 'billion'}


def convert_hundreds(num):
    if num < 1000:
        # convert 10s
        tens = num % 100
        dig2= num / 100
        dig1 = tens / 10
        dig0 = tens % 10

        if 9 < tens < 20:
            res.insert(0, teens_map[tens])
        else:
            if dig0: res.insert(0, digit_map[dig0])
            if dig1: res.insert(0, tens_map[dig1])
            if dig2:
                res.insert(0, 'hundred')
                res.insert(0, digit_map[dig2])

    return ' '.join(res)
    pass

def convert_number_to_words(num):
    res = []
    count = 0
    if num > 1000:
        while num > 1000:
            factor += 1
            num /= 1000
            convert_hundreds(num)



print convert_number_to_words(423748)
