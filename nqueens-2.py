"""
Problem:


Approach/Solution:


Notes:

Compexity:
 Time: O(n)
 Space:


Source:
None
"""
def can_place(res, row, col):
    for prev_row in range(row):
        prev_col = res[prev_row]
        if prev_col == col:
            # there is a queen in same column in previous
            # rows
            return False

        # check if any of the previous queens is in the
        # same diagonal as current queen, same diagonal has same slope
        # (y2-y1) == (x2 - x1) since slope is 1 in a grid diagonal
        row_dist = abs(row - prev_row)
        col_dist = abs(col - prev_col)
        if row_dist == col_dist:
            return False
    return True

def solve_queens(n):
    def helper(res, idx, n):
        if idx == n:
            out.append(res[:])

        for col in range(n):
            if can_place(res, idx, col):
                res[idx] = col
                helper(res, idx+1, n)

    out = [] # stores the different grid placement possible
    res = [0] * n
    helper(res, 0, n)
    return out

if __name__ == '__main__':
    print(solve_queens(5))