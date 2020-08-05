class Solution:
    def titleToNumber(self, s):
        """
        Args:
            s: str
        
        Return:
            int
        """
        res = 0
        for c in s:
            res = res * 26 + ord(c) - ord("A") + 1
        return res


# class Solution:
#     def titleToNumber(self, s):
#         """
#         Args:
#             s: str
        
#         Return:
#             int
#         """
#         dic = {chr(ord("A") + x): 1 + x for x in range(26)}
#         res = 0
#         for c in s:
#             res = res * 26 + dic[c]
#         return res