"""
Given n pairs of parentheses, find all possible balanced combinations
Solution:
"""


def add_parenthesis_2(n, left, right, idx, res):
    # base and error cases
    if left < right:
        return
    if left == n and right == n:
        print "".join(res)
    else:
        res[idx] = '('
        add_parenthesis_2(n, left+1, right, idx+1, res)

        res[idx]= ')'
        add_parenthesis_2(n, left, right+1, idx+1, res)


def add_parenthesis(left_rem, right_rem, idx, res):
    if left_rem < 0 or right_rem < left_rem:
        return

    if left_rem == 0 and right_rem == 0:
        print "".join(res)
    else:
        res[idx] = '('
        add_parenthesis(left_rem - 1, right_rem, idx + 1, res)

        res[idx] = ')'
        add_parenthesis(left_rem, right_rem - 1, idx + 1, res)


if __name__ == '__main__':
    n = 3
    res = [""] * n * 2
    #add_parenthesis(n, n, 0, res)
    add_parenthesis_2(n, 0, 0, 0, res)
