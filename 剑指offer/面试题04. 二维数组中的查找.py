class Solution:
    def findNumberIn2DArray(self, matrix, target):
        """
        time: O(M + N)
        space: O(1)

        Args:
            matrix: list[list[int]]
            target: int
        
        Return: bool
        """
        if not matrix:
            return False
            
        n = len(matrix)
        m = len(matrix[0])

        i = 0
        j = m - 1

        while i < n and j >= 0:
            if matrix[i][j] < target:
                i += 1
            elif matrix[i][j] > target:
                j -= 1
            else:
                return True
        
        return False
