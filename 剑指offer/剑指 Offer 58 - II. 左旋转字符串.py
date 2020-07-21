class Solution:
    def reverseLeftWords(self, s, n):
        """
        Args:
            s: str
            n: int
        
        Return:
            str
        """
        return s[n:] + s[:n]