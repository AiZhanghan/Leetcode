class Solution:
    def isPalindrome(self, x):
        """
        Args:
            x: int
        
        Return:
            bool
        """
        if x < 0:
            return False
        div = 1
        while x // div >= 10:
            div *= 10
        while x > 0:
            left = x // div
            right = x % 10
            if left != right:
                return False
            x = (x % div) // 10
            div //= 100
        return True


# class Solution:
#     def isPalindrome(self, x):
#         """
#         Args:
#             x: int
        
#         Return:
#             bool
#         """
#         if x < 0:
#             return False
        
#         temp = x
#         y = 0
#         while temp:
#             y = y * 10 + temp % 10
#             temp //= 10
#         return x == y