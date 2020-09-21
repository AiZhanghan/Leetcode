class Solution:
    def add(self, a, b):
        """
        Args:
            a: int
            b: int
        
        Return:
            int
        """
        while b:
            a, b = a ^ b, (a & b) << 1
        return a