class Solution:
    def countBinarySubstrings(self, s):
        """
        Args:
            s: str
        
        Return:
            int
        """
        pre = 0
        res = 0

        i = 0
        while i < len(s):
            c = s[i]
            count = 0
            while i < len(s) and s[i] == c:
                count += 1
                i += 1

            res += min(pre, count)
            pre = count
        
        return res


# class Solution:
#     def countBinarySubstrings(self, s):
#         """
#         Args:
#             s: str
        
#         Return:
#             int
#         """
#         group = []
#         i = 0
#         while i < len(s):
#             c = s[i]
#             count = 0
#             while i < len(s) and s[i] == c:
#                 count += 1
#                 i += 1
#             group.append(count)
        
#         res = 0
#         for i in range(len(group) - 1):
#             res += min(group[i], group[i + 1])
#         return res