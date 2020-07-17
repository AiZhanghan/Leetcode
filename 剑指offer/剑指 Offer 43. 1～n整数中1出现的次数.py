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
        high = int(s[0])
        _pow = pow(10, len(s) - 1)
        last = n - high * _pow
        if high == 1:
            return self.countDigitOne(_pow - 1) + last + 1 + \
                self.countDigitOne(last)
        else:
            return _pow + high * self.countDigitOne(_pow - 1) + \
                self.countDigitOne(last)
                