class Solution:
    def myPow(self, x, n):
        """
        Args:
            x: float
            n: int
        
        Return:
            float
        """
        if x == 0.0:
            return 0.0
        res = 1
        if n < 0:
            n = -n
            x = 1 / x
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res



# class Solution:
#     def myPow(self, x, n):
#         """
#         Args:
#             x: float
#             n: int
        
#         Return:
#             float
#         """
#         if n < 0:
#             n *= -1
#             x = 1 / x
#         return self.my_pow(x, n)
    
#     def my_pow(self, x, n):
#         """
#         Args:
#             x: float
#             n: int
        
#         Return:
#             float
#         """
#         if n == 0:
#             return 1
#         if n == 1:
#             return x
#         res = self.my_pow(x * x, n // 2)
#         if n % 2:
#             res *= x
#         return res
