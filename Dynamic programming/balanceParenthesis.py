"""
Given n pairs of parentheses, find all possible balanced combinations
Solution:
1. Start with clean slate and add left parenthesis.
2. Add right parenthesis only if there are more left parenthesis than right.
3. Stop if left count == n or right count > left count.
"""


def add_parenthesis(n, left, right, idx, res):
    # base and error cases
    if left > n or right > left:
        return

    if left == n and right == n:
        print "".join(res)
    else:
        res[idx] = '('
        add_parenthesis(n, left+1, right, idx+1, res)

        res[idx]= ')'
        add_parenthesis(n, left, right+1, idx+1, res)


if __name__ == '__main__':
    n = 3
    res = [""] * n * 2
    add_parenthesis(n, 0, 0, 0, res)
