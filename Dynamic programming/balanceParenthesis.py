"""
Given n pairs of parentheses, find all possible balanced combinations
"""
def construct(n, open, close, res=""):
    # base case and error cases
    if open < close:
        return
    if open == n and close == n:
        print res
    else:
        if open < n:
            open += 1
            res += '('
            construct(n, open, close, res)
        if close < open:
            res += ')'
            close += 1
            construct(n, open, close, res)

construct(2, 0, 0)
