class Solution:
    def myPow(self, x, n):
        """
        Args:
            x: float
            n: int
        
        Return:
            float
        """
        is_negative = False
        if n < 0:
            n = -n
            is_negative = True

        res = self.my_pow(x, n)
        return res if not is_negative else 1 / res
    
    def my_pow(self, x, n):
        """
        Args:
            x: float
            n: int
        
        Return:
            float
        """
        if n == 0:
            return 1
        if n == 1:
            return x
        res = self.my_pow(x * x, n // 2)
        if n % 2:
            res *= x
        return res