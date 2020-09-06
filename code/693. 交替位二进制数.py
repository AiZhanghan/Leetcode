class Solution:
    def hasAlternatingBits(self, n):
        """
        Args:   
            n: int
        
        Return:
            bool
        """
        temp = n ^ (n >> 1)
        return temp & (temp + 1) == 0