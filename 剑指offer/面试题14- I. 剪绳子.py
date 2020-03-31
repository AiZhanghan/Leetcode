class Solution:
    def cuttingRope(self, n):
        """
        parameter:
            n: int
        return: int
        """
        if n <= 3:
            res = n - 1
        else:
            a, b = n // 3, n % 3
            if b == 0:
                res = 3 ** a
            elif b == 1:
                res = 3 ** (a - 1) * 4
            else:
                # b == 2
                res = 3 ** a * 2
        return res   

# class Solution:
#     def cuttingRope(self, n):
#         """
#         parameter:
#             n: int
#         return: int
#         """
#         if n == 2:
#             return 1
#         if n == 3:
#             return 2
#         if n == 4:
#             return 4
#         if n == 5:
#             return 6
#         if n == 6:
#             return 9
        
#         dp = [0 for _ in range(n+1)]
#         dp[2] = 1
#         dp[3] = 2
#         dp[4] = 4
#         dp[5] = 6
#         dp[6] = 9

#         for i in range(7, n+1):
#             dp[i] = 3 * dp[i-3]
        
#         return dp[n]
