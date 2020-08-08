class Solution:
    def generate_huiwen(self, s):
        """
        Args:
            s: str
        
        Return:
            str
        """
        for left in range(len(s)):
            if self.is_huiwen(s, left, len(s) - 1):
                return s + s[:left][::-1]
    
    def is_huiwen(self, s, left, right):
        """
        Args:
            s: str
        
        Return:
            bool
        """
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True


if __name__ == "__main__":
    s = input()
    print(Solution().generate_huiwen(s))
    