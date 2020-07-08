class Solution:
    def cuttingRope(self, n):
        """
        Args:
            n: int
        
        Return:
            int
        """
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        quotient = n // 3
        remainder = n % 3
        if remainder == 0:
            res = 3 ** quotient
        elif remainder == 1:
            res = 3 ** (quotient - 1) * 4
        else:
            res = 3 ** quotient * remainder
        
        return res % 1000000007