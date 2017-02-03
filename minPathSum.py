class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m =  len(grid)
        n = len(grid[0])
        for row in range(0, m):
            for col in range(0, n):
                if row == 0 and col != 0:
                    grid[0][col] += grid[0][col-1]
                elif col == 0  and row != 0:
                    grid[row][0] += grid[row-1][0]
                elif row != 0 and col !=0:
                    grid[row][col] += min(grid[row-1] [col], grid[row][col-1])
        return grid[m-1][n-1]


print Solution().minPathSum([[1,2],[1,1]])