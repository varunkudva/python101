class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        memo = [[0] * n for x in range(m+1)]
        sum = self.pathsum(grid, m-1, n-1, memo)
        print memo
        return sum

    def pathsum(self, grid, row, col, memo):
        sum = grid[row][col]
        if row == 0 and col ==0:
            return grid[0][0]
        elif memo[row][col]:
            return memo[row][col]
        elif row == 0:
            memo[row][col] = sum + self.pathsum(grid, row, col-1, memo)
        elif col == 0:
            memo[row][col] = sum + self.pathsum(grid, row-1, col, memo)
        else:
            memo[row][col] = sum + min(self.pathsum(grid, row-1, col, memo), self.pathsum(grid, row, col-1, memo))

        return memo[row][col]

grid = [[1,2,5],[3,2,1]]
print Solution().minPathSum(grid)
