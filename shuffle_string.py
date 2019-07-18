# coding=utf-8

import random
from collections import Counter
import math

def shuffle_str(input_str):
    input = list(input_str)
    input_len = len(input)

    for i in range(0, input_len):
        random_idx = random.randint(i, input_len-1)
        input[i], input[random_idx] = input[random_idx], input[i]

    return ''.join(input)

def test_random(input):
    input_counts = Counter(input)
    output = shuffle_str(input)
    output_counts = Counter(output)
    print "input: {} output {} diff {}".format(input, output, input_counts - output_counts)

# test_random("Monday")
# test_random("yosemite")
def test_outcomes(input):
    n = len(input)
    total_outputs = math.factorial(n)
    output = []
    for i in range(total_outputs):
        output.append(shuffle_str(input))
    print total_outputs, len(set(output)), output

test_outcomes("abc")
