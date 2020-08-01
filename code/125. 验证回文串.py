class Solution:
    def isPalindrome(self, s):
        """
        Args:
            s: str

        Return:
            bool
        """
        temp = []
        for c in s:
            if c.isalnum():
                temp.append(c.lower())
        left = 0
        right = len(temp) - 1
        while left < right:
            if temp[left] != temp[right]:
                return False
            left += 1
            right -= 1
        return True


# class Solution:
#     def isPalindrome(self, s):
#         """
#         Args:
#             s: str

#         Return:
#             bool
#         """
#         left = 0
#         right = len(s) - 1
#         s = s.lower()
#         while left < right:
#             while left < right and not s[left].isalnum():
#                 left += 1
#             while left < right and not s[right].isalnum():
#                 right -= 1
#             if s[left] != s[right]:
#                 return False
#             left += 1
#             right -= 1
            
#         return True