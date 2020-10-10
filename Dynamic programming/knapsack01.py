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

    for i in range(items + 1):
        print(val[i])

    print("Items picked: ", print_items(items, weight))
    return val[items][weight]


if __name__ == '__main__':
    v = [10, 40, 30, 50]
    w = [5, 4, 6, 3]
    print(knapsack(w, v, 10))
