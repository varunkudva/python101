# coding=utf-8
"""
given a a list of sorted integers, every number comes as a pair (2 times) except for one.
Write a function that returns the number that didn't have a pair
"""


class CountHelper(object):
    def __init__(self, input):
        self.count_odd_with_set(input)
        self.count_odd_with_xor(input)
        pass

    def count_odd(self, num_list):
        singleton = set()
        for num in num_list:
            if num in singleton:
                singleton.remove(num)
            else:
                singleton.add(num)

        return singleton

    def


print(count_odd([2, 2, 5, 5, 101, 101, 305, 600, 600]))
