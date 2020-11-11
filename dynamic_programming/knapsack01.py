"""
Knapsack 0-1 problem:

Give a list of items with weights {w1, w2 .... wn} and values
{v1, v2,....vn}, find subset of items with maximum value given
total weight <= W.

DP Solution:

Let A[i,j] be the maximum value for first i items with a weight
of upto j pounds. The recurrence relation for subproblem
can be defined as,

    A[i,j] = A[i-1,j] if wi > j, item i not included

             max{A[i-1,j], A[i-1, j-wi] + vi} if wi <= j
"""
import unittest


def knapsack(w, v, weight):
    def print_items(i, j):
        if i <= 0 or j <= 0:
            return
        if val[i][j] == 0:
            return
        if val[i][j] == val[i - 1][j]:
            # ith item wasn't picked
            print_items(i - 1, j)
        else:
            print_items(i - 1, j - w[i - 1])
            print(i - 1, end=' ')

    items = len(v)
    val = [[0] * (weight + 1) for _ in range(items + 1)]

    for i in range(1, items + 1):
        for j in range(1, weight + 1):
            if w[i - 1] > j:
                val[i][j] = val[i - 1][j]
            else:
                val[i][j] = max(val[i - 1][j], val[i - 1][j - w[i - 1]] + v[i - 1])

    # for i in range(items + 1):
    #     print(val[i])

    print("Items picked: {}".format(print_items(items, weight)))
    return val[items][weight]


class Solution:
    def list_items(self, res, dp, item, capacity, weight):
        if item <= 0 or capacity <= 0:
            return
        if dp[item][capacity] == dp[item - 1][capacity]:
            # this item was not picked
            self.list_items(res, dp, item - 1, capacity, weight)
        else:
            self.list_items(res, dp, item - 1, capacity - weight[item - 1], weight)
            res.append(item)
        return res

    def solve_knapsack(self, profit, weight, capacity):
        """
        max profit with i items and capacity c
        M(i, c) = max(M(i-1,c), M(i-1, c-weight[i] + profit[i])
        time: O(m*n)
        space: O(m*n)
        """
        res = []
        items = len(profit)
        dp = [[0] * (capacity + 1) for _ in range(len(profit) + 1)]
        # skip capacity of 0
        for c in range(1, capacity + 1):
            for i in range(1, items + 1):
                if weight[i - 1] > c:
                    dp[i][c] = dp[i - 1][c]
                else:
                    dp[i][c] = max(dp[i - 1][c], profit[i - 1] + dp[i - 1][c - weight[i - 1]])

        return dp[items][capacity], self.list_items(res, dp, items, capacity, weight)


class TestKnapsack(unittest.TestCase):
    def test_sample_1(self):
        profit = [10, 40, 30, 50]
        weight = [5, 4, 6, 3]
        capacity = 10
        expected = (90, [2, 4])
        # print(knapsack(w, v, 10))
        self.assertEqual(Solution().solve_knapsack(profit, weight, capacity), expected, "Expected: {}".format(expected))

    def test_sample_2(self):
        weight = [2, 3, 1, 4]
        profit = [4, 5, 3, 7]
        capacity = 5
        self.assertEqual(Solution().solve_knapsack(profit, weight, capacity), (10, [3, 4]))


if __name__ == '__main__':
    unittest.main(verbosity=3)
