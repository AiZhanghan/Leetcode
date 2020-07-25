class Solution:
    def mySqrt(self, x):
        """
        Args:
            x: int
        
        Return:
            int
        """
        left = 0
        right = x // 2 + 1
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square > x:
                right = mid - 1
            elif square < x:
                left = mid + 1
            else:
                return mid
        if left * left > x:
            left -= 1
        return left
        