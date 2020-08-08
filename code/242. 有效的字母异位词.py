class Solution:
    def isAnagram(self, s, t):
        """
        Args:
            s: str
            t: str
        
        Return:
            bool
        """
        if len(s) != len(t):
            return False
        alpha = [0 for _ in range(26)]
        for i in range(len(s)):
            alpha[ord(s[i]) - ord("a")] += 1
            alpha[ord(t[i]) - ord("a")] -= 1

        for i in range(26):
            if alpha[i] != 0:
                return False
            
        return True


# class Solution:
#     def isAnagram(self, s, t):
#         """
#         Args:
#             s: str
#             t: str
        
#         Return:
#             bool
#         """
#         dic = {}
#         for c in s:
#             if c not in dic:
#                 dic[c] = 1
#             else:
#                 dic[c] += 1
#         for c in t:
#             if c not in dic:
#                 return False
#             else:
#                 dic[c] -= 1
#                 if dic[c] == 0:
#                     dic.pop(c)
#         return not dic