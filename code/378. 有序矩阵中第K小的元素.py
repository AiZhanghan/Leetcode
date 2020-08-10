class Solution:
    def kthSmallest(self, matrix, k):
        """
        Args:
            matrix: list[list[int]]
            k: int
        
        Return:
            int
        """
        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if self.counter(matrix, mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left
    
    def counter(self, matrix, mid):
        """
        Args:
            matrix: list[list[int]]
            mid: int
        
        Return:
            int
        """
        i = len(matrix) - 1
        j = 0
        count = 0
        while i >= 0 and j < len(matrix):
            if matrix[i][j] <= mid:
                count += i + 1
                j += 1
            else:
                i -= 1
        return count