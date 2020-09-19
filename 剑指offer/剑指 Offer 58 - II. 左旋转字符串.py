class Solution:
    def reverseLeftWords(self, s, n):
        """
        Args:
            s: str
            n: int
        
        Return:
            str
        """
        n = n % len(s)
        return s[n:] + s[:n]