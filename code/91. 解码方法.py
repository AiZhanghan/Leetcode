class Solution:
    def numDecodings(self, s):
        """
        Args:
            s: str
        
        Return:
            int
        """
        if not s or s[0] == "0":
            return 0
        
        pre = 1
        cur = 1
        
        for i in range(1, len(s)):
            if s[i] == "0":
                if s[i - 1] not in "12":
                    return 0
                else:
                    next = pre
            else:
                next = cur + (pre if "10" <= s[i - 1: i + 1] <= "26" else 0)
            pre = cur
            cur = next
        return cur


# class Solution:
#     def numDecodings(self, s):
#         """
#         Args:
#             s: str
        
#         Return:
#             int
#         """
#         if not s or s[0] == "0":
#             return 0
#         dp = [0 for _ in range(len(s) + 1)]
#         dp[0] = 1
#         dp[1] = 1
        
#         for i in range(1, len(s)):
#             if s[i] == "0":
#                 if s[i - 1] not in "12":
#                     return 0
#                 else:
#                     dp[i + 1] = dp[i - 1]
#             else:
#                 dp[i + 1] = dp[i] + (dp[i - 1] \
#                     if "10" <= s[i - 1: i + 1] <= "26" else 0)
#         return dp[-1]
                
            
if __name__ == "__main__":
    s = "19961023"
    print(Solution().numDecodings(s))