"""
"""
mat = None
visited = None

def position_valid(i, j):
    if any([i < 0,
            j < 0,
            i >= m,
            j >= n,
            mat[i][j] == 'X',
            visited[i][j]
            ]):
        return False
    return True


def valid_moves(row, col):
    moves = []
    if position_valid(row+1, col):
        moves.append((row+1, col))
    if position_valid(row-1, col):
        moves.append((row-1, col))
    if position_valid(row, col-1):
        moves.append((row, col-1))
    if position_valid(row, col+1):
        moves.append((row, col+1))
    return moves

k = 0
def find_count(mat, row, col):

    global visited

    if mat[row][col] == '*':
        return True

    visited[row][col] = 1
    choice = len(valid_moves(row,col))
    if choice > 1:
        k += 1

    for i, j in valid_moves(row, col):
        if find_count(mat, i, j):
            return True

    if choice > 1:
        k -= 1
    return False


def count_luck(mat, m, n):

    global visited
    visited =[[0] * n for _ in range(m)]

    for row in range(m):
        try:
            col = mat[row].index('M')
            return find_count(mat, row, col)
        except ValueError:
            pass
    else:
        print "Start point M not found"


if __name__ == '__main__':
    mat = []
    m,n,result_k = 0,0,0
    cases = int(raw_input())

    for i in range(cases):
        m, n = tuple(map(int, raw_input().split()))
        mat =[[0] * n  for _ in range(m)]
        for row in range(m):
            mat[row] = list(raw_input())

        result_k = int(raw_input())

        k = count_luck(mat, m, n)
        if k == result_k:
            print "Impressed"
        else:
            print "Oops!"

