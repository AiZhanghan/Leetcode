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
            res += 1
            n &= n - 1
        return res