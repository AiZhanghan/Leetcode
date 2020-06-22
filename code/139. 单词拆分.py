from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """DP"""
        wordDict = set(wordDict)
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(0, i):
                if dp[j] and s[j: i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]
        

# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         """记忆化回溯"""
#         self.s = s
#         self.word_dict = set(wordDict)
#         self.memo = [None for _ in range(len(s))]
#         return self.word_break(0)
    
#     def word_break(self, start: int) -> bool:
#         if start == len(self.s):
#             return True
#         if self.memo[start] != None:
#             return self.memo[start]
#         for end in range(start + 1, len(self.s) + 1):
#             if self.s[start: end] in self.word_dict and self.word_break(end):
#                 self.memo[start] = True
#                 return True
#         self.memo[start] = False
#         return False
