from collections import Counter


class Solution:
    def longestPalindrome(self, s):
        """
        Args:
            s: str
        
        Return:
            int
        """
        counter = Counter(s)
        res = 0
        for value in counter.values():
            res += value - (value & 1)
        if res < len(s):
            res += 1
        return res

# class Solution:
#     def longestPalindrome(self, s):
#         """
#         Args:
#             s: str
        
#         Return:
#             int
#         """
#         counter = Counter(s)
#         has_odd = False
#         res = 0
#         for _, value in counter.items():
#             if value % 2:
#                 has_odd = True
#                 res += value - 1
#             else:
#                 res += value
#         if has_odd:
#             res += 1
#         return res