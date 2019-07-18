class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        visited = [[0] * n for _ in range(m)]
        islands = 0

        # print m, n, visited
        def dfs(r, c):
            if r >= m or c >= n:
                return
            if visited[r][c]: return
            visited[r][c] = 1
            if grid[r][c] == 0: return
            dfs(r + 1, c)
            dfs(r, c + 1)

        for i in range(0, m):
            for j in range(0, n):
                # print grid[i][j]
                # print visited[i][j]
                if grid[i][j] == 1 and visited[i][j] == 0:
                    islands += 1
                    dfs(i, j)

        return islands


grid = [[1, 1, 1, 1, 0],
        [1, 1, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]]

print Solution().numIslands(grid)
