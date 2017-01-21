

def search_matrix(matrix, sol, word, N):
    for row in range(N):
        for col in range(N):
            if word_search(matrix, sol, word, row, col, 0, N):
                return True
    return False


def word_search(matrix, sol, word, row, col, idx, N):

    if row < 0 or row >= N: return False
    if col < 0  or col >= N: return False

    if idx == len(word):
        return True
    if matrix[row][col] == word[idx]:
        sol[row][col] = word[idx]

        if word_search(matrix, sol, word, row, col+1, idx+1, N) or \
                word_search(matrix, sol, word, row, col-1, idx+1, N) or \
                word_search(matrix, sol, word, row+1, col, idx+1, N) or \
                word_search(matrix, sol, word, row-1, col, idx+1, N) or \
                word_search(matrix, sol, word, row+1, col+1, idx+1, N) or \
                word_search(matrix, sol, word, row+1, col-1, idx+1, N) or \
                word_search(matrix, sol, word, row-1, col-1, idx+1, N) or \
                word_search(matrix, sol, word, row+1, col-1, idx+1, N):
            return True

        sol[row][col] = 0
        col += 1

    return False

def main():
   matrix = [['t', 'z', 'x', 'c', 'd'],
             ['a', 'h', 'n', 'z', 'x'],
             ['h', 'w', 'o', 'i', 'o'],
             ['o', 'r', 'n', 'r', 'n'],
             ['a', 'b', 'r', 'i', 'n'],
             ]
   word = 'how'

   sol = [[0] * 5 for i in range(5)]
   if search_matrix(matrix, sol, word, 5):
       for row in range(len(sol)):
           print sol[row]

main()
