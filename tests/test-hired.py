def solution(maze, n):
    # Type your solution here
    def is_valid_move(maze, r, c, n):
        if r < 0 or r >= n or c < 0 or c >= n:
            return False
        if maze[r][c] != 0:
            return False
        return True

    def path_track(maze, r, c, n):
        # end case
        if r == c == n-1:
            return True

        for neigh in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            nrow, ncol = neigh
            if is_valid_move(maze, nrow, ncol, n):
                #print(neigh)
                maze[r][c] = 2
                if path_track(maze, nrow, ncol, n):
                    return True
                maze[r][c] = 0
        return False

    return path_track(maze, 0, 0, n)

maze = [[0, 0, 1],[1, 0, 0],[1, 1, 1]]
print(solution(maze, 3))