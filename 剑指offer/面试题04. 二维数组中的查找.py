class Solution:
    def findNumberIn2DArray(self, matrix, target):
        """
        parameter:
            matrix: list[list[int]]
            target: int
        return: bool
        """
        if not matrix:
            return False
            
        res = False

        row = 0
        col = len(matrix[0]) - 1

        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                res = True
                break
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        
        return res
