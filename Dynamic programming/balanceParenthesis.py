"""
Given n pairs of parentheses, find all possible balanced combinations
Solution:
"""


def add_parenthesis_2(n, left=0, right=0, res=""):
    # base and error cases
    if left < right:
        return
    if left == n and right == n:
        print res
    else:
        if left < n:
            left += 1
            res += '('
            add_parenthesis_2(n, left, right, res)
        if right < left:
            right += 1
            res += ')'
            add_parenthesis_2(n, left, right, res)


def add_parenthesis(left_rem, right_rem, res=""):
    if left_rem < 0 or right_rem < left_rem:
        return

    if left_rem == 0 and right_rem == 0:
        print res
    else:
        if left_rem:
            res += '('
            add_parenthesis(left_rem - 1, right_rem, res)

        if right_rem:
            res += ')'
            add_parenthesis(left_rem, right_rem - 1, res)


# add_parenthesis(2, 2)
add_parenthesis_2(2)
