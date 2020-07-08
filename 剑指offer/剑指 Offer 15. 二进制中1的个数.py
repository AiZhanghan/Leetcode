class Solution:
    def hammingWeight(self, n):
        """
        Args:
            n: int
        
        Return:
            int
        """
        res = 0
        while n:
            n = n & (n - 1)
            res += 1
            
        return res