class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        parameter:
            x: float, base
            n: int, exponent
        return: float
        """
        if x == 0:
            return 0
        
        res = 1
        if n < 0:
            x = 1 / x
            n = -n
        
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1

        return res


# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         """
#         parameter:
#             x: float, base
#             n: int, exponent
#         return: float
#         """
#         if -1 <= n <= 1:
#             return x ** n

#         if n % 2 == 0:
#             return self.myPow(x, n // 2) * self.myPow(x, n // 2)
#         else:
#             return self.myPow(x, (n - 1) // 2) * self.myPow(x, (n - 1)// 2) * x
    