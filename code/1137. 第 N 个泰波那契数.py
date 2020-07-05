class Solution:
    def tribonacci(self, n):
        """
        Args:
            n: int
        
        Return:
            int
        """
        a, b, c = 0, 1, 1
        for _ in range(n):
            a, b, c = b, c, a + b + c
        return a 