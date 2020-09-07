class Solution:
    def validPalindrome(self, s):
        """
        Args:
            s: str
        
        Return:
            bool
        """
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return self.is_palindrome(s, l, r - 1) \
                    or self.is_palindrome(s, l + 1, r)
            l += 1
            r -= 1
        return True
    
    def is_palindrome(self, s, l, r):
        """
        Args:
            s: str
            l: int
            r: int
        
        Return:
            bool
        """
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True


if __name__ == "__main__":
    s = "eccer"
    print(Solution().validPalindrome(s))