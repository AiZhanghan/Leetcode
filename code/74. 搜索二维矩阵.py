class Solution:
    def searchMatrix(self, matrix, target):
        """
        Args:
            matrix: list[list[int]]
            target: int
        
        Return:
            bool
        """
        if not matrix:
            return False
    
        left = 0
        right = len(matrix) * len(matrix[0]) - 1

        while left <= right:
            mid = left + (right - left) // 2
            mid_val = self.get_value(matrix, mid)
            if mid_val < target:
                left = mid + 1
            elif mid_val > target:
                right = mid - 1
            else:
                return True
        
        return False


    def get_value(self, matrix, index):
        """
        Args:
            matrix: list[list[int]]
            index: int

        Return:
            int
        """
        n = len(matrix[0])
        row = index // n
        col = index % n
        return matrix[row][col]
