class Solution:
    def translateNum(self, num):
        """
        Args:
            num: int
        
        Return:
            int
        """
        s = str(num)
        a = 1
        b = 1
        for i in range(1, len(s)):
            a, b = b, b + (a if 9 < int(s[i - 1: i + 1]) < 26 else 0)
        return b