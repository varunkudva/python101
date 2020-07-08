# coding=utf-8

import unittest


def shuffle_odd_even(arr):
    """
    Shuffle even elements to the beginning of the array in one pass, in place
    :param arr: input array
    :return: modified array with shuffled elements
    """
    i, next_even = 0, 0
    for i, num in enumerate(arr):
        if num % 2 == 0:
            arr[next_even], arr[i] = arr[i], arr[next_even]
            next_even += 1


def shuffle_2_pointer(arr):


if __name__ == '__main__':
    arr = [5, 2, 9, 7, 3, 6]
    shuffle_odd_even(arr)
    print(arr)
    unittest.main()
