class Solution:
    def myPow(self, x, n):
        """
        Args:
            x: float
            n: int
        
        Return:
            float
        """
        if n < 0:
            x = 1 / x
            n = -n
        return self.my_pow(x, n)

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
        # if n == 1:
        #     return x
        # if n == 2:
        #     return x * x
        res = self.my_pow(x, n // 2)
        res *= res
        if n % 2:
            res *= x
        return res