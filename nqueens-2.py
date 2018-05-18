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


# this is the safety condition function.
def can_place(matrix, row, col):
    ''' if any of the previous queens is
    on the same row
    '''
    for i in range(0, row):
        if matrix[i] == col or matrix[i] == col - row + i or matrix[i] == col + row - i:
            return False
    return True

# each queen denotes index of a particular row
def place_queen(sol, queen, N):
    # if all queens placed, return True.
    if queen == N:
        print sol
        return True
    else:
        for col in range(0, N):
            if can_place(sol, queen, col):
                sol[queen] = col
                if place_queen(sol, queen+1, N):
                    return True
                sol[queen] = -1


N = int(raw_input())
# solution matrix
sol = [-1] * N
place_queen(sol, 0, N)
