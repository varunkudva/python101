
def can_place(matrix, row, col):
    ''' if any of the previous queens is
    on the same row
    '''
    if matrix[row] >= 0:
        return False

    # Left upper diagonal
    for i,j in zip(range(row-1, -1, -1),range(col-1, -1, -1)):
        if matrix[i] == j: return False
    # Left lower diagonal
    for i,j in zip(range(row+1, N, 1),range(col-1, -1, -1)):
        if matrix[i] == j: return False

    return True

def place_queen(sol, queen, N):
    # if all queens placed, return True.
    if queen == N:
        return True
    for row in range(0, N):
        if can_place(sol, row, queen):
            sol[row] = queen
            if place_queen(sol, queen+1, N):
                return True
            sol[row] = -1


def solve(N):
    # solution matrix
    sol = [-1] * N
    if place_queen(sol, 0, N):
            print sol

N = int(raw_input())
solve(N)
