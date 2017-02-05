class Solution(object):
    def row_search(self, A, x):
        low = 0
        high = len(A) - 1
        result = -1
        while low <= high:
            mid = (low + high) / 2
            if A[mid] == x:
                 return mid
            elif A[mid] < x:
                low = mid + 1
            else:
                high = mid - 1

        return result
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        low, high = 0, m-1
        while low <= high:
            mid = (low+high)/2
            if matrix[mid][0] > target:
                high = mid - 1
            elif matrix[mid][0] <= target and matrix[mid][n-1] >= target:
                # search in this row
                if self.row_search(matrix[mid], target) >= 0:
                    return True
                else:
                    return False
            else:
                low = mid + 1

        return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
target = 3
print "True" if Solution().searchMatrix(matrix, target) else "False"

