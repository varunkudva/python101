"""
Given a cost matrix cost[][] and a position (m, n) in cost[][], write a function
that returns cost of minimum cost path to reach (m, n) from (0, 0). Each cell of
the matrix represents a cost to traverse through that cell. Total cost of a path
to reach (m, n) is sum of all the costs on that path (including both source and
destination). You can only traverse down, right and diagonally lower cells from
a given cell, i.e., from a given cell (i, j), cells (i+1, j), (i, j+1) and
(i+1, j+1) can be traversed. You may assume that all costs are positive integers.
"""
import sys
class Solution(object):

    def min_cost_path_recursion(self, grid):
        """ Traditional recursive way """
        def min_path_sum(grid, i, j):
            if i < 0 or j < 0:
                return sys.maxsize
            elif i == 0 and j == 0:
                return grid[0][0]
            else:
                return grid[i][j] + min(min_path_sum(grid, i-1, j),
                                        min_path_sum(grid, i, j-1),
                                        min_path_sum(grid, i-1, j-1))
        m = len(grid)
        n = len(grid[0])
        return min_path_sum(grid, m-1, n-1)

    def min_cost_path_memoized(self, grid):
        """
        Recursive with memoization
        """
        def pathsum(grid, i, j):
            """ Recursive approach with memoization
            """
            if cost[i][j] > 0:
                return cost[i][j]
            else:
                if i == 0 and j == 0:
                    cost[i][j] = grid[0][0]
                elif i == 0:
                    cost[i][j] = grid[i][j] + pathsum(grid, i, j-1)
                elif j == 0:
                    cost[i][j] = grid[i][j] + pathsum(grid, i-1, j)
                else:
                    cost[i][j] = grid[i][j] + min(pathsum(grid, i-1, j),
                                                  pathsum(grid, i, j-1),
                                                  pathsum(grid, i-1, j-1))
            return cost[i][j]

        m = len(grid)
        n = len(grid[0])
        cost = [[-1] * n for _ in range(m)]
        s = pathsum(grid, m-1, n-1)
        # print cost
        return s

    def min_cost_path_dynamic(self, grid):
        """
        Bottom up iterative dynamic programming approach
        Following recursive function to get value of optimal solution
        c(i,j) =  cost(0,0) for i,j = 0,0
                  min[c(i-1, j), c(i, j-1), c[i-1, j-1) for 0 < i,j < m,n
        """
        def print_min_cost_path(cost, i, j):
            if i < 0 or j < 0:
                return
            if i > 0 and cost[i][j] == cost[i-1][j] + grid[i][j]:
                print_min_cost_path(cost, i-1, j)
                print "D",
            elif j > 0 and cost[i][j] == cost[i][j-1] + grid[i][j]:
                print_min_cost_path(cost, i, j-1)
                print "R",
            elif i > 0 and j > 0 and cost[i][j] == cost[i-1][j-1] + grid[i][j]:
                print_min_cost_path(cost, i-1, j-1)
                print "C",
            print grid[i][j],

        m = len(grid)
        n = len(grid[0])
        cost = [[0] * n for x in range(m)]

        # initialize first row and column cost
        cost[0][0] = grid[0][0]
        for i in range(1, n):
            cost[i][0] = cost[i-1][0] + grid[i][0]
        for j in range(1, m):
            cost[0][j] = cost[0][j-1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                cost[i][j] = min(cost[i-1][j], cost[i][j-1], cost[i-1][j-1]) + grid[i][j]

        #print cost
        print_min_cost_path(cost, m-1, n-1)
        print
        return cost[m-1][n-1]


if __name__ == '__main__':
    # Driver program
    grid = [[1,2,3],
            [4,8,2],
            [1,5,3]]

    print "Recursive -> Min Cost: {}".format(Solution().min_cost_path_recursion(grid))
    print "Memoization -> Min Cost: {}".format(Solution().min_cost_path_memoized(grid))
    print "DP -> Min Cost: {}".format(Solution().min_cost_path_dynamic(grid))
