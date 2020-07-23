class Solution:
    def add(self, a, b):
        """
        Args:
            a: int
            b: int
        
        Return:
            int
        """
        x = 0xffffffff
        a = a & x
        b = b & x
        while b:
            a, b = a ^ b, (a & b) << 1
        return a if a <= 0x7ffffffff else ~(a ^ x)
        