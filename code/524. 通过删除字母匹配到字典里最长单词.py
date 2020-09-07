class Solution:
    def findLongestWord(self, s, d):
        """
        Args:
            s: str
            d: list[str]
        
        Return:
            str
        """
        res = ""
        for x in d:
            if self.is_subsequence(s, x):
                if len(x) > len(res) or (len(x) == len(res) and x < res):
                    res = x
        return res
    
    def is_subsequence(self, s, x):
        """
        Args:
            s: str
            d: list[str]
        
        Return:
            bool
        """
        p1 = 0
        p2 = 0
        while p1 < len(s) and p2 < len(x):
            if s[p1] == x[p2]:
                p2 += 1
            p1 += 1
        return p2 == len(x)


# class Solution:
#     def findLongestWord(self, s, d):
#         """
#         Args:
#             s: str
#             d: list[str]
        
#         Return:
#             str
#         """
#         d.sort(key=lambda x: (-len(x), x))
#         for x in d:
#             if self.is_subsequence(s, x):
#                 return x
#         return ""
    
#     def is_subsequence(self, s, x):
#         """
#         Args:
#             s: str
#             x: str
        
#         Return:
#             bool
#         """
#         p1 = 0
#         p2 = 0
#         while p1 < len(s) and p2 < len(x):
#             if s[p1] == x[p2]:
#                 p1 += 1
#                 p2 += 1
#             else:
#                 p1 += 1
#         return p2 == len(x)