class Solution:
    def countSubstrings(self, s):
        """
        Args:
            s: str
        
        Return:
            res: int
        """
        res = 0
        n = len(s)
        for i in range(n):
            res += self.expand_around_center(s, i, i)
            res += self.expand_around_center(s, i, i + 1)    
        return res

    def expand_around_center(self, s, l, r):
        """
        Args:
            s: str
            l: int
            r: int
        
        Return:
            count: int
        """
        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        return count
