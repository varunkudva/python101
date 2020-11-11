import unittest

from dynamic_programming import knapsack01


class TestKnapsack(unittest.TestCase):
    def test_sample_1(self):
        profit = [10, 40, 30, 50]
        weight = [5, 4, 6, 3]
        capacity = 10
        expected = (90, [2, 4])
        # print(knapsack(w, v, 10))
        self.assertEqual(knapsack01.Solution().solve_knapsack(profit, weight, capacity), expected,
                         "Expected: {}".format(expected))

    def test_sample_2(self):
        weight = [2, 3, 1, 4]
        profit = [4, 5, 3, 7]
        capacity = 5
        self.assertEqual(knapsack01.Solution().solve_knapsack(profit, weight, capacity), (10, [3, 4]))
