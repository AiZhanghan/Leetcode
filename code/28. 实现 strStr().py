class KMP:
    def __init__(self, pat):
        """
        Args:
            pat: str
        """
        self.pat = pat
        M = len(pat)
        self.dp = [[0 for _ in range(256)] for _ in range(M)]
        self.dp[0][ord(pat[0])] = 1
        X = 0
        for j in range(1, M):
            for c in range(256):
                self.dp[j][c] = self.dp[X][c]
            self.dp[j][ord(pat[j])] = j + 1
            X = self.dp[X][ord(pat[j])]
    
    def search(self, txt):
        """
        Args:
            txt: str
        
        Return:
            int
        """
        M = len(self.pat)
        N = len(txt)
        j = 0
        for i in range(N):
            j = self.dp[j][ord(txt[i])]
            if j == M:
                return i - M + 1
        return -1



class Solution:
    def strStr(self, haystack, needle):
        """
        Args:
            haystack: str
            needle: str
        
        Return:
            int
        """
        if not needle:
            return 0
        kmp = KMP(needle)
        return kmp.search(haystack)


# class Solution:
#     def strStr(self, haystack, needle):
#         """
#         Args:
#             haystack: str
#             needle: str
        
#         Return:
#             int
#         """
#         if not needle:
#             return 0
#         for i in range(len(haystack) - len(needle) + 1):
#             j = 0
#             while j < len(needle):
#                 if needle[j] != haystack[i + j]:
#                     break
#                 j += 1
#             if j == len(needle):
#                 return i
#         return -1
        