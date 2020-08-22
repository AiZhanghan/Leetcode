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
        
        temp = x
        y = 0
        while temp:
            y = y * 10 + temp % 10
            temp //= 10
        return x == y