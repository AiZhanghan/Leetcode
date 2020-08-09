import math


class Solution:
    def isPowerOfThree(self, n):
        """
        Args:
            n: int
        
        Return:
            bool
        """
        if n <= 0:
            return False
        x = math.log(n, 3)
        return abs(x - round(x)) < 10 ** -12
