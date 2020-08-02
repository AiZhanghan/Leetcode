class Solution:
    def partition(self, s):
        """
        Args:
            s: str
        
        Return:
            list[list[str]]
        """
        self.res = []
        self.is_palindrome = [[False for _ in range(len(s))] 
            for _ in range(len(s))]

        for right in range(len(s)):
            for left in range(right + 1):
                if s[left] == s[right] and (right - left <= 2 or 
                    self.is_palindrome[left + 1][right - 1]):
                    self.is_palindrome[left][right] = True

        self._partition(s, 0, [])
        return self.res
    
    def _partition(self, s, index, path):
        """
        Args:
            s: str
            index: int
            path: list[str]
        """
        if index == len(s):
            self.res.append(path[:])
        
        for i in range(index, len(s)):
            if self.is_palindrome[index][i]:
                path.append(s[index: i + 1])
                self._partition(s, i + 1, path)
                path.pop()


# class Solution:
#     def partition(self, s):
#         """
#         Args:
#             s: str
        
#         Return:
#             list[list[str]]
#         """
#         self.res = []
#         self._partition(s, 0, [])
#         return self.res
    
#     def _partition(self, s, index, path):
#         """
#         Args:
#             s: str
#             index: int
#             path: list[str]
#         """
#         if index == len(s):
#             self.res.append(path[:])
        
#         for i in range(index, len(s)):
#             if self.is_palindrome(s, index, i):
#                 path.append(s[index: i + 1])
#                 self._partition(s, i + 1, path)
#                 path.pop()
        
#     def is_palindrome(self, s, start, end):
#         """
#         Args:
#             s: str
#             start: int
#             end: int
#         """
#         res = True
#         while start < end:
#             if s[start] != s[end]:
#                 res = False
#                 break
#             start += 1
#             end -= 1
#         return res