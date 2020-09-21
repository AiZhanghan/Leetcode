class Solution:
    def twoSum(self, n):
        """
        Args:
            n: int
        
        Return:
            list[float]
        """
        dp = [[0 for _ in range(67)] for _ in range(12)]
        for i in range(1, 7):
            dp[1][i] = 1
        
        for i in range(2, n + 1):
            for j in range(i, 6 * i + 1):
                for k in range(1, 7):
                    if j - k <= 0:
                        break
                    dp[i][j] += dp[i - 1][j - k]
        total = 6 ** n
        res = []
        for i in range(n, 6 * n + 1):
            res.append(dp[n][i] / total)
        return res


# class Solution:
#     def twoSum(self, n):
#         """
#         Args:
#             n: int
        
#         Return:
#             list[float]
#         """
#         dp = [0 for _ in range(6 * n + 1)]
#         dp[1: 7] = [1 for _ in range(6)]

#         for i in range(2, n + 1):
#             for j in range(i * 6, i - 1, -1):
#                 dp[j] = 0
#                 for k in range(1, 7):
#                     if j - k < i - 1:
#                         break
#                     dp[j] += dp[j - k]
        
#         total = 6 ** n
#         res = dp[n: ]
#         print(res)
#         for i in range(len(res)):
#             res[i] /= total
        
#         return res


if __name__ == "__main__":
    n = 2
    print(Solution().twoSum(n))