class Solution:
    def countDigitOne(self, n):
        """
        Args:
            n: int
        
        Return:
            int
        """
        if n <= 0:
            return 0
        s = str(n)
        high = ord(s[0]) - ord("0")
        pow = 10 ** (len(s) - 1)
        last = n - high * pow
        if high == 1:
            return self.countDigitOne(pow - 1) + last + 1 + self.countDigitOne(last)
        else:
            return pow + high * self.countDigitOne(pow - 1) + self.countDigitOne(last)