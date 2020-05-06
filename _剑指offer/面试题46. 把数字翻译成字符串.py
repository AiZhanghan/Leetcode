# class Solution:
#     def translateNum(self, num: int) -> int:
#         """
#         Args:
#             num: int
#         Return:
#             int
#         """
#         if num <= 9:
#             return 1
#         ba = num % 100
#         if ba <= 9 or ba > 25:
#             return self.translateNum(num // 10)
#         else:
#             return self.translateNum(num // 10) + self.translateNum(num // 100)


class Solution:
    def translateNum(self, num: int) -> int:
        """
        Args:
            num: int
        Return:
            int
        """
        s = str(num)
        dp = [None for _ in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, len(dp)):
            if s[i - 2] == "0" or s[i - 2: i] > "25":
                dp[i] = dp[i - 1]
            else:
                dp[i] = dp[i - 2] + dp[i - 1]
        return dp[-1]
