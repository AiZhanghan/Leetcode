class Solution:
    def reverseWords(self, s):
        """
        Args:
            s: str
        
        Return:
            str
        """
        s = s.strip()
        i = j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != " ":
                i -= 1
            res.append(s[i + 1: j + 1])
            while s[i] == " ":
                i -= 1
            j = i
        return " ".join(res)
        

# class Solution:
#     def reverseWords(self, s):
#         """
#         Args:
#             s: str
        
#         Return:
#             str
#         """
#         l = 0
#         r = 0
#         res = []

#         while True:
#             l = r
#             while l < len(s) and s[l] == " ":
#                 l += 1
#             if l == len(s):
#                 break
#             r = l
#             while r < len(s) and s[r] != " ":
#                 r += 1
#             res.append(s[l: r])
#             if r == len(s):
#                 break
#         return " ".join(res[::-1])


# class Solution:
#     def reverseWords(self, s):
#         """
#         Args:
#             s: str
        
#         Return:
#             str
#         """
#         return " ".join(reversed(s.split()))
