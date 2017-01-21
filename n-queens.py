
def can_place(matrix, row, col):
    ''' if any of the previous queens is
    on the same row
    '''
    for i in range(col):
        if matrix[row][i] == 1:
            return False

    # Left upper diagonal
    for i,j in zip(range(row-1, -1, -1),range(col-1, -1, -1)):
        if matrix[i][j]: return False
    # Left lower diagonal
    for i,j in zip(range(row+1, N, 1),range(col-1, -1, -1)):
        if matrix[i][j]: return False

    return True

def place_queen(sol, queen, N):
    # if all queens placed, return True.
    if queen == N:
        return True
    for row in range(0,N):
        if can_place(sol, row, queen):
            sol[row][queen] = 1
            if place_queen(sol, queen+1, N):
                return True
            sol[row][queen] = 0


def solve(N):
    # solution matrix
    sol = [[0] * N for i in range(N)]
    if place_queen(sol, 0, N):
        for row in range(len(sol)):
            print sol[row]

N = int(raw_input())
solve(N)
