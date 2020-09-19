class Solution:
    def translateNum(self, num):
        """
        Args:
            num: int
        
        Return:
            int
        """
        s = str(num)
        if len(s) < 2:
            return len(s)
        
        pre_pre = 1
        pre = 1 if s[0] == "0" or s[0: 2] > "25" else 2
        
        for i in range(2, len(s)):
            cur = pre
            if s[i - 1] != "0" and "0" <= s[i - 1: i + 1] <= "25":
                cur += pre_pre
            pre_pre = pre
            pre = cur
        
        return pre


# class Solution:
#     def translateNum(self, num):
#         """
#         Args:
#             num: int
        
#         Return:
#             int
#         """
#         s = str(num)
#         if len(s) < 2:
#             return len(s)
#         dp = [0 for _ in range(len(s))]
#         dp[0] = 1
#         dp[1] = 1 if s[0] == "0" or s[0: 2] > "25" else 2

#         for i in range(2, len(s)):
#             dp[i] = dp[i - 1]
#             if s[i - 1] != "0" and "0" <= s[i - 1: i + 1] <= "25":
#                 dp[i] += dp[i - 2]
        
#         return dp[-1]
